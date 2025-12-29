# Mirasys VMS V9.8.2.2 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/mirasys-vms-v9-8-2-release-notes

Mirasys VMS V9.8.2.2 release notes
Release date: 21 August 2024
Enhancements

Now, you can hide the Utility Bar for Layouts, Plugins, Bookmarks, and Saved tabs from the left-hand menu under the device tree. Under View, choose Show or Hide the utility bar.

Importing user groups from Active Directory has been optimized, and it is faster to search available groups and specific groups.

When you export .sef2 password-protected material, we have added a warning message to remind you that the password cannot be recovered.

Help text has been added to the System Manager checkbox, which enables the computer to restart if a critical error occurs.

VMS V9.8.2.2 Fixes

When the database is full, metadata deletion works as intended.

VCA settings and alarm triggers are restored with VMS settings restore.

V9.8.2 Fixes
Spotter

Smart List Management plugin UI enhancement.

Spotter uses centralized Web Browser settings as intended.

Smart Search automatically selects the first tab enabled if no tab was selected by the Operator.

Spotter UI scaling works as intended.

Spotter Web and Mobile

A warning message is displayed before exporting when a Camera name contains symbols that are not permitted.

Logging in to Spotter Web Mobile works by double-tapping the input field.

Spotter Web exporting is done sequentially.

Spotter Web can deserialize the view configuration JSON correctly.

Spotter Web security patch.

System Manager

Selected certificates for RTSP streaming are displayed correctly.

The multiple stream option works as intended in Camera settings.

The camera settings display the Smart Service as enabled during backup for the camera/device when the settings are restored in System Manager.

User rights for adding user groups work as intended.

Audit trail search results are reset when the profile changes.

VMS Server

Failover material copy disk configuration works as intended after dvr.xml reset.

The DVR Server works as intended on OR settings changes.

The states of camera-related alarms are restored after the alarm settings are applied.

Mirasys AI Services

When a camera is disabled, streams from OR Service are removed.

Version information for LPR integration Service is displayed in the log file.

When the LPR integration Service installation uses already installed Postgres DB, and not the one installed by the installer, the error message Invalid license will be displayed when the database is off.

System

Retry mechanism of the material copy process works as intended.

Updated Memory manager and extended information about memory allocations.

Drivers

PanasonicIPCapture Driver: VideoChangeSettingsInAlarm works as intended with i-Pro WV-S22700-V2L.

PSIAIPCapture Driver: RTP over RTSP and RTP over UDP stream work as intended.

PSIAIPCapture Driver: All dynamic UI features in the camera settings work as intended.

The viewing stream timestamp is displayed correctly.

You can download the release notes as a PDF file here V9.8.2.2 Release Notes.pdf .




Pagination
Previous page
Mirasys VMS V9.9.0 release notes
Next page
Mirasys VMS V9.8.1 release notes