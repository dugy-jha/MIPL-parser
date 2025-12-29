# Mirasys VMS V9.3 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-3-release-notes

Mirasys VMS V9.3 release notes
What’s new?
WatchDog: Allow hardware monitoring




Export MAC, serial number and HWGUID into one file
Include alarm triggers into alarm display
Incident Reporting plugin (optional)

An Incident report plugin is a tool for a formal recording of the facts related to an incident.
You can freely customize Incident Reporting to fit your environment needs. 

Storage Locker plugin (optional)

Storage Locker is a centralized container for the

Images

Video clips

Camera audit reports

RTSP stream for cameras configured as VCA

Cameras configures in VCA settings can now be enabled to provide an RTSP stream including VCA annotation and image overlays.
This stream can be configured as an additional camera with an RTSP driver to have both, clear stream and annotated stream recorded or available via Spotter or Gateway SDK.

The configurable database connection string

The databases DvmsData, WdContext, DvmReportContext, IncidentReporting, StorageLocker and RecorderDB can now be configured with individual connection strings.
This enables outsourcing the database to any external MS SQL server.

Other minor changes

Optimize settings for restore and failover

Encrypted Gateway SDK communication

HTTPS support in Spotter Public HTTP API

LDAPS support

​​Export to MP4 format

Optimize file system

Changelog V9.3 - 2021/5/7

Additional user role for archive viewing

UI improvement for setting change in System Manager

License improvement for VCA settings

Database index for metadata event time

Fix: End User License Agreement read-only mode

Fix: Gateway users logout

Fix: Postponed failover

Fix: Joystick PTZ enable button for already open PTZ cameras

Fix: Privacy user role settings tab level set/clear all buttons

Fix: "Camera highlight" with multiple Audio channels

Fix: 1x1 default grid

Fix: Export dialogue in spotter settings

Fix: Saving new tab content speed increase

Fix: Axis joystick driver loading in Spotter log

Fix: Spotter automatic lock when the System management server is unreachable

Fix: Corrected motion mask tool size

Fix: Camera highlight in profile map with PTZ control

Fix: Ribbon menu position

Fix: Export Image popup

Fix: UI for Automatic lock

Fix: Failover recorder improvement after the failed recorder

Fix: Closing PTZ control when playback is started

Fix: Export Image message

Fix: Commands included when importing maps from one profile to another

Fix: Spotter exit

Fix: Closing VCA settings

Fix: ArchiveSDK exporting improvements

Fix: IO device details loading

Fix: AVI and MKV support for H.265 export

Fix: Version information in logs

Fix: Copy player option with storage locker

Fix: Export log and SMS log data

Fix: Alarm retention time setting

Fix: “disable Alarms” action handling

Fix: Add to Storyboard only when licensed

Fix: 64 streams limit for storyboard

Fix: Reduced metadata saved to the database

Fix: Spotter default export settings​

Other and cosmetic changes

Pagination
Previous page
Mirasys VMS V9.4 release notes
Next page
Mirasys VMS V9.2 release notes