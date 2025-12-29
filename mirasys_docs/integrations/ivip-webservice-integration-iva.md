# ivIP Webservice integration (IVA) | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/ivip-webservice-integration-iva

ivIP Webservice integration (IVA)

This integration allows send VMS alarms to Innovative ISM using ivIP Webservice.

Requirements

Mirasys VMS 9.6 or newer

ISMivIP Web Service SMEventProvider SMEventSDK feature on license

Configuration

Configuration file is located on default under SystemManagement.
C:\Program Files\DVMS\SystemManagement\SMEventProviders

Default configuration file name is SMEventProviderISMivIPWebService.xml.

Start configuration that you create own profile for integration, example profile name ivIP.

Then create own user for this profile, example username ivIP.

Bound profile and user together.

Add all needed cameras and text channels to this profile.

Recommend way is to create folder based on server name and then add cameras and text channels under that as own folders.

Integration use this data to generate ready on configuration file, where is only needed to change receiver details (server IP-address, port and ivAuth), source zone (ivChip) and zone per device (ivZone).

There is also option to add own marking for source details to help understand what is this site.

If there is happening change on device names, these need to apply manually in configuration file.

Now open this SMEventProviderISMivIPWebService.xml in example Notepad++ software and edit wanted details and enable this integration changing Enabled value to true.

After this you can restart SMserver and this generate configuration data based on created profile.

When file is created, these is need to reopen this configuration file and change ivAuth, ivChip and ivZone details.

There is option edit comment formant using this line in XML configuration

XML
<CommentFormat value="$AlarmSource $AlarmName $AlarmType"


There is a limit for avComment value string on 80 symbols

When that is done, you need restart SMserver, which load current configuration to system and start sending data to ivIP Webservice.

If there is made change etc. on profile side, system automatically add these new sites/devices to configuration.

This not update sites/devices names to XML file, this need to be done manually editing that configuration file.

System make automatically 2 backups from this configuration file based on changes.

VMS upgrade overwrite this file, please make backup before VMS upgrade.

Example message
XML
POST /interVIEW_Alarm/interVIEW_AlarmMake HTTP/1.1
Content-Type: text/xml;charset="utf-8"
User-Agent: Mirasys User Agent
SOAPAction: http://www.innovative.dk/interVIEW_Alarm/interVIEW_AlarmMake
Host: 127.0.0.1:8090
Content-Length: 599
Expect: 100-continue
Connection: Keep-Alive
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance">>
<soapenv:Body>
<interVIEW_AlarmMake xmlns="http://www.innovative.dk/interVIEW_Alarm">
<ivAuth>1</ivAuth>
<ivChip>123456</ivChip>
<ivZone>12</ivZone>
<ivType>A</ivType>
<ivComment>Camera 1 Motion detected:Camera</ivComment>
<ivLatitude></ivLatitude>
<ivLongitude></ivLongitude>
<ivExtra></ivExtra>
</interVIEW_AlarmMake>
</soapenv:Body>
</soapenv:Envelope>

Troubleshooting

If you want to check what kind of data is sent out, then you can create text channel and send data to that IP-address and port.





If configuration file is not made correctly, you can see error related to this in SMserver log files.

If there is problem to send data to ivIP server, you can see error related to this in SMserver log files.

If there is need to do deeper debug, then this can be done editing SMServer.exe.config file.

Default location C:\Program Files\DVMS\SystemManagement

Open this file using Notepad using Administrator rights and edit line 31
<level value="INFO" /> to <level value="DEBUG" />
Then save this file and restart SMserver

Pagination
Previous page
Hikvision Proxy
Next page
Lenel OnGuard