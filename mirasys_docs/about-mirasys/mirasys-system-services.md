# Mirasys System Services | Mirasys Help Center

Source: https://documentation.mirasys.com/about-mirasys/about/mirasys-system-services

Mirasys System Services
SMServer

SMServer (System Management Server) is the Master server service.
SMServer is used to assign a server in the system as a Master that acts as the focal point in communicating with the client applications and the other servers in the system.
A VMS must have a server assigned as a Master with SMServer on it connected to the system network.
SMServer listens on TCP port 5008 for the client applications.
SMServer uses TCP port 5009 to connect to the system network’s other servers for time synchronization, settings changes, receiving event information etc.
The service maintains the system state and system data, e.g. server information, system clock, users and profiles.
SMServer maintains connections to all the watchdog services in the system and receives and logs monitoring events.
Upgrading the system servers and clients is done through SMServer.
Alarm events and the audit trail are recorded in the server database. In larger environments, a SQL Server database can be used to store alarm and audit trail databases.
Audit trails record user activities in the system.
A Master server with SMServer can support up to 150 recording VMS servers that are referred to as Slaves.
A Slave can be any server device with the DVRServer service installed and enabled.
The service must be installed on a computer or server with Microsoft operating systems Windows 10, Windows 11, Server 2012, Server 2016 R2 or Server 2019.
The device can also be a virtual device running in Hyper-V and VMware virtual machine platforms. 

DVRServer

DVRServer is the service installed on servers set up as recording devices in the VMS network.
This sets them up to store video data sent by the cameras.
They receive footage and save it on their hard drives with metadata saved on the common database.
The servers also perform VCA, motion detection and send out alarms, should pre-defined criteria for such be fulfilled.
Servers with DVRServer require two NICs on their hardware: one to communicate with IP camera networks, the other for server-server/server-client communication.
Devices meant to capture footage from analogue cameras need to have capture cards installed or instead receive traffic from an IP encoder with the analogue cameras connected to it.
It is advisable to keep IP cameras on a separate network from the recording servers and the only cameras directly connected to the recording servers are analogue cameras connected to said servers’ capture cards.
DVRServer listens on TCP port 5009. Video, audio and data streams require TCP port 5011 to be open.
DVRServer never contacts the applications (Spotter for Windows and System Manager) or SMServer.
However, if IP cameras are installed in the system, servers contact the IP cameras using TCP or UDP depending on the camera model.
The service must be installed on a computer or server with Microsoft operating systems Windows 10, Windows 11, Server 2012, Server 20016 R2 or Server 2019.
The device can also be a virtual device running in Hyper-V and VMware virtual machine platforms. 

WDServer

WDServer is the Watchdog server service that functions as the system monitor. It monitors local DVRServer and SMServer services and is responsible for seeing that both services are running and operating normally.
During normal monitoring, it will save events to a local event buffer (max. 100 individual events).
These events can be used to trigger digital outputs in DVRServer. WDServer can also be configured to send emails.
Even if neither is configured, WDServer will always log the events in a log .txt file, with C:\Users\[Window user]\AppData\Roaming\DVMS\DVR Application\Logs folder being the default.
In severe situations such as a system malfunction or hard drive failure, Watchdog can do a number of preset tasks, e.g. restart the affected computer or send e-mail messages containing information about the malfunction.
If the system Master is down, the error situations will be notified once the SMServer service is up again.
Error situations will not cause the watchdog to initiate a rebooting loop.
Any reboots by WDServer will be followed by changing the faulty component to an error-tolerant state (e.g., disabling a faulty channel).
Rebooting will never be done more than once per 6-hour cycle.
If other faults or errors normally resulting in a reboot occur, these will be logged but not acted upon.
WDServer is automatically installed with SMServer and DVRServer.
WDServer takes care of the connections and operational reliability of the VMS system through TCP port 5010.
The Watchdog records GatewayServer and SMS service up/down events if they’re installed on the same device as the Watchdog. If these services go down, the application restarts them.
The service must be installed on a computer or server with Microsoft operating systems Windows 10, Windows 11, Server 2012, Server 20016 R2 or Server 2019.
The device can also be a virtual device running in Hyper-V and VMware virtual machine platforms.

GatewayServer

The optional GatewayServer service must be installed on a computer with Microsoft Windows 7, Server 2008, Server 2008 R2 or Server 2012 operating systems.
The computer must have HTTP software installed. Mirasys VMS software is not required on the server.
The GatewayServer contacts the SMServer through TCP port 5008.
When the WebClient Java applet or the Spotter Mobile application is used, GatewayServer and the applet or application communicate by default through TCP ports 9999 (download applet) and 9000 (direct communication between the server and the applet/application).
These TCP ports can be changed during the GatewayServer installation or at a later point by editing the ServiceLauncher.exe.config configuration file in the service’s installation folder (default C:\Program Files\DVMS\Gateway).

Pagination
Previous page
Mirasys VMS Applications
Next page
Mirasys VMS System components