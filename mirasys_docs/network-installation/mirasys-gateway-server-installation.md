# Mirasys Gateway Server Installation | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/mirasys-gateway-server-installation

Mirasys Gateway Server Installation

Mirasys WebClient is a browser-based application that is used for viewing video from Mirasys servers over a network.

Mirasys WebClient uses the user profiles, user names, and passwords as Mirasys System Manager and Spotter client programs.

To use Mirasys WebClient, the Mirasys Gateway server must be first installed on a computer running an HTTP (web) server.

Mirasys VMS recording software is not required on the server. The Gateway server needs to be able to connect to the Mirasys VMS Master Server.

Minimum System Requirements
Client

Internet Explorer 6 or Mozilla Firefox 2.0 or newer

Java Runtime Environment (latest version recommended for security reasons)

Server

Windows 7 Enterprise, or Windows 2008/2012 Server

HTTP server software (IIS)

Intel i3 processor, or better

4 GB of RAM

Please note that the minimum system requirements are recommended for mostly live viewing.If multiple users access the same WebClient server simultaneously, mainly for search and playback functions, a more powerful processor is required.

System Restrictions

The Mirasys VMS Gateway server can be installed on any Microsoft Windows server that meets the system requirements.
Mirasys VMS software is not required on the server.
The Gateway server has a default license controlled limitation of 32 simultaneous streams for all WebClient connections.

Installing The Mirasys Gateway Server

To install the Mirasys Gateway server:

Double-click the Release_9XX_Gateway_x64.exe installation package to start the installation.

After the VMS Gateway Setup screen has loaded, select the destination folder and click Next.

Type the SMServer IP address (the IP address of the Master Server) into the SMServer IP field.

Click Next

When the software has been installed, click Finish.

Verifying The Installation

To verify that the server has been correctly installed:

Open a compatible web browser and type the following address:

HTTP://[WEBCLIENT SERVER URL]:[PORT]/


For example, if the WebClient server is on the same computer: http://localhost:9999/

If the server is correctly installed, the login screen is displayed.

Type a user name and password in the corresponding boxes and click Log On.

The user name and password are set in the Mirasys System Manager program.

Streaming Options

The users can view the WebClient streams in JPEG format (default) or in the native format in which they are received by the servers.

This does not require any action on the server-side: the users can decide to view the streams in native format by adding ?video=native to the end of the WebClient URL.

For example, if the WebClient server is on the same computer: 

http://localhost:9999?video=native

Pagination
Previous page
Installing Spotter Plugins
Next page
Update & Upgrade