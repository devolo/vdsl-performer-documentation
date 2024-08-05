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

# This file defines a typical response from a Speedport Smart 3 device when it receives an SSDP discovery request
# and the response to the GetValues request.
port = 49000
location = '/description.xml'

ssdp_rsp = \
	"HTTP/1.1 200 OK\r\n" \
	"CACHE-CONTROL: max-age=1800\r\n" \
	"LOCATION: http://{ip_addr}:49000/description.xml\r\n" \
	"SERVER: Speedport Smart 3 010137.3.0.404.0\r\n" \
	"Date: Date is ignored\r\n" \
	"EXT: \r\n" \
	"ST: urn:telekom-de:device:TO_InternetGatewayDevice:2\r\n" \
	"USN: uuid:00000000-0000-0002-0000-44fffffffe3b38ffffffa2ffffffb4::urn:telekom-de:device\r\n"
values = \
	"HTTP/1.1 200 OK\r\n" \
	"SERVER: Speedport Smart 3 010137.3.0.404.0\r\n" \
	"CACHE-CONTROL: max-age=1800\r\n" \
	"CONTENT-TYPE: text/xml; charset=utf-8\r\n" \
	"CONTENT-LENGTH: \r\n" \
	"\r\n" \
	"<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:cwmp=\"urn:telekom-de.totr64-2-n\">" \
	" <SOAP-ENV:Body>" \
	"  <cwmp:GetParameterValuesResponse>" \
	"   <ParameterList SOAP-ENC:arrayType=\"cwmp:ParameterValueStruct[19]\">" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRGds</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">8</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRGus</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">8</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRpsds</Name>" \
	"	 <Value xsi:type=\"xsd:string\">{snrds}</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRpsus</Name>" \
	"	 <Value xsi:type=\"xsd:string\">{snrus}</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRMTds</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">256</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.SNRMTus</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">256</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.LATNds</Name>" \
	"	 <Value xsi:type=\"xsd:string\">17,47,47,0,0</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.TestParams.LATNus</Name>" \
	"	 <Value xsi:type=\"xsd:string\">7,47,11,0,0</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Channel.1.Stats.Total.XTURFECErrors</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">0</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Channel.1.Stats.Total.XTURCRCErrors</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">0</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.LinkStatus</Name>" \
	"	 <Value xsi:type=\"xsd:string\">Up</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.StandardUsed</Name>" \
	"	 <Value xsi:type=\"xsd:string\">G.993.2_Annex_B</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.CurrentProfile</Name>" \
	"	 <Value xsi:type=\"xsd:string\">17a</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.DownstreamMaxBitRate</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">139815</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.UpstreamMaxBitRate</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">55351</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.DownstreamNoiseMargin</Name>" \
	"	 <Value xsi:type=\"xsd:int\">176</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Line.1.UpstreamNoiseMargin</Name>" \
	"	 <Value xsi:type=\"xsd:int\">199</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Channel.1.DownstreamCurrRate</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">102345</Value>" \
	"	</ParameterValueStruct>" \
	"	<ParameterValueStruct>" \
	"	 <Name>Device.DSL.Channel.1.UpstreamCurrRate</Name>" \
	"	 <Value xsi:type=\"xsd:unsignedInt\">41434</Value>" \
	"	</ParameterValueStruct>" \
	"   </ParameterList>" \
	"  </cwmp:GetParameterValuesResponse>" \
	" </SOAP-ENV:Body>" \
	"</SOAP-ENV:Envelope>"
