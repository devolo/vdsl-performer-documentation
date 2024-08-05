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

# This file defines typical responses from a device implementing the specifications found at https://github.com/devolo/vdsl-performer-documentation.
# - SSDP Response to SSDP Discovery
# - HTTP Response including the UPnP XML description
# - SOAP Response to SOAP Action GetSupportedDataModel
# - SOAP Response to SOAP Action GetSupportedParameters
# - SOAP Response to SOAP Action GetValues

port = 60001
location = '/51625d8d/gatedesc.xml'

ssdp_rsp = \
	"HTTP/1.1 200 OK\r\n" \
	"CACHE-CONTROL: max-age=1800\r\n" \
	"DATE: Thu, 15 Sep 2022 07:25:45 GMT\r\n" \
	"EXT:\r\n" \
	"LOCATION: http://{ip_addr}:60001/51625d8d/gatedesc.xml\r\n" \
	"OPT: \"http://schemas.upnp.org/upnp/1/0/\"; ns=01\r\n" \
	"01-NLS: 7f6b668c-34c7-11ed-a091-92417c447b47\r\n" \
	"SERVER: Unspecified, UPnP/1.0, Gateway company\r\n" \
	"X-User-Agent: redsonic\r\n" \
	"ST: urn:schemas-upnp-org:service:ConfigurationManagement:2\r\n" \
	"USN: uuid:51625d8d-cf52-3074-91e1-584cfa6febf0::urn:schemas-upnp-org:service:ConfigurationManagement:2\r\n"
description = "HTTP/1.1 200 OK\r\n" \
	"Content-Type: text/html; charset=UTF-8\r\n" \
	"CONTENT-LENGTH: 1594\r\n" \
	"\r\n" \
	"<?xml version=\"1.0\"?>" \
	"<root xmlns=\"urn:schemas-upnp-org:device-1-0\" configId=\"configuration number\">" \
	"<specVersion>" \
	"<major>2</major>" \
	"<minor>0</minor>" \
	"</specVersion>" \
	"<device>" \
	"<deviceType>urn:schemas-upnp-org:device:deviceType:v</deviceType>" \
	"<friendlyName>short user-friendly title</friendlyName>" \
	"<manufacturer>manufacturer name</manufacturer>" \
	"<manufacturerURL>URL to manufacturer site</manufacturerURL>" \
	"<modelDescription>long user-friendly title</modelDescription>" \
	"<modelName>model name</modelName>" \
	"<modelNumber>model number</modelNumber>" \
	"<modelURL>URL to model site</modelURL>" \
	"<serialNumber>manufacturer's serial number</serialNumber>" \
	"<UDN>uuid:UUID</UDN>" \
	"<UPC>Universal Product Code</UPC>" \
	"<iconList>" \
	"<!-- not of interest -->" \
	"</iconList>" \
	"<serviceList>" \
	"<service>" \
	"<serviceType>urn:schemas-upnp-org:service:ConfigurationManagement:2</serviceType>" \
	"<serviceId>urn:upnp-org:serviceId:serviceID</serviceId>" \
	"<SCPDURL>URL to service description</SCPDURL>" \
	"<controlURL>http://{ip_addr}:60001/ConfigurationManagement</controlURL>" \
	"<eventSubURL>URL for eventing</eventSubURL>" \
	"</service>" \
	"</serviceList>" \
	"<deviceList>" \
	"<!-- Can include embedded devices with the same information as the root device including a serviceList -->" \
	"</deviceList>" \
	"<presentationURL>URL for presentation</presentationURL>" \
	"</device>" \
	"</root>"
supp_data_models = \
	"HTTP/1.1 200 OK\r\n" \
	"CONTENT-TYPE: text/xml; charset=\"utf-8\"\r\n" \
	"DATE: Fri, 26 Aug 2022 23:06:04 GMT\r\n" \
	"SERVER: SOP/10.1 UPnP/2.0\r\n" \
	"CONTENT-LENGTH: 770\r\n" \
	"\r\n" \
	"<?xml version=\"1.0\"?>\n" \
	"<s:Envelope\n" \
	"xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\"\n" \
	"s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n" \
	"<s:Body>\n" \
	"<u:GetSupportedDataModelsResponse xmlns:u=\"urn:schemas-upnp-org:service:ConfigurationManagement:2\">\n" \
	"<cms:SupportedDataModels xmlns:cms=\"urn:schemas-upnp-org:dm:cms\">\n" \
	"<SubTree>\n" \
	"<URI>urn:broadband-forum-org:tr-181-2-0</URI>\n" \
	"<Location>/BBF/</Location>\n" \
	"<URL>https://cwmp-data-models.broadband-forum.org/tr-181-2-0-0.xml</URL>\n" \
	"<Description>TR-181</Description>\n" \
	"</SubTree>\n" \
	"</cms:SupportedDataModels>\n" \
	"</u:GetSupportedDataModelsResponse>\n" \
	"</s:Body>\n" \
	"</s:Envelope>\n"
supp_parameters = \
	"HTTP/1.0 200 OK\r\n" \
	"CONTENT-TYPE: text/xml; charset=\"utf-8\"\r\n" \
	"DATE: when response was generated\r\n" \
	"SERVER: OS/version UPnP/2.0 product/version\r\n" \
	"CONTENT-LENGTH: \r\n" \
	"\r\n" \
	"<?xml version=\"1.0\"?>" \
	"<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">" \
	"<s:Body>" \
	"<u:GetSupportedParametersResponse xmlns:u=\"urn:schemas-upnp-org:service:ConfigurationManagement:2\">" \
	"<cms:Result xmlns:cms=\"urn:schemas-upnp-org:dm:cms\">" \
	"<cms:StructurePathList>" \
	"<StructurePath>" \
	"/BBF/DSL/Channel/0/DownstreamCurrRate" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Channel/0/UpstreamCurrRate" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRGds" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRGus" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRpsds" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRpsus" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRMTds" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/TestParams/SNRMTus" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/LinkStatus" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/CurrentProfile" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/DownstreamNoiseMargin" \
	"</StructurePath>" \
	"<StructurePath>" \
	"/BBF/DSL/Line/0/UpstreamNoiseMargin" \
	"</StructurePath>" \
	"</cms:StructurePathList>" \
	"</cms:Result>" \
	"</u:GetSupportedParametersResponse>" \
	"</s:Body>" \
	"</s:Envelope>"
values = \
	"HTTP/1.0 200 OK\r\n" \
	"CONTENT-TYPE: text/xml; charset=\"utf-8\"\r\n" \
	"DATE: when response was generated\r\n" \
	"SERVER: OS/version UPnP/2.0 product/version\r\n" \
	"\r\n" \
	"<?xml version=\"1.0\"?>" \
	"<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">" \
	"<s:Body>\r\n" \
	"<u:GetValuesResponse xmlns:u=\"urn:schemas-upnp-org:service:ConfigurationManagement:2\">" \
	"<cms:ParameterValueList xmlns:cms=\"urn:schemas-upnp-org:dm:cms\">" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRGds</ParameterPath>\n" \
	"<Value> 8 </Value>\n" \
	"</Parameter>" \
	"<Parameter>\n" \
	"\t<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRGus</ParameterPath>\n" \
	"\t<Value>8</Value>\n" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRpsds</ParameterPath>" \
	"<Value>{snrds}</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRpsus</ParameterPath>" \
	"<Value>{snrus}</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRMTds</ParameterPath>" \
	"<Value>256</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/SNRMTus</ParameterPath>" \
	"<Value>256</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/LATNds</ParameterPath>" \
	"<Value>17,47,47,0,0</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/TestParams/LATNus</ParameterPath>" \
	"<Value>7,47,11,0,0</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Channel/0/Stats/Total/XTURFECErrors</ParameterPath>" \
	"<Value>0</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Channel/0/Stats/Total/XTURCRCErrors</ParameterPath>" \
	"<Value>0</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/LinkStatus</ParameterPath>" \
	"<Value>Up</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/StandardUsed</ParameterPath>" \
	"<Value>G.993.2_Annex_B</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/CurrentProfile</ParameterPath>" \
	"<Value>17a</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/DownstreamMaxBitRate</ParameterPath>" \
	"<Value>139815</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/UpstreamMaxBitRate</ParameterPath>" \
	"<Value>55351</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/DownstreamNoiseMargin</ParameterPath>" \
	"<Value>176</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Line/0/UpstreamNoiseMargin</ParameterPath>" \
	"<Value>199</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Channel/0/DownstreamCurrRate</ParameterPath>" \
	"<Value>102345</Value>" \
	"</Parameter>" \
	"<Parameter>" \
	"<ParameterPath>/BBF/DSL/Channel/0/UpstreamCurrRate</ParameterPath>" \
	"<Value>41434</Value>" \
	"</Parameter>" \
	"</cms:ParameterValueList>" \
	"</u:GetValuesResponse>\r\n" \
	"</s:Body>" \
	"</s:Envelope>\r\n"
