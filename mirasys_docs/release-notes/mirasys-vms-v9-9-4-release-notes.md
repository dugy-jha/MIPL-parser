# Mirasys VMS V9.9.4 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/mirasys-vms-v9-9-4-release-notes

Mirasys VMS V9.9.4 release notes
Release date: 13.08.2025
Enhancements
Alarm sound looping

The alarm profile sound can be configured in the System Manager profile settings to loop the sound until the alarm ends in the Spotter application.

Fixes
System

When using V9.9.4 VMS server or client installation and starting a client application, the connection to the V9.5.0 and older version main server works as intended.

SlimDX installation error causes the VMS installers to fail.

PDF and SVG map images are included in the settings backup file, and the images are correctly restored on settings restore.

System Management Service

The performance counters work as intended.

VMS Service

The VCA counter alarm works as intended.

The Hardware settings in the System Manager can be used even if audio devices are not available.

In the event of an unexpected shutdown, the VMS server retains the data that has already been written to the disk.

Events for the same incident from the Hikvision proxy cause a single alarm triggering.

AI services

AI services disable the HW decoding if no compatible device is found.

A proper error message is shown in AI service installers if NVIDIA hardware or driver version is too old.

System Manager

Editing the profile folder name in System Manager works as intended when a system update event is received.

Sort direction (ascending/descending) does not change when the Watchdog events list is updated.

VCA log files are included in the log export.

Spotter

The TruCast stream is working correctly for the ONVIF driver.

Spotter works as intended when the VMS server name is set to a video view.

Icons are shown as intended in the Spotter profile tree for plugin items.

The Smart Recognition plugin combobox controls work as intended.

The profile search works correctly with all profile node types.

Profile tree icons for input and output controls are shown correctly in the Spotter profile tree.

Alarms work as intended after the settings restore is done.

Video buffers are handled correctly during video processing, and the buffers are recycled after the processing is complete.

The alarm pop-up plugin works as intended when the alarm pop-up global algorithm is updated.

Drivers
NewAxisIPCapture V2.9.10.1

The driver works as intended with Axis cameras using an HTTPS connection.

Axis camera motion detection works as intended.

The AXIS Q1806-LE camera capabilities are detected correctly.

Time stamp calculation for incoming frames works as intended.

UniversalOutputDriver V1.0.2.0

The Universal Output Driver can run applications without a logged-in user.

ONVIFIPCapture V1.9.16.0

The ONVIF events from different camera channels (heads) are handled correctly by the driver.

The ONVIF driver handles the PropertyOperation value of the property events.




You can download the release notes as a PDF file here: Mirasys VMS V9.9.4 Release Notes.pdf

Pagination
Previous page
Mirasys VMS V9.9.5 release notes
Next page
Mirasys VMS V9.9.3 release notes