# Troubleshooting Network Issues | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/troubleshooting-network-issues

Troubleshooting Network Issues

The most noticeable error that can occur in the VMS’ operation would be a failure to receive a video feed from a camera.
The reasons for this include, but are not limited to, physical connection errors (cable disconnected, disrupted or improperly connected), logical connection errors (configuration errors, e.g. wrong addresses incorrect camera login details or command typos) or device or component failures at any point in the network (cameras, servers, networking devices, clients).
If a client views footage from a remote site, failures in the connection beyond a VMS site could include connection configuration errors or ISP network faults.

Troubleshooting Tools
Web browsers

Web browsers can be used to troubleshoot IP cameras and networking devices in a few ways if their interface IP addresses are known:

Connection testing: If a web browser is unable to reach a device’s GUI interface through its IP address, it indicates some manner of connection problem or issues with its software.

This method is a basic “Can I contact it” type of connection testing, only telling if there’s a need to use the previously mentioned tools to diagnose network issues.

At a later point, it can be used for HTTP connection testing.

Remote configuration: When a web browser has established contact with the device, it usually opens a simple web page that functions as the GUI for the device.

The device’s settings can be configured through this interface.

WireShark

WireShark is a web sniffer program that allows the user to monitor network traffic that the device the application is installed on can perceiver.
This allows the user to examine flows of packets to and from the device and whatever end devices there are at the other end of the exchanges.
The packets that have been read can be opened and examined by the user.
The application is free and it comes with all the necessary components as well as WinPcap, a link-layer packet capture driver for Windows.

Windump

WinDump is a Microsoft Windows port of tcpdump, a command-line basic packet analyzer program.
The program uses WinPcap to capture packets for analysis and inspection.
The program is able to view unencrypted traffic and open the information contained therein.

Iperf

Iperf is a network performance measuring tool that uses WinPcap. The basic application is free, but a GUI version is not.
The application is installed on two devices at the endpoints of a connection and they’re set to transmit TCP or UDP streams between each other.
This can be used to test connection issues between end devices. Packet sizes can be easily changed to gauge traffic impact on bandwidth.

Command Lines

Command-line utilities are accessed through the Windows command prompt.
The command-line formats presented in this section will be in the format of command (optional) [required] <description>.
The description within a field explains the argument. An argument outside of the description brackets is the proper syntax for it.

Ping

The command utility ping is used to test communications between the pinging device and the target IP/hostname.
A ping can indicate response times from the destination when successful. It can also indicate whether there’s a problem on the local end when trying to contact the destination (Request timed out) or if there’s a problem on the destination network (Destination host unreachable).
The format for the command is presented below. The command can have numerous arguments to specify the actions the command will perform.
ping (<argument>) [<destination hostname or IP address>]

Netstat

The command utility netstat displays various network statistics for the device in the command prompt window.
This can be used to discover port issues and other connection issues on the device.
The format for the command is presented below. The command can have numerous arguments to specify the actions the command will perform.
netstat (<arguments>)
Results are displayed in the command prompt or in a text file if so instructed by the user.
To have the output of a netstat command saved as a text file, enter the command with the modifier “>”, followed by a name for the file.
The text file is saved on the device’s C:/ drive.
netstat –abn >output.txt

Arp

The command utility arp is used to access the ARP (Address Resolution Protocol) cache on the device. arp –a displays the cache in the command prompt and arp –d deletes named entries in the cache.
The ARP cache is refreshed every time the device pings a destination host or the network at large. ARP can be used to view devices on the connected network by their MAC and IP addresses.
The format for the command is presented below.
ARP [<argument>] (<IP address>) (<MAC address>) (if_addr < IP address of the interface whose address translation table should be modified>)

Traceroute

The command utility tracert is used to map the route packets would take in the network to their destination as well as the time it takes for them to make each hop.
This can be used to determine failure points in a network as well as incorrect routing.
The format for the command is presented below.
The command can have numerous arguments to specify the actions the command will perform.
tracert (<arguments>) [<destination hostname or IP address>]

Nslookup

The command utility nslookup is used to look up the domain name or IP address in the DNS lookup server.
The format for the command is presented below. Typing only the base command displays the information for the device’s DNS server.
nslookup [-option] (host <destination hostname or IP address>) (server <non-default server’s hostname or IP address>)

Telnet

Telnet is a text-based terminal connection over TCP, allowing direct, unencrypted communication between devices.
This can be used to remotely contact, use and, if need be, configure networking devices through their CLI interfaces. To telnet (open a Telnet connection), the command is typed in with the relevant arguments in the command prompt.
The format for the command is presented below. The command can have numerous arguments to specify the actions the command will perform.
telnet [<destination hostname or address>] (<port number>)
Telnetting to network devices is highly recommended to be done within the local network the device is connected to, as the communication is unsecured.

VLC

The VLC media player is a freeware media player application that can contact streaming addresses over an IP network.
To receive a stream from an IP source:

Launch the VLC application

Click Media  Open Network Stream…

Click the Network tab

Enter the camera URL:

[protocol]://[camera IP/domain name]:[port]/[destination file/function]?[argument]

Play video

The protocol for the connection can be anything
The potential arguments in the URL include but are not limited to, a username and password set for that camera.
If camera connections are being tested without having set a password or username on them, the device needs to be kept on an isolated network.
Consult the program’s documentation for further information on the media player functionalities.

Simultaneous Camera Channel Failures


This issue is more of a concern for larger surveillance system networks involving networking on many levels across many local sites.
Larger systems require more networking devices between the system components, and every added device brings a potential failure point.
If multiple related cameras go offline at once on a video matrix, it would point to a camera cluster losing connectivity.

Usually, it would point to a server or switch failing:

If cameras opened in the Spotter client disconnect when the client has opened a session with a DVRServer, there are issues with the service, its server or its connection to the system.

If ThruCast has been enabled, it can stream camera footage without DVRServer.

If there’s a failover server, it will take over, but the client needs to connect to it.

If some of the cameras fail simultaneously, it would point to a switch losing power, the connection failing or otherwise being disabled.

Check if the connection is still intact.

The only form of troubleshooting for switch device failures would be replacing the switch as soon as possible.

Master Failover

SMServer failures can be noticed by the end-user with the Spotter for Windows client falling back to the login state.
Normally these are recovered from when the service is restarted on the Master.
In the event of a SMServer cannot be restored, nothing can currently be done except to physically replace the Master.
The functionality for a Failover Server to take over for a crashed Master is currently in development, but for the time being, other means need to be used, such as offline pre-configured spare Masters.
This will not make recovery immediate, but it would help reduce downtime.

Port Conflicts

Port conflicts arise in situations where there are two or more applications on a computer that use the same ports for communication.
VMS applications’ ports do not conflict with each other, but a situation might come up where a third-party program is trying to use the ports that the VMS components use, leading to either program not connecting over the network.
To discover port conflicts on Microsoft devices, open a command prompt and enter a netstat command to list all ports. It is recommended to use modifiers to narrow down the list.

netstat –abn

a displays all active TCP connections and the TCP and UDP ports on which the computer is listening

b displays the executable's name involved in the creation of each connection and/or listening port (this requires running the command prompt as an administrator of the device)

n displays active TCP connections with addresses and port numbers numerically expressed

For devices using Linux and Mac OS operating systems, lsof command can be used instead of netstat to list all ports. It is recommended to use modifiers to narrow down the list.

lsof -i

i lists the device’s IP sockets

When a port conflict is discovered, the next step is to resolve it. One way of doing this is to reassign an application’s port to another number.
E.g. if there’s a conflict between two applications in TCP port 800, either of the conflicting applications needs to be ported through TCP port 801.
If port numbers are to be changed for an application, these changes must be consistent.

Device Discovery

Adding cameras to a camera network is like adding any other networked device to the network.
It is recommended to first read the camera instruction manuals and configure the devices before connecting them to the network.
It is also recommended to document all vital information on the devices, including their MAC addresses.
Normally camera discovery and adding them to the system is handled through the System Manager application that controls the SMServer.
IF the camera has not been configured, including its IP address setting, and have connected it to the network, you can either contact your IT department so they could look up the device’s address in the router, or you could use ARP to discover the device, should IT not be available.
IF you have not configured the IP address for the camera and have it connected to the network, you can either contact your IT department so they could look up the device’s address in the router, or you could use ARP to discover the device, should IT not be available.
Devices in an IP network are discovered by using ARP (Address Resolution Protocol) requests whenever a ping command is enacted on a networked device.
To discover the IP address of a device with a known MAC address, it’s possible to perform a reverse ARP request.
This involves pinging the connected subnet’s broadcast address (the last address of a subnet e.g. 192.168.1.255 on a 192.168.1.0/24 subnet).
Pinging will also send automatic ARP requests to the whole subnet. The ping will return a timeout result.

After pinging the network, type in the command arp –a to get a list of all connected devices in the network and browse them until the newly connected camera is found.
Write down the IP address of the device. Use the IP address in the System Manager to add the camera to the VMS.
This method can also be used to discover other devices added to your network. If you are unsure about a device added to the network, it’s best to investigate it with the help of any resident IT personnel.

Pagination
Previous page
ThruCast
Next page
Networking Best Practices