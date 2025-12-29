# Main Server | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/master-server

Main Server

In a networked system, one of the servers must be set as the Main Server.

A Main Server is the central server of a surveillance system. All other VMS Servers connect to it, and all client applications communicate through the Main Server.

If the system contains only one server, then that server is the Main Server. If there is more than one server, the Main Server can be set freely.

In a more extensive system we recommended that the Main Server is a server dedicated for this purpose alone

Main Servers must have SQL Server Express 2014 or other Microsoft SQL Server 2014 installed.

The Main Server functionality is the following:

It verifies the identity of all programs and users who try to log on to the system (authentication).

It stores all system configuration data.

It stores all user data.

It monitors the system.

It synchronizes the clocks on all servers.

It generates reports.

It stores watchdog events.

It stores alarms.

It stores audit trails.

Pagination
Previous page
VMS Servers
Next page
Client Programs