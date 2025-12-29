# Installing Mirasys Spotter Web | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/installing-mirasys-spotter-web

Installing Mirasys Spotter Web

Spotter Web is working only with Enterprise Master Server

OS limitations

If SpotterWeb is installed on client OS, there can be a maximum of 10 simultaneous connections: https://docs.microsoft.com/en-us/iis/troubleshoot/request-restrictions

For each SpotterWeb login, 3 connections are made: HTTP, SignalR for events and WebSocket for streaming. So for example Windows 10 Professional, only 3 clients can log in at the same time.

There are no similar limitations in server OS, so it is highly recommended to install SpotterWeb to Windows Server OS.

When installing SpotterWeb to client OS, the installer will give a warning about the OS/IIS limitations.

Spotter Web installation

Start the installation by clicking SpotterWeb installation package.

Click Install

Confirm notification about the operating system limitation

Click Next

Use the default installation folder and click Next

Set the master server address(the computer name of the master server PC)

Use default master server port and master server HTTP port

Click Next

Set the SpotterWeb site address(the computer name of the master server PC)

Use default SpotterWeb HTTPS port(443)

Check that Set firewall exceptions are enabled

Click Next

Click Install

Click Finish

Click Close to finalize the installation

Pagination
Previous page
Installing Client Programs
Next page
Installing Spotter Plugins