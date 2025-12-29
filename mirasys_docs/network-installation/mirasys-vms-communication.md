# Mirasys VMS communication | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/mirasys-vms-communication

Mirasys VMS communication

Mirasys VMS system components can be divided into applications and servers.
Applications are used to open communication with and between the system’s servers, and to send connection requests to servers.
Meanwhile, servers accept connection requests from applications or from other servers.
Communication between the system components is implemented with TCP/IP protocol through TCP ports 5008-5011.

Signaling And Streaming Protocols

UDP (User Datagram Protocol) is a transport-layer protocol used to stream the video feeds from the connected cameras.
The protocol is connectionless and lightweight, so it is often used to discover connectivity issues in a network. In the VMS, any connection difficulty is immediately noticed as a loss in the video feed.
For streaming to function properly, the network for the system needs to be well constructed and the connections need to be reliable.

UDP

UDP (User Datagram Protocol) is a transport-layer protocol used to stream the video feeds from the connected cameras.
The protocol is connectionless and lightweight, so it is often used to discover connectivity issues in a network. In the VMS, any connection difficulty is immediately noticed as a loss in the video feed.
For streaming to function properly, the network for the system needs to be well constructed and the connections need to be reliable.

RTSP

RTSP (Real-Time Streaming Protocol) is used to control video streams over a network. RTSP communications between a client and a recording VMS server send instructions on playback and play speed.
As with UDP, RTSP is a stateless communication protocol that requires a solid network to function reliably.
Usually, the interaction between VMS and camera goes in the following order:

VMS sends DESCRIBE request to camera

Camera answers with DESCRIBE response contain information about supported video/audio streams in SDP (Session Description Protocol) format

VMS sends SETUP request to camera

Camera answers with SETUP response needed to create a new RTSP session for a specific stream

VMS sends PLAY request to camera
Camera answer with PLAY response after this camera starts video/audio sending to VMS – usually, RTP (Real-Time Protocol) over UDP protocol is used for data sending

Periodically VMS sends KEEPALIVE request – if no camera stops video stream sending

VMS sends TEARDOWN request when video should be stopped

RTSPS

RTSP (Real-Time Streaming Protocol over TLS) is a secure version of RTSP, similar to how HTTPS is a secure version of HTTP.
The protocol uses TLS (Transport Layer Security) to secure communications, requiring a stable connection for TCP traffic.

TCP

TCP (Transfer Control Protocol) is used for signalling between the devices and components of the VMS network and the Internet at large.TCP is an ordered, error-checked and reliable signalling protocol that can function even if there are some minor faults in the network, at the cost of latency.

HTTP

HTTP (Hypertext Transfer Protocol) is used to communicate control signals for IP cameras in the system.
Many drivers use HTTP/HTTPS for setting and retrieving parameters to/from the cameras. In a direct connection, a user contacts the camera GUI with HTTP/HTTPS.
Some drivers may also use HTTP to receive motion detection data and video streams. Some camera drivers traffic PTZ signalling through HTTP.

HTTPS

HTTPS (Hypertext Transfer Protocol over TLS) is a secure version of HTTP.The protocol uses TLS to secure communications.

Mirasys VMS Ports

In all VMS installations, the following TCP ports must be open on all servers for the applications and servers to function correctly:

Port 53
The default port for DNS service (Required by Mirasys VMS 8.5 and newer versions)

Port 5008
For signalling between SMServer and client applications, and inbound communications from clients to the SMServer
Port rule: open inbound

Port 5009
For remote connecting between DVRServer and client applications, and signalling between SMServer and DVRServer for time synchronization, settings changes, event information, etc.
Port rule: open inbound

Port 5010
For Watchdog monitoring communication between WDServer, client applications and DVRServer
Port rule: open inbound

Port 5011
For streaming between the Streaming Service and client applications
Port rule: open inbound

Optional ports:

IP cameras and auxiliary devices may need specific ports opened. Please refer to device-specific documentation for instructions.

WebClient, Spotter Mobile and GatewayServer specific ports

Ports 9000 and 9999
Between WebClient/Spotter Mobile and GatewayServer.
Port rule: open inbound

AVM specific ports

Port 8084
Between SMServer and the Spotter for Windows client
Port rule: open inbound

IP Camera Ports

Cameras use their own ports to keep contact with the VMS and transmit data to the recording servers.
Please refer to device-specific documentation for instructions.
If there are firewalls between the cameras and recording VMS servers running DVRServer, the relevant ports need to be open through the firewall.

HTTP

Port 80
The default port for HTTP traffic used to communicate with a camera’s system

Port 8080
Used by some cameras for PTZ control communications

HTTPS

Port 443
The default port for HTTPS traffic used to securely communicate with a camera’s system

RTSP

Port 554
The default port used on the VMS to traffic stream control signals

Port 7070
Default stream control port for some camera drivers

UDP

Port 53
The default port for DNS service (Required by Mirasys VMS 8.5 and newer versions)

Ports 3556-4556
Used on the VMS to receive feeds from the cameras. Each video stream occupies two sequential ports in the port range. To verify device port use, reading of device manufacturer driver read me files is highly recommended.

Pagination
Previous page
General Network Requirements
Next page
Using Mirasys VMS With Different Networking Components