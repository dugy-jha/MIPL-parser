# Mirasys VMS V9.9.3 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/mirasys-vms-v9-9-3-release-notes

Mirasys VMS V9.9.3 release notes
Release date: 2025-06-18
Fixes
System

Communication configuration values are updated on servers and clients, and the values used are logged in the client logs.

Client applications do not create a large number of threads for NATS communication.

Memory usage in clients and servers was optimized by removing duplicate data from the data structures.

The setting restoration works as intended if the services and client run on a PC other than the main server.

Installers use the folder defined at the last installation time on upgrade by default.

Configuring NATS to use a port other than the default 4222 port is possible using the nats-server.conf config file.

The administrator can forcefully log out the Spotter user in System Manager when Spotter is configured to log in automatically.

The VMS installer stops on error if the NATS keys cannot be created.

The XMC license feature is removed from the license and enabled by default, allowing the SMServer to create database connections without a license.

Broken or failover recorders do not send events to clients.

System Management Service

Terminated alarm search logging was moved to the debug level.

The Watchdog event database operations are more resilient to database connection errors.

The thread allocation for alarm search is optimized.

Failover works as intended when there is more than one failover server.

The VMS server failover settings change doesn’t cause a settings update on clients.

When the VMS server is set to failover server, all devices are cleaned up and removed from the profile.

VMS Service

The VMS service works as intended when the ONVIF profile M trigger with empty parameters is received.

Active alarms are ended when the VMS service settings are changed.

VMS service file storage index saving works as intended.

The VMS service registration and unregistration work as intended.

The VMS server restart works as intended on a settings change.

The VMS server recovers from the live streaming errors as intended.

System Manager

If a log file cannot be exported, the correct error message is written to the log, and the export process continues for other log files.

The Moxa PTZ settings work correctly in the System Manager.

The RTSP streaming server license is checked from the VMS server license.

The System Manager application shows the correct icon in the Windows taskbar.

Removing a multi-channel device works as intended when another device is added inside its channel range.

The camera settings export and import work as intended when ‘;' and ',’ characters are used in the name and other text fields.

Deleting old data and writing new data to the database works as intended when the database is full.

Text for the "Highest filtered alarm priority" in the alarm settings is fully visible.

Selecting the VCA trigger zone without available events in the alarm settings works as intended.

System Manager automatically reconnects to get the events if the keep-alive event is not received.

When creating a settings backup, the saving dialog works as intended.

VMS service diagnostics in the System Manager show the version of the I/O drivers.

The motion mask settings are displayed correctly in the camera settings.

Exporting the cameras to CSV from the file menu works as intended when the camera description contains new line characters.

The user can define an end zone for the metadata trigger in the alarm settings if the metadata trigger has several zones that are not used for other alarms.

Selecting and deselecting all Spotter roles works as intended.

The VMS server search works as intended.

ONVIF topics in the alarm trigger settings are fully visible, and the dialog can be resized.

Spotter

Settings loading in the Spotter startup are optimized to work faster.

Spotter functions as intended when a user attempts to save settings and loses connection to the main server.

Camera view closing works as intended in the Zoom plugin.

VLC player plugin streaming is stopped when the tab is hidden and restarted when the tab is shown.

The VLC player works as intended when the Spotter settings are changed.

The VLC Player plugin components have been updated to the latest versions.

Profile tree icon loading works as intended.

Spotter UI resource loading works as intended.

Plugin instance limit works as intended, and the user can open up to a limited number of plugin instances.

Alarm search thread usage was optimized.

Profile loading works as intended when the connection to the main server is lost.

Showing alarms in the timeline is set off by default and can be enabled from the timeline context menu.

Exiting from the Spotter works as intended.

Spotter works as intended when the mouse cursor is moved over the Spotter timeline.

Loading UI resources works as intended.

Image export to the default location also works after the “Don’t show this dialog again” option has been selected.

The frame rate is displayed correctly in the camera tooltip info.

The audit trail event is saved as intended when Spotter is locked and exits due to a loss of the main server connection or a forced log out.

The .html file is included in the ASF exports.

A defined storyboard draft directory is used when a draft file is saved and loaded.

The event queue size is increased to 1024.

Spotter works as intended when the alarm object has invalid (null) properties.

Filtering alarms in the timeline works as intended.

The profile tree response time is optimized.

Spotter Web

Spotter Web backend manages the user session as intended.

Driver fixes
BoshIPCapture v1.7.9.0

The additional streams for the Bosch NDV-5704-AL camera are detected with valid capabilities. There is no frame sending error in the VMS log.

WisenetIPCapture v1.2.19.0

The Wisenet driver uses the same session key for all RTSP connections for NVRs.

The PTZ move is working as intended.

Edge storage is working as intended.

MoxaPTZ v1.7.4.0

The DVRServer initialization works as intended if there is no connection to the Moxa device.

Disconnection to the Moxa device doesn't affect the DVRService operation.

The Moxa input states are not changed during the VMS server initialization.

The Moxa input state is in an unknown state until the state is received from the device.

AxisIPCapture v2.9.9.0

The driver settings XML file was updated to use the default camera-side dewarping, and information was added for possible dewarping options.

Known issues

When a VMS server is changed to a failover server, alarm configurations are not cleared from the target server's system data. It is recommended to use a clean VMS target server setup or to remove all devices and alarms from the target VMS server configuration before changing it to a target failover server.

When using the VCA counter rule with the occupancy section, the alarm is not triggered.




You can download the release notes as a PDF file here Mirasys VMS V9.9.3 Release Notes.pdf.

Pagination
Previous page
Mirasys VMS V9.9.4 release notes
Next page
Mirasys VMS V9.9.2 release notes