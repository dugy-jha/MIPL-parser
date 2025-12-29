# System Requirements | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/system-requirements

System Requirements

The Mirasys VMS (Video Management System) software is a flexible and scalable network video recording software that consists of Mirasys server software and client application software.
The server and client software can be installed on any standard PC platform that fulfils the hardware and operating system (OS) requirements.

Servers may also be virtualized using, e.g., Microsoft Hyper-V or VMWare.
Mirasys VMS is delivered either in pre-assembled servers or as software-only, in which case the distributor/reseller, an integrator/installer or the end-customer installs the software on a PC.
The performance of a Mirasys VMS solution depends on several factors such as processor type and speed, available memory, and network bandwidth.

The requirements below define the minimum requirements for running Mirasys VMS software with IP surveillance cameras.

The examples presented in this document should only be used as a base guideline when planning to set up a system.

For a detailed calculation of system performance and storage capacity requirements, please refer to your Mirasys sales contact or an authorized distributor/reseller.

Please note also that the performance and functionality of a VMS system's server or client software are guaranteed only when it runs as the sole application on the PC platform.

No other software applications – with the exception of dedicated server software such as Mirasys ANPR+ (Automatic Number Plate Recognition), Mirasys Reporting+, Mirasys VCA (Video Content Analytics), or Microsoft SQL Server when required – should be installed on the computer on which the Mirasys VMS server or client applications are executed.

It is also recommended that server and client software should be used on separate computers.

Minimum Server Requirements

The servers require this minimum (small) system configuration:

Hardware:

Intel Core i3, or better

8 GB of RAM recommended

Min. 1 TB HDD

Min 100 GB C: drive space

In a basic configuration, one hard disk may be enough, but for secure multi-disk recording (modified RAID 0), at least two disk units are required.
A separate disk for the operating system and application software is also recommended.
The use of 24/7 optimized HDDs is highly recommended.

The VMS software reserves by default 90% of available disk space on other drives than the C-drive for storage use.

It does not use the C-drive for storage, except when it is the only drive.

Display adapter with at least 128 MB memory (a dual-head display adapter is optional).

Please note that display adapter performance can vary greatly depending on the adapter and the bus architecture used to connect the adapter to the motherboard.

Two 1 Gbps (separate network connections for the camera network and the system network, see the Mirasys VMS Networking for further information).

Minimum Client Workstation Requirements

These are the minimum requirements for Mirasys VMS client applications (such as Spotter for Windows or the System Manager).
The following hardware specification should be viewed only as of the minimum requirements for a small-scale surveillance system.

Intel Core i3, or better (when using H.264 cameras in the system, quad-core processors are recommended).
The recommended processor allows simultaneous viewing of more than 10 cameras at a higher resolution than VGA (640×480).

Min. 8 GB RAM recommended

Min. 20 GB of free disk space

Display adapter with at least 512 MB of memory. Video adapter memory amount and performance will impact capacity to display simultaneous recorded or live camera streams.

Please note that display adapter performance can vary greatly depending on the adapter and the bus architecture used to connect the adapter to the motherboard.

Windows OS Compatibility
Mirasys VMS V9 supports the following operating systems:

Operating System

	

Server with analogue camera support via capture cards

	

Server with only IP cameras or connected video servers (encoders)

	

Gateway server

	

System Manager client application

	

Spotter for Windows client application




Windows 10

	

-

	

X

	

X

	

X

	

X




Windows 11

	




	

X

	

X

	

X

	

X




Windows Server 2016

	

-

	

X

	

X

	

X

	

X




Windows Server 2019

	

 

	

X

	

X

	

X

	

X




Windows Server 2022

	




	

X

	

X

	

X

	

X

Network Requirements

These network requirements apply to systems where users access the servers over a network.

General

A 1 Gbps Ethernet is required on both the client and the server-side.
Data can be transmitted over the Internet, Intranet, LAN, WAN, WLAN, ISDN, ADSL, or any other network using TCP/IP.
For best performance, the camera network should be closed to other network traffic and kept separate from the system network used for server-server or server-client communication.
It is heavily recommended to have at least two 1 Gbps network adapters for each server: at least one adapter for the camera feeds and one adapter for server-client and server-server communications.
In the case of large systems with multiple high resolution and high frame rate cameras, separating specific camera sets into their own networks (and adding network adapters to servers) can be recommended.
However, this is done case-by-case and requires specific calculations on network load.
PTZ (Pan-Tilt-Zoom) control requires a low latency in the network to make dome control as responsive as possible.

Network Card Settings

Network card setting requirements:

Interrupt Moderation Rate --> Extreme

Receive Buffers/Receive Descriptors --> 2048

Transmit Buffers/Transmit Descriptors --> 2048

If the network card cannot be adjusted to these settings, replace the card.

IP Addresses

The servers must have static IP addresses so that the client programs can connect to them.
The Agile Virtual Matrix (AVM) Display Servers should also have either static addresses or names.
The AVM operator console connection to the display servers is made either with an IP address or computer name.

You can use some NAT solutions with the system but not all:

Static network address translation (NAT) can be used between the servers and the client programs. 

Dynamic NAT cannot be used because the IP addresses can change. 

Single-address NAT works if there is only one server in the NAT system. It does not work if there is more than one server in the same system.

Ports

Port

	

Protocol

	

Service

	

Direction




5008

	

TCP

	

SMServer

	

OUT




5009

	

TCP

	

DVRServer

	

OUT




5010

	

TCP

	

WDServer

	

OUT




5011

	

TCP

	

DVRServer

	

OUT




8081

	

TCP

	

SMServer

	

OUT




8082

	

TCP

	

SMServer

	

OUT




8083

	

TCP

	

DVRServer

	

OUT




3556-4556

	

UDP

	

DVRServer

	

IN




554

	

RTSP

	

DVRServer

	

IN




8086 & 8087

	

TCP

	

Storage Locker service

	

IN




If you are using Windows Firewall, the VMS installer can automatically create exceptions for the required ports.

Automatic port forwarding can configure the ports to be different than these default ones.

Bandwidth Requirements

The bandwidth requirements for the network between the servers and client programs depend on a number of factors. 

Here are a few aspects to think about:

Data transmission from the servers to the client computers (uplink) requires more bandwidth than data transmission from the client computers to the server (downlink). 

The connection does not have to be symmetric.

Real-time monitoring requires more bandwidth than transmitting recorded video or audio.

In addition, signaling and protocols increase the required bandwidth. 

Data Security

The system uses a data protection mechanism and user authentication.
However, using public networks always includes a security risk because there are no completely secure systems available on the Internet.
For this reason, dedicated networks should be used whenever possible to prevent unauthorized access to the system.
Consider using a Virtual Private Network (VPN) to create a secure connection between computers on a public network.
Antivirus programs should also be used if the system units are on a public network (intranet).

Windows updates

Please check from time to time that your system has the latest Windows updates installed and .NET Framework is up to date.

Pagination
Previous page
About the System
Next page
Server Installation