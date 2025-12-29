# VMS Ports | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/vms-ports

VMS Ports
Management Server

(“Master Server”)

TCP

	

inbound/outbound

	







4222

	

in

	

C:\Program Files\DVMS\SystemManagement\NATS\nats-server.exe




5008

	

in

	

C:\Program Files\DVMS\SystemManagement\SMServer.exe




5009

	

out

	

C:\Program Files\DVMS\SystemManagement\SMServer.exe




5010

	

out

	

C:\Program Files\DVMS\SystemManagement\SMServer.exe




8082

	

in

	

C:\Program Files\DVMS\SystemManagement\SMServer.exe




8086

	

in

	

C:\Program Files\DVMS\IncidentReporting\ADVIncidentReporting.exe




8087

	

in

	

C:\Program Files\DVMS\StorageLocker\ADVStorageLocker.exe




8088

	

in

	

C:\Program Files\DVMS\Export\ADVExportService.exe

VMS Server

(“Recording Server”)

TCP

	

inbound/outbound

	







5009

	

in

	

C:\Program Files\DVMS\DVR\DVRServer.exe




5010

	

in

	

C:\Program Files\DVMS\DVR\WDServer.exe




5011

	

in

	

C:\Program Files\DVMS\DVR\DVRServer.exe




5013

	

in

	

C:\Program Files\DVMS\DVR\DVRServer.exe




554

	

out

	

C:\Program Files\DVMS\DVR\DVRServer.exe




80

	

out

	

C:\Program Files\DVMS\DVR\DVRServer.exe




443

	

out

	

C:\Program Files\DVMS\DVR\DVRServer.exe




7001 ->
RTSP Server Streaming

	

out

	

C:\Program Files\DVMS\DVR\DVRServer.exe




UDP

	

inbound/outbound

	







3556-4556

	

out

	

C:\Program Files\DVMS\DVR\DVRServer.exe

Client Applications

TCP

	

inbound/outbound

	







4222

	

out

	

C:\Program Files\DVMS\VAU\Vau.exe

C:\Users\<user>\AppData\Roaming\DVMS\spotter\<versionnumber>\<master server>\spotter.exe

C:\Users\<user>\AppData\Roaming\DVMS\systemmanager\<versionnumber>\<master server>\systemmanager.exe

C:\Users\<user>\AppData\Roaming\DVMS\systemmonitor\<versionnumber>\<master server>\systemmonitor.exe




5008

	

out

	

-"-




5009

	

out

	

-"-




5011

	

out

	

-"-




5013

	

out

	

C:\Users\<user>\AppData\Roaming\DVMS\systemmanager\<versionnumber>\<master server>\systemmanager.exe




UDP

	

inbound/outbound

	







40000 - 50000

	

in

	

Trucast streaming

Spotter Web

TCP

	

inbound/outbound

	







443

	

in

	

C:\Windows\System32\inetsrv\w3wp.exe




4222

	

out

	

-"-




5008

	

out

	

-"-




5009

	

out

	

-"-




5011

	

out

	

-"-

Gateway

TCP

	

inbound/outbound

	







5008

	

out

	

C:\Program Files\DVMS\Gateway\ServiceLauncher.exe




5009

	

out

	

-"-




5011

	

out

	

-"-




9000

	

in

	

-"-

Smart Services
List Management

TCP

	

inbound/outbound

	







5672

	

in

	

C:\Program Files\Erlang OTP\erts-XX.X\bin\erl.exe




8082

	

out

	

C:\Program Files\DVMS\AdvLmService\AdvLmService.exe




8089

	

in

	

-"-

Smart LPR

TCP

	

inbound/outbound

	







5672

	

out

	

C:\Program Files\DVMS\AdvLprService\AdvLprService.exe




8082

	

out

	

-"-




8090

	

In

	

-"-

Smart FR

TCP

	

inbound/outbound

	







5672

	

out

	

C:\Program Files\DVMS\AdvFrService\AdvFrService.exe




8082

	

out

	

-"-




8091

	

In

	

-"-

Smart ODS

TCP

	

inbound/outbound

	







5672

	

in

	

C:\Program Files\Erlang OTP\erts-XX.X\bin\erl.exe




8082

	

out

	

C:\Program Files\DVMS\AdvOdsService\AdvOdsService.exe




8093

	

In

	

-"-

Smart OR

TCP

	

inbound/outbound

	







5672

	

out

	

C:\Program Files\DVMS\AdvOrService\AdvOrService.exe




8082

	

out

	

-"-




8092

	

In

	

-"-

Pagination
Previous page
Networking Best Practices