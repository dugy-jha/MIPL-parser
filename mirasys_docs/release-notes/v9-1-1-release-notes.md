# Mirasys VMS V9.1.1 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-1-1-release-notes

Mirasys VMS V9.1.1 release notes
New Features
Test email sending

Test email can be sent in System Manager email settings for selected email addresses. Test email sending button can be found under the email addresses list.
Test email sending uses email settings defined in the email settings dialogue and the result of the test email sending is shown to the user.

New product type

The newly introduced version type Enterprise Plus will have all available features of the software by default enabled. For more details see the feature list document.

Spotter profile folder search

Spotter profile tree has the possibility to make a sub-search from the profile folder.
While the top-level profile search does the search for all items in the profile tree, the profile folder sub-search makes the search to the selected profile folder and its sub-folders.
All searches can be cleared from the top-level search X-button.




 

Other minor changes

HEVC codec support added to Media Exporter CA tool

HEVC codec support added to Gateway SDK test application

Added connection timeout value to Spotter AVM Operator Console that can be adjusted from Spotter settings

Added default joystick setup for Axis T8311 to Spotter

Right mouse button double click can be used to exit Spotter full-screen mode

Removed UHDCode HEVC codec. If UHDCode HEVC codec was in use, Intel HEVC codec will be used instead in the new version

Changelog V9.1.1 - 2020/10/30

Fix Alarms drop-down list in Spotter alarm search is too small for alarms with a long name

Fix: Alarm names are shown as “-” after the master upgrade

Fix: Spotter alarm search causes Spotter to disconnect from the master server

Fix: Control device Esc command does not work when Spotter is in full screen

Fix: Spotter Web API returns an error with view query if plugin tab is currently selected

Fix: VMS server starts to use a lot of CPU in systems with a lot of cameras

Fix: Spotter VCA visualization works incorrectly when the image is mirrored or flipped

Fix: Spotter crash when trying to use a sound card that does not exist

Fix: VMS server gives wrong oldest stored material time

Fix: Spotter crash when using alarm popup

Fix: Spotter camera audit plugin doesn’t show playback view

Fix: Spotter camera audit plugin doesn’t start playback automatically

Fix: System Manager makes relogin just after user logs incorrectly

Fix: Asf/Wmv clips cannot be dragged and dropped to Spotter or SpotterPlayer

Fix: VMS server does not update metadata configuration file automatically on an update to contain new metadata drivers

Miscellaneous minor and cosmetic changes

Pagination
Previous page
Mirasys VMS V9.2 release notes
Next page
Mirasys VMS V9.1.0 release notes