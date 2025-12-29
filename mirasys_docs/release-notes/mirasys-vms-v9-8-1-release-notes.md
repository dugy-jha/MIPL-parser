# Mirasys VMS V9.8.1 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/mirasys-vms-v9-8-1-release-notes

Mirasys VMS V9.8.1 release notes
Release date: 25.06.2024
Enhancement

New Profile I/O icons have been added to System Manager, Spotter, and Spotter Web.

Optimization for Object Recognition Inference.

Spotter Web Mobile UI enhancement for the “Cameras, Export, and Alarms” menu.

Spotter

The grid selection icon is hidden when creating a Storyboard and previewing it.

When selecting the system address or system name upon login in Spotter, long names in the user name list are displayed correctly.

Spotter quad view selection is displayed correctly for ImmerVision cameras when 360-degree view is enabled.

The Camera View is displayed correctly when using multiple streaming and Intel decoding.

Clicking the two-way audio icon opens the correct channels.

Spotter tree search works as intended.

Filtering in Smart Recognition works as intended.

Smart Search item selection works as intended.

Smart Search for multiple attributes works as intended.

Smart search finding results for matching license plates and showing corresponding identities works as intended.

Operators cannot access the Storage Locker file store path.

When the export is canceled, the export process ends immediately.

When the selected list item for Smart Search is a vehicle, the similarity search button will be disabled.

Spotter Web and Mobile

Spotter Web security patches and updates.

The playback panel only takes up one line in the layout.

Spotter Web Mobile login works as intended on iOS devices.

Usability improvement for tapping the input field to enter the username when logging in.

System Manager

UI controls update time in the “RTSP Server Streaming“ tab has been improved.

Saving settings before the editable regions are loaded works as intended.

In Audit Trail search parameters, long DNS under VMS Server is displayed as expected.

Camera CSV list import works as intended.

Smart Object Recognition values tooltip displays the correct information.

UI elements are adjusted correctly when the Failover Log dialog is resized.

The false error message on the services screen (LPR) no longer appears when enabling LPR for a camera with an RTSP stream enabled.

Unhandled Exception in System Manager during OR / LPR / FR settings save has been fixed.

Saving FR, LPR, and OR settings for cameras in local and remote recorders works as intended.

Centralized Spotter plugin configuration for selection and option items works as intended.

VMS Server

The VMS Server works as intended on digital IO open/close.

Alarm limits for storage time are working as intended.

Face Recognition (FR), Licence Plate Recognition (LPR), Object Recognition (OR)

LMS and ODS memory handling and removing old data have been stabilized.

System

Communication encryption is working as intended for failover material copying.

Material copy works as intended when started before the failover server is online.

Automatic material copy works as intended when the server is shut down.

DVRService initializes as intended.

Missing Chromium browser component files added to the System Manager and Spotter installation.

VMS license level updating works as intended.

The alarm log copy works as intended when a new VMS Server is added to the System Manager.

Drivers

EHIIPCapture Driver works as intended with Hikvision iDS-2CD7A26G0/P-IZHSY (ANPR/LPR) H8-platform.

List upload works as intended for Easy LPR with the EHIIPCapture Driver for the Hikvision iDS-2CD7A26G0/P-IZHSY camera.

License plate numbers are displayed in correct lists for Easy LPR with the EHIIPCapture Driver for the Hikvision iDS-2CD7A26G0/P-IZHSY camera.

i-Pro WV-S22700-V2L is compatible with the ONVIF Driver.

Video Change settings for Alarms work as intended with the Panasonic Driver for i-Pro VV-S22700-V2L.

You can download the release notes as a PDF file here V9.8.1 Release Notes.docx .

Pagination
Previous page
Mirasys VMS V9.8.2.2 release notes
Next page
Mirasys VMS V9.8.0 release notes