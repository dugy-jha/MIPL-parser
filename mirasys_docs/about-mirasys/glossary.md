# Glossary | Mirasys Help Center

Source: https://documentation.mirasys.com/about-mirasys/about/glossary

Glossary




.
	







.dhc

	

The file format used to export and import information and settings for a remote user connection in the VMS



A
	







Alarm

	

Alarms in our VMS are configured in the system manager and can be assigned to user profiles. Alarms have a trigger, action and calendar that can be activated based on the hour.




Analogue camera

	

A CCTV camera that provides the video stream analogue. Typically via COAX cable.




API

	

The application programming interface is a set of programming routines, protocols, and tools for building software applications




Applet

	

A small, single-task application that does not require installation in any system using it




Archive

	

This functionality can be triggered manually in the Spotter application or scheduled in the system configuration. It is the fastest way to get data out of the system. The granularity is only in a full hour.




Archive SDK

	

This SDK allows to open and process of Mirasys archives and requires a signed NDA to be used.




ARP

	

Address Resolution Protocol, a link layer protocol used to resolve network layer addresses of connected devices into link-layer addresses




Artefact

	

An aberration appears in an image as a result of the image being compressed with a lossy codec




AVM

	

Agile Virtual Matrix, a Spotter for Windows plugin where numerous security camera feeds are displayed in an array on a wall with multiple screens



B
	







b/s

	

Bits per Second, a measure of bandwidth. Usually prefixed with k (Kilo, x103), M (Mega, x106), G (Giga, x109), etc. for brevity




B-Frame

	

Bi-directional predictive inter-frame, a frame referencing preceding and successive I-frame and P-frame (or two P-frames) to remove unchanged regions from the image




Broadcast

	

Network-wide transmission of an audio or video stream



C
	







Camera

	

IP camera with its address and user interface for configuration.




Capture Card

	

A hardware card used on recording servers set up as digital recorders (DVRs) to convert analogue signals into digital information




CIF

	

Common Intermediate Format, a video resolution format for analog cameras. 352x240 (NTSC) or 352x288px (PAL) resolution at 30000/1001 FPS frame rate




CLI

	

Command Line Interface, a method of interacting with a computer system through a text representation (example: MS-DOS)




Closed network

	

An information network of computers or other digital devices not connected to an internetwork, e.g. the Internet




Codec

	

Format of video compression done by a device or software that enables compression or decompression of digital video




Codec compression format

	

We use this term for video formats like H.264/265, JPEG/MJPEG, and MxPEG.




Configuration

	

All adjustments to the system behaviour on the server-side or via the System Manager.



D
	







Decoder

	

Converter from analogue camera stream to digital. These devices have their IP address.




Digital noise

	

random fluctuations and deviations in a digital signal




DNS

	

Domain Name System, a method of converting IP addresses to hostnames




Domain

	

A shared network of computers and the user accounts for them in a corporate environment




DoS

	

Denial-of-Service is a digital attack aimed at flooding a network or networked device with connection requests, drowning out legitimate requests or overloading a connected device’s capabilities




Driver

	

A software component used to interact with hardware devices

We use the term "Driver" exclusive for connectors to cameras.




DVRServer

	

VMS recording server service



E
	







Easy LPR

	

Mirasys Easy LPR is a camera-based license plate recognition extension for Mirasys Spotter.




Encoder

	

Converts digital video to analogue (video) signals. Old term. Not used in pure digital processing.

This term is often also confusingly used instead of Decoder as a device that allows converting multiple analogue cameras to one IP address.




EoL

	

End of Life of a product version




Ethernet

	

A physical network connection standard, most commonly known as “LAN cable”




Event

	

We call an event any data, input or situation in our VMS which we can transform into an alarm. There are undoubtedly many events in our software that are not used for triggering alarms.




Export

	

This functionality of the Spotter application provides the possibility to save video and audio data into files for any period.



F
	







Failover

	

Failover servers are VMS Servers on a passive standby until the system recognizes that one of the active video recording VMS Servers has broken down; at this point, a failover server takes the place of the broken server.

This function grants an automatic switch from a production server to a spare (=failover) server.

The switch will start when the slave server is unavailable for a configured period.

By default, this threshold time is 10 minutes to avoid the process from starting on temporary network problems.




Failback

	

In V9.5.0, failback can be done automatically or manually, and there is no need to use settings backup to revert the failover.

Failback uses the same functionality as failover but in reverse order by moving recorder functionality from the failover server back to the failed Recorder.

Manual failback can be triggered from the failover log. Automatic failback will trigger failback when automatic fallback is enabled and connected to the failed Recorder is restored successfully.




Firewall

	

The network security measure, screening incoming and outgoing network traffic and blocking unauthorized or harmful packets




FPS

	

Frames Per Second, a measure of image refresh rate



G
	







Gain

	

The relationship between the number of electrons acquired on an image sensor and the analogue-to-digital units that are generated represents the image signal




Gateway

	

Gateway is an optional service that can be installed to grant users access via web browser, mobile applications or Gateway SDK integrations.

An edge device between two networks, providing routing information for data traffic between the networks




Gateway SDK

	

This is one of the integration possibilities to access all data inside the VMS. Documentation of the Gateway SDK requires a signed NDA.

The VMS license needs to contain a license connector to enable a specific Gateway SDK integration.




GPS

	

Global Positioning System, a network of satellites sending data to receivers, lets the device calculate its position on the globe. Can also be used for time syncing.




GPU

	

Graphics Processing Unit, a processor chip specialized in calculating, generating and outputting images from data.
Can be harnessed for other complex computational tasks, such as distributed computing.




GUI

	

Graphical User Interface, a method of interacting with a computer system through a graphical representation (example: Windows)



H
	







H.264

H.265

	

A video compression format. Also known as MPEG-4 Part 10. Advanced Video Coding.

A video compression format. Also, known as MPEG-H Part 2 or High-Efficiency Video Coding(HEVC), Designed to be a successor to H.264

Most commonly used video codec format to compress video data.

H.264 is also MPEG-4 Part 10 or Advanced Video Coding (MPEG-4 AVC).

H.265 is also High-Efficiency Video Coding (HEVC) and MPEG-H Part 2.




High Availability

	

This technology is used for master servers to grant an automatic switch within milliseconds from the production master server to a master server in standby mode.

This function is typically provided by Hyper-V or VMware systems. 




High-Dynamic-Range Imaging

	

Multiple-exposure imaging method aimed at creating a recorded image with similar luminosity levels as those seen by the human eye




Hop

	

The action of data packets crossing between network interfaces




Hostname

	

Plain name of a digital device in a network




HTTP

	

Hypertext Transfer Protocol, an application layer Internet protocol used for sending requests from a web client (e.g. a web browser) to a web server, returning web content (web pages) from the server back to the client




HTTPS

	

Hypertext Transfer Protocol over TLS, an application layer Internet protocol used for sending requests from a web client (e.g. a web browser) to a web server, returning web content (web pages) from the server back to the client over TLS-secured communications



I
	







ICT

	

Information and Communications Technology, the term for fields relating to telecommunications and information networking




I-Frame

	

Intra-frame, a full image frame in a video stream




IGMP

	

Internet Group Management Protocol, a communications protocol used by hosts and network devices on IP networks to establish multicast group memberships




Incident Reporting

	

Incident Reporting is a service that takes care of creating daily reports and incident reports, which can contain video clips or images as evidence.




IP

	

Internet Protocol, an OSI Layer 3 networking protocol




IP Encoder

	

A hardware device that converts analogue signals into IP packets and sends them to an IP network. Can also be referred to as a video server.




IPSec

	

Internet Protocol Security Architecture, security suite used to secure packets between routers, forming VPN tunnels over IP networks




ISP

	

Internet Service Provider




IT

	

Information Technology, a catch-all term for fields relating to computers and other digital devices



J
	







Java

	

A programming language often used on websites for scripts and applets




JRE

	

Java Runtime Environment (JRE), part of the Java Development Kit, a set of programming tools for developing Java applications



L
	







LAN

	

Local Area Network, a small, usually home or office-level networked area




Layer 2

	

2nd layer (Data Link) of the OSI model, transfers data between adjacent network nodes in a WAN or between nodes on the same local area network segment




Layer 3

	

3rd layer (Network) of the OSI model, used for packet forwarding, including routing through intermediate routers




License

	

Every VMS server (master or slave) has its license, which provides features to this one server. Example: Amount of channels, integration connectors, special plugins etc.




Load

	

Network traffic through or on network components, such as connections or devices



M
	







MAC address

	

Media Access Control address, a physical-layer identifier composed of six pairs of hexadecimal characters for network interfaces of digital devices.

The first three pairs identify the device/interface manufacturer.




Managed switch

	

A Layer 2 networking device that can be configured through a workstation or web browser connection to manage connections on the device or information traffic going through it




Master

	

VMS server device with the Mirasys SMServer service installed on it




Master failover

	

Securing the availability of the master server is essentially different from a slave server failover.

We provide this functionality via an operating system like MS Hyper-V (cluster) or VMware to avoid downtime. See also high availability.




Master server

	

Central server with typically no recording functionality. This server manages alarms, user access, profiles and system configuration.




Media Exporter SDK

	

This SDK allows data export from a VMS via command line and requires a signed NDA to be used.




Megapixel

	

A million pixels. Shorthand statistic for camera resolution or image fidelity.




Metadata

	

We separate into two groups.

Event metadata describes attributes of an object/scene/event in the context of a preconfigured rule on the metadata source/device. Face detection, ANPR and tripwire are specific events.

Continuous object attributes like bounding box coordinates, speed, and size... on every frame of video footage. These metadata are described in text from the activity of objects in video footage.




Mirasys TruCast

	

With the Mirasys TruCast, the user can define where the IP camera stream is sent to the Mirasys Spotter(from the VMS server or the IP camera) and the situation when Mirasys TruCast will be used.




Mirasys TruStream

	

With the Mirasys TruStream, the Mirasys Spotter changes the shown IP camera resolution, depending on the used camera grid resolution. Multistreaming must be enabled.




MJPEG

	

Motion-JPEG (Joint Photographic Experts Group), a video compression format




Multicast

	

Transmission of an audio or video stream from one computer to others selected to be the targets

In computer networking, multicast is group communication where data transmission is simultaneously addressed to a group of destination computers. 

Multicast can be one-to-many or many-to-many distribution. 

Multicast should not be confused with physical layer point-to-multipoint communication.

Multicast requires a layer two network switch configuration with multicast support.




Multi-channel device

	

A device that can send multiple signal channels, each carrying a certain number of video streams




Multistreaming

	

Method for a digital device to send multiple video streams with each having a different end target

Other than multicast, multi-streaming provides multiple individual streams from a device or server to the client or server.



N
	







NAT

	

Network Address Translation, translation of an internal network’s IP addresses to outside IP addresses




Network

	

Logical structure existing between a collection of interconnected digital devices

All active and passive network components enable the application to communicate. See also the OSI 7-Layer model.




NIC

	

Network Interface Controller, a computer device’s LAN adapter card




NTP

	

Network Time Protocol, a communication protocol used to sync a networked devices time with a time server




NTSC

	

National Television System Committee, an analogue video standard specified for video surveillance at 525 lines per frame with a 59.94Hz refresh rate. Used in the Americas.




NVR

	

Network Video Recorder, networked digital device that records video feeds over an IP connection.



O
	







OS

	

Operating System




OSI model

	

Open Systems Interconnection model, an abstract layered representation of a communication system



P
	







PAL

	

Phase Altering Line, an analogue video standard specified for video surveillance at 625 lines per frame and a 50Hz refresh rate. Used in Europe, Asia and Australia




P-Frame

	

Predictive inter-frame, a frame referencing a preceding I-frame to remove unchanged regions from the image




Person search

	

The person search is the Mirasys Spotter plugin, which uses Person/Vehicle/Bike detector SSD detection architecture, RMNet backbone, and learnable image downscale block.

The model is intended for security surveillance applications and works in various scenes and weather/lighting conditions.




PIM

	

Protocol Independent Multicast, a family of multicast routing protocols for IP networks that provide one-to-many and many-to-many distribution of data over a TCP/IP network




Plugin

	

A spotter is expandable with plugins and can also be used to control the Mirasys Agile Virtual Matrix (AVM) video-matrix option.

Built-in plugins are currently (enabled functionality and available plugins depend on product version and licensed features)




PoE

	

Power over Ethernet, a method of powering devices through their Ethernet connection to a computer or networking device




Port

	

Software construct serving as a network communications endpoint for a computer or other digital device




Port forwarding

	

Application of NAT that redirects communications from one address and port number combination to another while the packets are traversing a network gateway




Programming

	

This is the term for developing the software code. Not to confuse with the configuration of the system.




Proxy integration

	

All integrations require an additional installation on the VMS server to communicate with a 3rd party system or device.

Typically the messages are received in a UDD text channel from the proxy service.




PTZ

	

“Pan, Tilt, Zoom,” two-axis remote-controlled camera



Q
	







Quantization

	

A lossy compression technique is achieved by compressing a range of values to a single quantum value



R
	







RAID

	

Redundant Array Of Independent Disks, a method of saving data across multiple disks. RAID levels are used to categorize readiness of data integrity and redundancy




Router

	

Active network component to control, filter and direct network traffic. Typically Layer-2 or 3.




RTP

	

Real-time Transport Protocol, a networking protocol used for delivering audio and video over IP networks




RTSP

	

Real-Time Streaming Protocol, a connectionless networking protocol used to control video streaming between a viewing client and a video source




RTSP Server

	

RTSP/RTSPS server is used to stream video and metadata from Recorder to any third-party client that supports RTSP/RTSPS protocol.




RTSPS

	

Real-Time Streaming Protocol over TLS, a secure networking protocol used to control video streaming between a viewing client and a video source



S
	







SDP

	

Session Description Protocol, a format for describing streaming media initialization parameters




Service

	

A software service of our software running on a Windows PC.




SMA

	

Service and Maintenance Agreement. For detailed content, ask your sales representative.




SMS

	

Short Message Service, a telephone text messaging system




SMServer

	

System Manager Server, VMS master controller service

The service name of the master server.

This service is installed on every system but is only required on the master server for system configuration, alarm handling or user/profile management.




SMTP

	

Simple Mail Transfer Protocol, standard transfer protocol for e-mail transmissions




SNTP

	

Simple Network Time Protocol is a communication protocol used to sync a networked devices time with a time server. A simplified version of NTP with only a millisecond in accuracy loss




Spotter

	

A spotter is the leading Windows application to access the system as a user. Find more details in the Spotter User Guide for your version.




Spotter Web

	

Spotter Web is a new HTML5 client in which communication is automatically encrypted using IIS certificates.




SQL

	

Structured Query Language, a programming language for managing data held in a database




Static IP Address

	

An unchanging IP address for a digital device in a network




Storage Locker

	

Storage Locker is Mirasys VMS service which takes care of video clips, images, and incident reports in a centralized location.




Storyboard

	

This functionality of the Spotter application allows exporting of data with comments provided in a storytelling format. 




Stream

	

Continuous audio or video transmission over a network

A stream is the data send by a device or system to a receiver. We typically use this term for video streams.




Stream profile

	

Most cameras allow configuring the camera a stream profile to manage different stream properties easily.




Subnet

	

A network segment sharing a range of IP addresses. Subnet size is represented with a prefix signifying the number of bits (most significant first) reserved for a subnet.
The IPv4 prefix is 8-32 bits, IPv6 is 4-128 bits.




System Manager

	

System Manager is the Windows application to configure the installation.

This application is installed on every VMS server by default.

In multi-server installations, the system administrators should use only the System Manager of the Master server to configure elements.



T
	







TCP

	

Transmission Control Protocol, networking protocol




Text channel

	

Receiving points for text messages in the VMS.




ThruCast

	

Mirasys proprietary multistreaming method, where traffic from an IP camera can be directed to a Spotter client directly, instead of going through a recording VMS server




TLS

	

Transport Layer Security, formerly known as SSL (Secure Sockets Layer), is a cryptographic protocol that provides secure communication over an IP network




Tunnel

	

A channel that allows untouched packets of one network to be transported over another network



U
	







UDD

	

The Universal Data Driver is an extension for the text channel to receive, interpret and filter incoming text messages to use specific data to trigger events and alarms.

The text channel is configured via an XMP configuration file. For more details, see the UDD guide.




UDP

	

User Datagram Protocol, a connectionless networking protocol




Unicast

	

Transmission of an audio or video stream from one computer to another




Unmanaged switch

	

A Layer 2 networking device that can be used out-of-the-box and all connections can be considered plug-and-play. Devices like these cannot be accessed or configured remotely.




Update

	

This term describes going from lower to higher minor software versions. Example: v9.2 -> v9.3




Upgrade

	

We use this term to describe going from lower to higher major software versions. Example: v8.x -> v9.x




UPnP

	

Universal Plug and Play, is a set of networking protocols that permits networked devices to discover each other's presence on the network and establish functional network services




UPS

	

Uninterruptible Power Supply, a reserve power source in the event of electrical failure in a device’s power cord or building power network




URL

	

Uniform Resource Locator, a reference to a resource that specifies its location network and a mechanism for retrieving it



V
	







VCA

	

Video Content Analytics, the capability of automatically analyzing video to detect and determine temporal and spatial events

Video Content Analysis is the AI model-based image processing to describe video footage in text form.

Example: bounding box of a moving object, speed, size, classification, colour, direction, etc.




WDServer

	

The service name of the WatchDog service. This service is installed on every system to monitor and restart the other services and report hardware problems.




VLAN

	

Virtual Local Access Network, a logical method of partitioning a layer-2 network by assigning Ethernet ports to virtual networks




VMD

	

Video Motion Detection, method of detecting motion in a video stream by comparing frames with each other; changes are logged as motion




VMS

	

Video Management System, networked system connecting cameras, recording servers and viewing clients

Video Management System. This describes all software components required for a complete system functionality to configure, administer, process, view, record, stream and store data from devices.




VPN

	

Virtual Private Network, secure communication line between end devices over a larger network




WAN

	

Wide Area Network, geographically large networked region




WDR

	

Wide Dynamic Range, multiple-exposure imaging method aimed at increasing image details and eliminating dark areas




WinPcap

	

Windows port of the Pcap packet capture driver




WireShark

	

A network monitoring application




WLAN

	

Wireless LAN, wireless local networking. Also known as Wi-Fi.




XMC

	

XMC is a database module for VMS servers. It can store data on alarms and events into a Microsoft SQL database.

Pagination
Previous page
Mirasys VMS System components