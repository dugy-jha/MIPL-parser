# About the System | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/about-the-system

About the System
What is Mirasys Software

Mirasys software is a distributed, digital video management system (VMS or DVMS) for video and audio surveillance applications.
The software can be used for monitoring real-time and recorded video, audio and text data, and to control PTZ cameras, I/O devices and IP cameras.
The software supports systems consisting of both analogue and/or digital surveillance cameras, supporting the creation of analogue, digital or hybrid (consisting of both analogue and digital) surveillance systems.
A centralized surveillance system domain can consist of a network of up to 150 local or remote VMS Servers.
Mirasys software is sold both separately and as part of Mirasys video management systems consisting of both the software and the VMS Server hardware.
Please contact your Mirasys supplier for information on Mirasys software or hardware.

What Does a System Contain?

The Mirasys system consists of these components:

1-150 VMS Servers

Master Server (dedicated server – recommended -, one of the video recording VMS Servers, or the only server in a single-server, non-networked environment)

VMS Server ("nodes," if the system consists of multiple servers)

Client programs:

Mirasys VMS System Manager

Mirasys VMS Spotter for Windows

Mirasys VMS Spotter Mobile

Mirasys VMS WebClient

VMS Servers

The VMS servers record video and audio from multiple cameras and audio channels and write the data on hard disks.
You can access a VMS Server locally or over a network by using the System Manager and Spotter programs, and monitor server functionality through the Spotter Diagnostics plugin.
A server contains the computer with storage, the Windows operating system, and the VMS software with required drivers.

In addition, you can connect these devices to a VMS Server:

PTZ (dome) cameras and keyboards

External devices, such as sensors, to the digital inputs

External devices, such as doors, lights, and gates, connected to digital outputs

Monitors

Printers

Backup unit (NAS, SAN, or RAID, for example)

Master Server

In a networked system, one of the servers must be set as the Master Server. A Master Server is the central server of a surveillance system.
All other VMS Servers connect to it, and all client applications communicate through the Master Server.
If the system contains only one server, then that server is the Master Server.
If there is more than one server, the Master Server can be set freely. In a larger system, it is recommended that the Master Server is a dedicated server for this purpose alone.

NOTE: Master Servers must have SQL Server Express 2014 or another Microsoft SQL Server 2014 installed.

The Master Server does these things:

It verifies the identity of all programs and users who try to log on to the system (authentication).

It stores all system configuration data.

It stores all user data.

It monitors the system.

It synchronizes the clocks on all servers.

It generates reports.

It stores watchdog events.

It stores alarms.

It stores audit trails.

Client Programs

System administrators use the System Manager program for these tasks:

Configuring the servers.

Adding user accounts and user profiles.

Monitoring the system.

End-users use the Spotter program, for example, for these tasks:

Monitor real-time and recorded video and audio

Control digital I/O switches and PTZ cameras

Export video and audio clips to local media

Receive and handle alarm notifications

Create video matrixes via the optional, separately sold Agile Video Matrix (AVM) software

Control automatic license plate recognition systems via the optional, separately sold ANPR+ software

Starting from Version 8 onwards, the Mirasys VMS software is available only as a 64-bit ("x64") version.
Note that mixed 32-bit and 64-bit systems need more care and expertise for the installation, upgrading and management of the system.
Analog video compression (capture) cards are not supported on the 64-bit Mirasys VMS.

Mirasys 32-bit vs. 64-bit Versions 
Managing an Environment With 64-bit Versions of Mirasys VMS

In a networked, multi-server Mirasys VMS system, the server with the Master Server role can simultaneously connect to and manage both 32-bit and 64-bit VMS Servers (also known as "slaves") on the network:

The 64-bit Master Server supports simultaneously both 32-bit as well as 64-bit VMS Servers.

A Version 8. x based Master Server supports simultaneously Version 8. x, Version 7. x and Version 6. x VMS Servers, but does not support servers based on Version 5. x, or earlier.

Version 8 supports clients to connect to 32bit and 64-bit server versions. It is recommended to reinstall the clients with the version 8 installer to get the latest application updater (VAU).

Server upgrading considerations

When using the System Manager application's "Update servers" -feature to update the VMS Servers in the system, all or the selected VMS Servers you choose to update will update to the version you choose (which installation file you provide).
In a mixed environment with both 32-bit and 64-bit servers, be careful that you know which servers are to be upgraded to which version, 32-bit or 64-bit!
The 64-bit versions will not work at all on, so-called, hybrid servers with internal analogue video capture cards (also known as compression cards or grabber cards).
The system manager shows the 32 bit or 64-bit version information in the "Version" table.
All new IP cameras, encoders (video servers) or other drivers are also available as separate 32-bit and 64-bit versions.
When installing a new driver or updating an existing driver, you must use a 32-bit driver package on a 32-bit server, and a 64-bit driver package on a 64-bit server.
Note also that all servers with the Master Server role, as well as all VMS Servers with Mirasys VCA require Microsoft SQL Server Express 2014 to be installed on the server before installing Mirasys VMS.

Pagination
Previous page
Mirasys VMS Installation Guide
Next page
System Requirements