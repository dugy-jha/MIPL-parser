# Mirasys VMS V9.6.3 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-6-3-release-notes

Mirasys VMS V9.6.3 release notes
Release date: 05.12.2023
Enhancements

Enhancement: Alarm search added to Spotter Web back-end

Fixes
Spotter

Fixed: Loading large profiles containing many alarms without time delay.

Fixed: Spotter setting to disable activity calculation works as intended (did not work for alarms).

Fixed: Spotter shows profile alarm activity correctly in the timeline when activity collection is on and when the activity data cache is on/off.

Fixed: Large profile loading no longer causes a false disconnection state for VMS server devices, and Spotter is recovering streaming from VMS Recorder correctly.

Fixed: On Spotter startup, Spotter loads an additional window using the default profile if the loaded layout contains only one window for playing an archive.

Fixed: Spotter no longer crashes when a second user attempts to take over PTZ control from the current user without adequate permissions.

Fixed: In Spotter, PTZ area zoom or centering operations are performed when clicking the PTZ control toolbar.

Fixed: In Spotter, the PTZ control toolbar is now hidden when users pan and tilt the camera.

Fixed: Alarm Errors in Spotter Log. Alarms that are no longer being used are now automatically cleaned from profiles without configuration on the main server startup.

Fixed: The alarm action devices are properly shown on the alarm view when the alarm trigger device is configured not to be displayed.

Spotter Web

Fixed: Spotter Web installer spelling mistake

System Manager

Fixed: Save settings for FR in System Manager works as intended

Fixed: System Manager no longer crashes when opening the Privacy tab in the Camera Settings dialog

Fixed: VCA streaming works as intended

Fixed: System Manager works as intended when the motion detection tab is clicked

VMS Server

Fixed: VCA Core is not initialized when the setup is not configured to use VCA core.
Additional testing has been done during daylight savings time for Finland and US time zones, where the daylight saving time shift occurs on different dates.

Fixed: MxPeg (Mobotix) streams are working as intended in the VMS RTSP Server

Fixed: Uninstallation works as intended

Fixed: The recorder works as intended after a license update

Fixed: Users can proceed with the installation as intended when using the installation wizard and selecting “Start after SQL.”

License Plate Recognition | Face Recognition | List Management

Fixed: The LMS installer will remove orphaned records from the database

Fixed: Recorder Privacy Masks event receiver initialized with LPR and FR services

Driver

Fixed: Adding Moxa to Mirasys VMS works as intended

Fixed: Easy LPR is working with Dahua ANPR ITC413




You can download the release notes as a PDF file here V9.6.3 Release Notes .pdf .

Pagination
Previous page
Mirasys VMS V9.7.0 release notes
Next page
Mirasys VMS V9.6.2.2 release notes