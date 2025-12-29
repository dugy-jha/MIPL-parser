# Mirasys VMS V9.7.1 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-7-1-release-notes

Mirasys VMS V9.7.1 release notes
Release date: 19.03.2024
VMS V9.7.1 Enhancements

Driver version is displayed with the Driver in System Manager Camera Settings under Camera Driver information.

The ONVIF Driver is updated. The latest version will skip PTZ presets loading when the device has been configured in the Driver XML file.

VMS V9.7.1 Fixes
Spotter

Fixed: Export to Storage Locker works as intended.

Fixed: Spotter settings saving works as intended for imported AD users.

Fixed: Error message displayed when tab content is not saved due to SM Server being down.

Fixed: The forklift and other vehicle attribute visualization in VCA Core have been added in Spotter.

Fixed: Smart Search plugin search renders correct search results for 1000 results and above.

Fixed: Smart List Management plugin shows buttons when numerous face images are added for the identity.

Fixed: Spotter is showing VCA metadata correctly.

Fixed: Spotter works as intended when previewing Storyboard.

Fixed: Users are not able to access a password-protected shared bookmark.

Fixed: Spotter Smart Search plugin displays correct percentage values in the Identity column.

Fixed: Password is saved as encrypted text in the Spotter settings file.

Fixed: Spotter converts metadata correctly.

Spotter Web

Fixed: Removing a removed camera from the view works as intended.

Fixed: Alarm events duration and the time since the alarm start is clear and consistent in the alarm list in Spotter Web.

Fixed: In Spotter Web Export, 64-character file names fit within the export progress dialog.

Fixed: Spotter Web shows devices on the export dialog in Firefox.

Fixed: Spotter Web profile loading works as intended.

Fixed: Live stream opening works as expected when the same stream is opened from several clients simultaneously.

System Manager

Fixed: When the “Driver” field is empty in the CSV file, all selected drivers are used for the capability query. If both native and ONVIF drivers can be used, then the ONVIF is used by default.

Fixed: HTTP error handling works as intended in System Manager.

Fixed: Spotter role settings playback limit time is not reset to 5 minutes by default, instead of keeping the playback limit time previously defined by the user.

Fixed: Saved alarms work as intended in the UI alarm list in System Manager.

Fixed: The System Manager works as intended after digital I/O configuration changes.

Fixed: When multiple devices of the same kind are selected from the profile tree in profile settings, the shortcut number is not changed.

Fixed: System Manager displays an error to the user that the download has failed when VAU cannot download Spotter.

Fixed: The profile tree in profile map settings will work as intended when clicking the device on the tree.

VMS Server

Fixed: Material copy works as intended.

Fixed: Failover works as intended during upgrades to V9.7.

Fixed: When recording for 72h, there is only data for 72h.

Fixed: VMS server stops correctly (without “pure virtual call“ error in log) with enabled RTSP streams for IP cameras.

Fixed: VCA configuration from the backup file can be restored to a recorder whose address differs from the recorder in the backup.

Fixed: When a network MOXA IO device is added to the VMS Server and the network connection is broken, the user will only get one error message in the recorder log.

FR, LPR and LM

Fixed: List Manager Service installation works as intended.

Fixed: To prevent extra memory load and slowing down of process startup, files for the LPR region, as well as devices, must be selected upon installation instead of being automatically included.

System

Fixed: When restoring the V9.6 backup to V9.7, VCA settings work as intended, and configurations and created engine files are intact.

Fixed: Failover VMS version number is displayed correctly.

Fixed: Pre-recording functionality works as intended.

Drivers

Fixed: Hikvision EasyLPR is working as intended with latest Hikvision Driver.

Fixed: Privacy mask/zone now updating on the camera side with the ONVIF Driver.

Fixed: Audio in the Bosch Driver works as intended.

Fixed: The Hikvision Driver supports the Hikvision DS-2CD6365G1-IVS camera.

You can download the release notes as a PDF file here V9.7.1 Release Notes.pdf

Pagination
Previous page
Mirasys VMS V9.7.2 release notes
Next page
Mirasys VMS V9.7.0 release notes