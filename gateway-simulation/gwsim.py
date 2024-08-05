# Copyright (c) 2024, devolo solutions GmbH
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import time
import re
import socket
import select
import struct
from importlib.machinery import SourceFileLoader

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("ip_addr", type=str, help="Local IP address of gateway simulator.")
parser.add_argument("-r", dest="rsp_file", type=str, help="File with responses to use (default rsp_generic.py).")
parser.add_argument("-s", dest="snr_file", type=str, help="File with SNR values to use (default snr_default.py).")

args = parser.parse_args()

if not args.rsp_file:
	args.rsp_file = 'rsp_generic.py'
rsp = SourceFileLoader("responses", args.rsp_file).load_module()

if not args.snr_file:
	args.snr_file = 'snr_default.py'
snr = SourceFileLoader("snr", args.snr_file).load_module()

# Socket to receive SSDP messages
ssdp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ssdp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mreq = struct.pack("4s4s", socket.inet_aton("239.255.255.250"), socket.inet_aton(args.ip_addr))
ssdp_sock.bind(("239.255.255.250", 1900))
ssdp_sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Socket to receive unicast messages sent to address mentioned in SSDP Discovery response
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(("", rsp.port))
server_sock.listen()
read_list = [ssdp_sock, server_sock]
while True:
	print("Waiting for connection...")
	readable, writable, exceptional = select.select(read_list, [], read_list)
	for s in readable:
		if s is server_sock:
			print("Connection established")
			conn, addr = server_sock.accept()
			with conn:
				print(f"Connected by {addr}")
				contents = ''
				while True:
					data = conn.recv(1500)
					if not data:
						print("End of reception")
						break
					# print(f"Received {data}")
					contents += data.decode("utf-8")
					if len(contents) < 1400 or contents.endswith(">"):
						if re.search(rf".*GET " + rsp.location + ".*", contents):
							print("Answering request for description")
							conn.send(bytes(rsp.description.format(ip_addr=args.ip_addr), "utf-8"))
							break
						elif re.search(rf".*GetSupportedDataModels.*", contents):
							print("Answering request for GetSupportedDataModels")
							conn.send(bytes(rsp.supp_data_models, "utf-8"))
							break
						elif re.search(rf".*GetSupportedParameters.*", contents):
							print("Answering request for GetSupportedParameters")
							conn.send(bytes(rsp.supp_parameters, "utf-8"))
							break
						elif re.search(rf".*GetValues.*", contents) or re.search(rf"POST / .*", contents):
							print("Answering request for GetValues")
							conn.send(bytes(rsp.values.format(snrds=snr.snrds, snrus=snr.snrus), "utf-8"))
							break
					else:
						print("Continue reception")
				conn.close()
		else:
			data, addr = ssdp_sock.recvfrom(1500)
			# print(f"received ssdp {data} from {addr}")
			if re.search(rf".*urn:schemas-upnp-org:service:ConfigurationManagement:2.*", data.decode("utf-8")):
				print(f"Received discover, answering to {addr}")
				ssdp_sock.sendto(bytes(rsp.ssdp_rsp.format(ip_addr=args.ip_addr), "utf-8"), addr)
server_sock.close()
ssdp_sock.close()
