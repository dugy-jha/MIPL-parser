# Mirasys VMS V9.6.0 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-6-0-release-notes

Mirasys VMS V9.6.0 release notes
Release date: 04.07.2023
We have a new look for the Mirasys documentation site

The Mirasys documentation has a new look, and new documentation has been added. Please see our new site here and contact Support if you are missing any user information that you would like us to add.

Face Recognition

Identify human faces and receive events when a specific person is seen in a video with the new Face Recognition (FR) feature.

Face recognition can speed up the process of searching through video footage for a particular individual. It enhances security capabilities by identifying and cross-verifying individuals in real time against a database of known individuals. This can be useful in various security scenarios, like preventing unauthorized access and identifying suspicious behavior.

Facial recognition can be used for access control in sensitive areas. It can replace or supplement traditional access control mechanisms like keycards or passwords, which can be stolen or forgotten.

Note that anti-spoofing is not included in version 9.6.

Face recognition allows for hands-free operation, which is more user-friendly and efficient than manual input methods. The Face Recognition Service receives video streams, processes images, detects faces, and sends notifications with detection data. The detection events are sent to the VMS Server which saves the detection details, which can be visualized in Spotter using the VCA visualization plugin.

Face Recognition service has a separate installer, so it can execute on a separate server or on some VMS server.

License Plate Recognition

License Plate Recognition (LPR) can help enhance security at various facilities by tracking and recording vehicles' entry and exit. They can be used to enforce parking restrictions, prevent unauthorized access, and identify stolen or suspicious vehicles. LPR can make searching for specific incidents involving particular vehicles in video footage much more efficient, saving time and resources. Get events when specific car plates are detected in the video by storing the settings for License plate recognition (LPR) and managing the settings. While the Easy LPR only works with pre-determined cameras, you can choose which camera you will use with Mirasys License Plate Recognition.

The License Plate Recognition Service receives video streams, processes images, detects license plates, and sends notifications with detection data. The detection events are sent to the VMS Server which saves the detection details, which can be visualized in Spotter using the VCA visualization plugin.

Plate number detection is available for Eurasia and the Americas. Please see the user documentation for a list of supported countries.

License Plate Recognition service has a separate installer, so it can execute on a separate server or on some VMS server.

List Management

List management (LM) is used to store identities and identity list information, receive and save Face Recognition events and License Plate Recognition events from the LPR service or ANPR camera and do searches in saved events. It allows you to have nearly unlimited identities and lists, making it possible to define identities and lists to determine the allowed or not allowed identities.

LM service does the following:

Store identities and identity lists in the database

Receive and store LPR and FR events in the database

Match detected license plates and faces to defined identities and identity lists

Search LPR and FR events from the database using search parameters

Send real-time LPR and FR events for clients and VMS Servers

Send LPR and FR events to the VMS server for processing

Notify clients and VMS Servers about changes in identities and identity lists

Enable integration to License Plate and Face recognition

List management settings can be managed on the System Manager side list management settings and on the Spotter side Smart List Management plugin, where managing identities and identity lists is possible.

The list Management service has a separate installer, so it can execute on a separate server or on some VMS server.

System Manager Audit Trail Logs

Viewing and searching VMS audit logs can now be done by time, user, and operation by the VMS users. You can easily search by date, time, end time, user, application, max result count, and operation.

The report can be exported in PDF format and printed out. It will have the user name with printing time as the title for the audit trail log.

Spotter Plugins
Smart Recognition Plugin

The Smart Recognition plugin receives live face and license plate detection events and identity match events when you use Mirasys Face Recognition and Mirasys License Plate Recognition. Video footage related to the event can be viewed in detail. Users can define the events that are shown in the detection events list and also use the detected faces and license plates to create new identities or update existing identities. Selected events can be selected for exporting to clip and to storyboard.

Smart Search Plugin

The Smart Search plugin can be used to search for face and license plate detection events that are matched or unmatched to known identities and lists when you use Mirasys Face Recognition and Mirasys License Plate Recognition. Based on a selected face detection event, it searches for similar faces for Mirasys Face Recognition. Video footage related to the found events can be viewed in detail. Found detections (face or license plate) can be used to create new identities or update existing identities. Selected events can be selected for exporting to clip and to storyboard. Searched events can be exported to a Pdf format report with all detection, identity, and list details.

Smart List Management Plugin

The Smart List Management plugin defines the identities that can be allowed or disallowed access to the premises, allowing you to, for example, create an automatic detection system of cars' access to the premises.

The smart list management tab plugin also provides list management functionality in Spotter for users with permission to do list management changes but cannot access the System Manager application.

Mirasys Video Wall (AVM Plugin) and the Monitor Manager improvements
Plugins in the device grid

Mirasys Video Wall (AVM) and Monitor Manager plugins can be placed into the device grid.

Time search using the time slider

When you release the time slider green balloon, the operator console sends a time to search to the Display Server. The operator console time slider is updated when the playback time is changed.

Spotter
MP4 Export: timestamp

MP4 is supported as an export format, with or without a timestamp.

PTZ Camera Control

The system Manager profile setting has a new option Open when selected for PTZ cameras that automatically activates dome camera control when the dome camera view is selected in Spotter.

Spotter Camera Grid Selection

Open the camera grid and use the automatic fit (Crop, Stretch, and None options) selection directly from the Spotter playback panel.

Playback speed adjustment

When the playback synchronizer cannot keep pace with 2x, 4x, and 8x playback speeds, it will jump to fast forward/backward. Spotter user role has a new option if this automatic fast forward/backward is used or not.

Automatic User Login

Spotter will log on automatically when automatic log-in is selected. Spotter has a new option if the logon is executed for the user who was the Spotter start-up login user or for the user that last made the logon.

Postpone Spotter restart

Spotter restart can be postponed in a similar way as the settings update can be postponed. This option can be enabled from the Spotter user role. Postpone time and the possibility to trigger restart are shown in Spotter UI.

Device view text alignment

Define the alignment of the device view text in Spotter settings to top/middle/bottom and left/center/right.

Digital Zoom

In the camera view, digital zooming usability has improved usability when using the right mouse button.

System Manager
Adding Camera Using CSV files

Exporting configured cameras and adding a list of cameras to the system is now possible using a CSV format file.

Export Logs

Collecting Export Logs from several all system services into one single zip file is now possible.

Storage Locker Settings

No need to wait for export files to be downloaded to the local disk. Playback exports that are stored in Storage Locker are now possible directly from the network disk. You can now also map network disks directly from Storage Locker settings.

Easy LPR

UI improvements.

VCA Core

VCA Core version is updated to version V1.6.3.




Bug fixes
Spotter Web
Major

PTZ presets moving is working in iOS for Spotter Web desktop (Spotter Mobile does not support PTZ control).

Spotter Web uses the correct user when reserving PTZ control.

Minor

The trial version label no longer appears on the Export page.

Spotter
Major

The stream selection is working correctly, including when the image fit option None is in use.

The Camera audit has been optimized for when the profile contains a lot of cameras, in order to operate max 50 cameras in parallel.

Optimization has been done to playback synchronizer to work better with multiple playback streams.

Minor

Windows default shortcuts (window key + arrow keys) are working as intended.

Person search result list clearing is working as intended.

Spotter allows users to select the same preset even if it is already selected.

The alarm popup settings saving is working as intended.

Automatic grid calculation prevents video images from going black.  

VCA visualization is enabled for smart or easy LPR

Spotter works when drag-and-drop cameras and the license has a low stream count

Spotter Public Web API
Minor

Examples have been added to the Spotter public Web API sample application to show how to reserve and free PTZ control for multiple cameras

System Manager
Major

New camera capabilities will be applied to the HW settings after the camera has been updated

License calculation in UI for multi-channel devices is correct when the configured camera count is more than the license count

Camera settings are working when multi-streaming is enabled and settings are changed

All changes are applied correctly without any unnecessary profile loading time when a profile is edited and the VMS Server is stopped.

Minor

Storage Settings shows the cameras in the correct order

Enable and disable System Manager UI buttons are working correctly, and edit and delete options are available when after saving settings.

Correct hours are showing in the calendar.

VMS server
Major

The DvrServer startup issue with VCA Core has been fixed.

The storage is mapped correctly to the network when using the old file system.

The archiving process has been optimized.

Edge Storage Management is working correctly.

Improved usage of VCA Core events to allow get alarm triggers when multiple rules are defined.

Small optimization on VMS Server to update the settings without a full-service restart.

Analog camera configuration files were added to the backup process.

All cameras with VCA Core enabled are now showing in VCA settings.

The camera sends no signal event when the VMS Server is reinitialized.

Gateway
Minor

Logging has been fixed in GW for unnecessary logging.

System

All server logs are now included in the log export.

Drivers

Easy LPR now only receives and shows plates once from Axis Q1700-LE.

I-frame settings for Axis driver in camera advanced settings.

PTZ camera control and the area zoom for Dahua DH-SD6CE230U-HNI are working correctly.

You can download the release notes as a PDF file here V9.6 Release Notes .pdf.




Pagination
Previous page
Mirasys VMS V9.6.1 release notes
Next page
Mirasys VMS V.9.5.4 release notes