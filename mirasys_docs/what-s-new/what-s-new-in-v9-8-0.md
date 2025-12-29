# What's new in V9.8.0 | Mirasys Help Center

Source: https://documentation.mirasys.com/what-s-new/whatsnew/what-s-new-in-v9-8-0

What's new in V9.8.0
Release date: 17.05.2024
Object recognition search for persons and vehicles

We are introducing Object Recognition Search to our VMS. Operators can now search recordings for attributes for both persons and vehicles. The object recognition search searches by the following criteria: where (which cameras), when (time frame), and what (humans or vehicles and their attributes).

For persons, searchable attributes are upper body clothing color (Black, White, Gray, Blue, Green, Red, Yellow), lower body clothing color (Black, Blue, White, Gray, Brown, Green), if they are carrying a bag (generic), and if they are wearing a headwear (generic).

Vehicles can be searched by type (car, motorcycle, van, truck, bicycle, or bus) and by color (Black, Blue, Brown, Gray, Green, Orange, Red, White, and Yellow).

Our System Manager have added settings for System Administrators to enable object detection for the camera channel and manage object detection parameters and licensing, as well as search storage settings.

VMS Backup now includes SmartLM, FR, OR and LPR configurations.

Improved Smart Search

We have updated Smart Search, which now includes object recognition. You can filter out cameras by detection type: LPR, FR, or OR. Similarity search has its own tab, just like face recognition, license plate recognition, and object recognition.

It is possible to hide the search criteria so that there’s more space available for the list. When the search criteria are collapsed, the search result and the stream view can be adjusted to take up more or less space on the screen by using the white drag handle.

Usability improvements: Profile tree re-design

The profile tree has been redesigned so that the Device Tree now occupies most of the space and remains open when Operators go into Device Tree, Layouts, Plugins, Bookmarks, and Saved Tabs. Icons have been added, and Operators can adjust the space these functionalities take up under the Device Tree.

Enhanced Audit Trail Log in System Manager

We have enhanced the Audit Log functionality within the System Manager to provide a more detailed and comprehensive view of audit events. System Administrators can now refine their search with parameters like date, time, user, application, recorder IP address, and specific events. The "Select all or unselect all" feature for selecting audit trail events has improved design and user-friendliness.

The Audit Trail Log result list now displays crucial information at a glance, including Local time for each event, User names, Application and IP address, Detailed event information, and comments particularly useful for playback requests, Event status, object involved, and Recorder IP address and name.

These enhancements bring transparency and detail to system audits and significantly improve security and compliance processes.

Optimization for VMS Server setting changes and updates

Changing settings for text data, storage, alarms, digital I/Os, and general recorder settings has been improved to avoid video loss. Updates will no longer require a recorder service restart.

Note that the following will still require restarting the VMS Server:

General settings: Changes to the VMS role (from normal to failover). In this case the VMS Server will go into idle state and no recording is performed.

Storage settings: Changes to the file system disk configuration.

Storage settings: Change “Use OS cache” or “OS cache max value” settings. This requires to reopen files to re-write, because it changes the writing type from direct writing to disk to OS cached and vise-a-versa.

Improved Profile Loading time in System Manager

To improve loading time in System Manager, we have removed the content loading in the left-hand sidebar, and only the profile names are now displayed. When the user clicks a profile name, it opens the profile settings, loads the content, and displays it. This optimization will significantly improve loading time for systems with large profiles.







Free adjustment of camera frame rate and resolution

System Administrators can freely adjust the camera frame rate and resolution without auto-adjustment. We have removed the performance bar, the automatic framerate optimization, and the camera load indicator from the VMS Server’s Camera Settings (previously located under the general tab) for this enhancement.

Direct Alarm Clip Export to a Specific Folder

When system administrators enable and configure this feature in Spotter Alarm Export settings, it is possible to directly export an alarm to a specific folder in Alarm Search from the Alarms table in Spotter to enhance workflow efficiency for Operators. This allows operators to mark alarms for immediate export by simply clicking a button with a folder icon next to the alarm, and it will be swiftly exported to the designated folder. Alarms exported to the assigned folder will be marked as "Exported to Folder.”

Specific roles can be assigned permissions by the System Administrator to create settings for alarm processing. There will be an indication to the operator if the alarm export could not be carried out successfully.

We have segmented Spotter settings for alarms that are directly exported to a designated folder, which include Storage Selection, Folder Name, Export Name, Copy Player Option, Format, Export Quality, and Password Protection.

This feature can be used for a specific purpose, such as exporting false positives for AI model training.

Default alarm filtering settings for alarm popup

We have added alarm default filtering settings for alarm popups. By default, alarms are not filtered, and all alarms will be shown.

With this alarm filtering enabled, a new option exists to sort the alarms from newest to oldest and to select which active alarms are shown in the alarm popup. Specific alarm popup settings can override generic settings. The defined alarm filtering settings are used when the alarm popup is opened.

Sharing bookmarks and layout with selected operators

Operators now have the choice to share bookmarks and layouts with selected users. System administrators can restrict sharing with selected users according to the assigned user permission. By default, this role permission will be disabled, and can be enabled by System Administrators.

When sharing bookmarks with a selected user, the operator can share with all users sharing the same profile. Bookmarks can be shared with all users using the same profile as the operator sharing the bookmark. Operators can choose whether to share the tab content with others after saving a tab in Spotter. Layouts can be shared to all users.

A list of users is presented for selection, including the option to share the tab with all users. This allows for specific or broad sharing as per user discretion. Users are listed alphabetically, with logged-in users (indicated by a green dot) displayed first, followed by those not logged in (indicated by a grey dot), also in alphabetical order.

The Spotter profile tree displays all tabs saved by the user, tabs shared by others to all users, and tabs specifically saved for the logged-in user, filtered by accessible profiles.

CSV file import enhancements

Understanding the importance of finely tuned control over camera settings, especially when deploying large numbers of devices, we have addressed a limitation in the import functionality of CSV camera settings. Previously, cameras imported via CSV could not be set to passive mode as part of the import process, requiring administrators to adjust this setting manually for each camera. We acknowledge the inconvenience this has caused, especially for larger installations.

We are including passive mode configuration as part of the CSV import process to remedy this. We aim to enable administrators to specify this setting within the CSV file, streamlining the setup process and reducing the need for manual configuration post-import.

We also added multiple streaming state (enabled or disabled) when this is supported by the camera, and bitrate mode for bitrate.

Further, audio channels were inadvertently present despite not being added through the CSV file import for new installations. From V9.8, audio channels should not be automatically added when it is not added when importing CSV files.

I/O Alarm enhancement

The current I/O alarm logic is that when the I/O is off it creates an alarm, and when it is on it does not create an alarm. If the polarity is changed, it changes both the icons and alarms.

We have now added the option to invert this behaviour without this affecting the alarm triggering. There is a new icon set with inverted icons that can be changed in profile settings for inputs and outputs.

Driver improvements

The option for ONVIF driver to disable "Point and click" (Centering) and "Box draw" (Area Zoom) for PTZ cameras has been added for cases when it is not working properly.

The option to disable Allow enhanced prediction via Bosch Driver has been added.

The number of streams the Axis Driver can receive has increased from four to five. Adding a fifth stream will require an additional license.

Intellio cameras work with the RTSPIPCapture Driver.

Immervision de-warping updated

The Spotter camera 360 plugin used for de-warping 360 camera images has been updated with the latest Immervision SDK.

System improvements

Our AI services are updated to use .NET 8

External components have been updated.

Bug Fixes
Spotter

The “Edit preset button” is always accessible for PTZ control.

The device limit camera count logic is applied to all devices.

Cameras that are not in use state can be opened in Spotter for playback.

AVM Plugin licensing works as intended.

The activity data cache works as intended in Spotter for video, audio, text data, and alarms.

Spotter connection to the main server works as intended.

VCA Core’s “Hands Up” feature works as intended.

Timestamp of the failover events shown in Spotter to use local time.

Material copying messages in Spotter includes the percentage value.

Spotter works as intended when the http://youtube.com address is used in the Web browser plugin.

Spotter role settings UI has been adapted to all languages.

Spotter works as expected when system settings are applied.

Spotter Web

Audit trail events saved by Spotter Web contain the recorder’s address and name.

Spotter Web loading time of large device profiles has been improved.

Spotter Web security patches and updates.

Spotter Web Mobile

Camera names have correct scaling in the layout.

The first camera is displayed in the camera list.

Downloading files works as intended.

Alarms are in sync in Spotter Web Mobile and Spotter/Spotter Web.

The size of the sign-on button has been adjusted.

The export notification works as intended.

Camera picture is shown in the mobile browser.

Spotter Web Mobile stays logged in when the screen is active.

System Manager

Audit trail events are always saved with the VMS Server name.

When opening user group settings, list management settings loading is skipped when list management is not installed.

Profile devices are not automatically sorted in alphabetical order.

Birate and Birate modes are exported to CSV file for single and multiple cameras.

Save recorder settings works as intended.

VMS Server

The SMServer can connect to the recorder after the failover process.

The activity data cache works as intended in the VMS Server for video, audio, text data, and alarms.

I/O alarm logic works as intended.

Stream encryption can be changed and works as intended for the failover material copying and server.

Face Recognition (FR), License Plate Recognition (LPR), List Management (LM)

If a recorder is removed when a service is offline, the service will receive this update.

License plate matching use both license plate number and area code when the area code is used in identities.

Dedicated dump file location for all services

System

Failover server and failed VMS server connections are managed properly in SMServer service when doing failover and failback.

Failover, failback and failover material copying works as expected when communication encryption is enabled.

SMServer checking for system data change works as intended.

VMS server connections are managed properly when saving VMS server settings. 

Driver

Enabling audio output for a camera using the ONVIF Driver works as expected.

Hikvision DS-2CD6365G1-IVS (360) images are correctly displayed using Intel HW decoding.

The Moxa Driver is selected for the camera first if multiple PTZ Drivers are available.

The Moxa PTZ Driver uses 1-based camera index for Bosch OSRD protocol.

Simultaneous pan/tilt and zoom is working with the Bosch OSRD protocol and Pelco D protocol.

The Moxa PTZ Driver allows controlling multiple cameras.




You can download the release notes as a PDF file here V9.8.0 Release Notes.pdf.

Pagination
Previous page
What's new in V9.9.0
Next page
What's new in V9.7.0