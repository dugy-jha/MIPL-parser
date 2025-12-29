# Mirasys VMS Applications | Mirasys Help Center

Source: https://documentation.mirasys.com/about-mirasys/about/mirasys-vms-applications

Mirasys VMS Applications
VAU

VAU (VMS Application Updater) is a service application without its own user interface.
It is used to automatically update user applications to the latest versions from the Master SMServer.
VAU is installed during the application installation, and the application is started automatically when the System Manager is run.
VAU uses the Master’s IP Address or hostname to contact the SMServer (TCP port 5008).
After VAU has established a connection to the SMServer, it downloads the latest version information.
If the version information differs from the information detected during the previous application start-up, VAU downloads all needed update files.
If the downloaded version information matches the local version information, only the configuration files will be downloaded.
The configuration information includes, but is not limited to, the SMServer address which the Spotter for Windows or System Manager will contact at start-up.
After updating the version or downloading the configuration files, Spotter or System Manager will be started and VAU will close.

System Manager

When the System Manager or Spotter for Windows application is started, the user’s username and password are used to download the corresponding user profile from the SMServer (TCP port 5008).
The profile data includes all information regarding the servers connected to the system and available for the user profile.
The applications access the servers through TCP port 5009. Video, audio and data streams requested through the applications use TCP port 5011.
The System Manager is the primary system management and configuration application.
It contacts SMServer and accesses information pertaining to the system.
The application allows a user to add, modify and remove servers, cameras and other devices to the service, manage alarm conditions and actions, etc.

Spotter For Windows

Spotter for Windows is the primary desktop monitoring application.
A Spotter client contacts the SMServer and accesses the devices connected to it running DVRServer.
Through this, it accesses live and recorded surveillance data. A spotter can be used as a specialized video wall application, as well.
Currently, only one instance of the SMServer service at a time can be accessed by the Spotter for Windows application.
More information on the System Manager can be found in the Mirasys VMS 7.3 - Spotter User Guide documentation.

WebClient & Spotter Mobile

The WebClient applet can be used on any web browser from any computer on the Internet, but Java needs to be enabled.
If the GatewayServer server application is installed with the default values, TCP ports 9999 and 9000 must be open between the WebClient browser computer and the GatewayServer server computer.
The default ports can be changed during the GatewayServer installation or at a later point by editing the ServiceLauncher.exe.config configuration file in the service’s installation folder (default C:\Program Files\DVMS\Gateway).

Pagination
Previous page
Drivers EOL and EOS
Next page
Mirasys System Services