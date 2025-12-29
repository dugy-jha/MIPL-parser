# Mirasys VMS V9.6.2.2 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-6-2-release-notes

Mirasys VMS V9.6.2.2 release notes
Release date: 03.11.2023
Enhancements

ONVIF driver support for focus and iris.

Moxa driver support for PTZ camera control

Bosch MIC 7100i camera support to radar proxy

Fix for 9.6.2.2 

Fixed: VCA Core updated to V1.6.4 and works as expected during daylight savings time changes.  

Fixes 
Spotter

Fixed: Spotter works as expected when users edit existing identities in the Smart List Management plugin.

Fixed: Storyboard export works without executing normal export first.

Fixed: Camera feature for corridor mode, and timestamp work in Smart Recognition and Smart Search.

Fixed: Smart Recognition and Smart Search plugins are displaying all ID data.

Fixed: Search results for unknown identity search in the Smart Search plugin.

Fixed: Spotter shows VCA metadata alarms correctly.

Fixed: The alarm popup shows alarms only if enabled for the action devices.

Fixed: Login works correctly when using Media Exporter and AD account.

Fixed: Input and output icons that are shown correctly in the alarm search

Fixed: Spotter works on start-up after large resolution has been logged in.

Fixed: The joystick device settings dialog layout stays the same when using the Saving Device button.

Fixed: Smart Search plugin text field search reads uppercase and lowercase letters the same.

Fixed: The @ character can be used in all text boxes.

Spotter Web 

Fixed: Date and time selection for playback works correctly on the timeline.

Fixed: The state of Digital Output and pulse can be changed in the UI.

Fixed: Missing icons for Digital Input and Digital Output have been added.

System Manager

Fixed: Adding the latest version of Recorder to an old version of SMServer is possible.

Fixed: Encrypt stream data checkbox is available in General Settings.

Fixed: System Manager is still working when log export compression fails.

Fixed: Manual log-off of users by Administrator working correctly.

Fixed: Possible to create several identities using the same name.

Fixed: Changes are saved when importing the camera list after changing the username or password.

Fixed: Streaming codecs are in the same order as viewing and streaming quality.

Fixed: Changes are visible when the custom GOV Length is changed in the System Manager

Fixed: Removed outdated recorder API settings in System Manager

Fixed: When Hailo is chosen as the device in FR and LPR settings, plates and faces are properly detected without any issue.

Fixed: Finnish translation for logged-in user.

System

Fixed: Data storage limits apply for pre-recording data

Fixed: VAU downloads without error.

Fixed: Exception in SMServer log related to Recorder.

Fixed: PostgreSQL spelling in the LM installer.

Drivers

Fixed: Onvif driver detects the right PTZ movement timeout.

Fixed: Bosch camera and camera-based motion detection does not stream if motion detection on camera is used, there is no motion and no opened streams in Spotter.

Fixed: Bosch Videojet 4000 encoder can be added as part of the VMS system with the latest Bosch driver.




You can download the release notes as a PDF file here V9.6.2.2 Release Notes.pdf.

Pagination
Previous page
Mirasys VMS V9.6.3 release notes
Next page
Mirasys VMS V9.6.1 release notes