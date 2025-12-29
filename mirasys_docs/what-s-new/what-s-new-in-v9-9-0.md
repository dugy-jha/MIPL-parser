# What's new in V9.9.0 | Mirasys Help Center

Source: https://documentation.mirasys.com/what-s-new/whatsnew/what-s-new-in-v9-9-0

What's new in V9.9.0
Release date: 7.11.2024
Alarm Triggering Web API Integration

Mirasys VMS software will have an HTTP API for triggering alarms within the video management system (VMS). This API allows security operators to swiftly respond to security incidents detected by third-party applications and devices, ensuring seamless coordination and timely actions.

Modifications have been made on the VMS Server side and System Manager to facilitate the registration, editing, and triggering of alarms. System Administrators can register triggering events via the API, which will appear as external alarm triggers in the VMS system settings. The System Administrator and Spotter now support the new alarm trigger type across various interfaces such as alarm list, alarm view, alarm popup, alarm search, and timeline.

Alongside existing alarm trigger types, the system now supports the new alarm trigger type introduced by the API. System Manager now includes settings for enabling/disabling the API.

Supported Alarm Trigger types are Motion, NoMotion, NoSignal, DigitalInput, AudioHigh, AudioLow, TextData, TextDataConnectionLost, and Metadata.

The new Trigger type created for these Alarms is External.

HTTP API Integration:

Integration of HTTP API to register and receive external alarm-triggering events.

Methods include POST for creating new registrations, PUT for modifying existing registrations, GET for retrieving a list of all registrations, and DELETE for removing registrations.

The API supports sending trigger events.

You can request Mirasys Web API to trigger alarms here.

Creating Alarm Triggers for Mirasys Alarm Triggering Web API

To effectively use our new Alarm Triggering Web API, we have added the ability to create alarm triggers to our VMS.

There are new VMS Server settings where System Administrators can create, edit, and delete alarm triggers for this Web API based on a Channel or as a Generic Alarm.

Creating Alarm Triggers for ONVIF Profile M

The ability for System Administrators to create, edit, and delete Alarm Triggers for ONVIF Profile M empowers Operators to respond to alarms efficiently, promoting a cohesive and proactive approach to security management within the VMS.

In System Manager, under the new Alarm Trigger tab, you can create, edit, and delete alarm triggers for ONVIF Profile M conformant devices. When creating Alarm triggers, you can name the trigger, and based on the device you add the trigger for, you can select the topic (for example, “Motion Detection”) and the trigger source. You can also Enable additional parameters by selecting the name and value of the extra parameter.

Configuration options are available for ONVIF Profile M devices, allowing users to select trigger sources, apply optional filtering, and save settings effortlessly.

Spotter
Smart Live Recognition of Attributes for Persons and Vehicles

Designed for operators seeking to leverage advanced monitoring and data analysis capabilities, our smart object recognition allows you to select specific cameras to monitor live feeds, focusing on detecting attributes of persons and vehicles and enabling a tailored approach to surveillance. Operators can create, edit, and save custom storyboards from detection events, capturing crucial sequences for detailed analysis.

Custom filters should be applied to focus on specific attributes such as "red cars" or "persons with bags," streamlining the monitoring process by concentrating on relevant events. For every recognition event, view detailed information, including the attribute type (e.g., vehicle model, clothing color), confidence levels, timestamps, and visuals of the detected attributes for accurate assessment.

Manage detection events efficiently by bookmarking important detections for quick reference. Export detection data and images for reporting purposes, ensuring critical information is readily available for review or evidence.

Improved Smart Recognition 

We have updated the Smart Recognition live view, which now includes object recognition. When opening this plugin, it shows all events.  

The main filtering components are the service(s) being used, cameras, being able to narrow down in which cameras we’re searching. You can filter out cameras by detection type: LPR, FR, or OR.  

Tabs for the select services and cameras will be enabled depending on the services and cameras selected. All selections under these tabs will apply when applying filter. You can then apply changes in filtering criteria as well as pause the filtering.

Spotter VLC Player plugin

The VLC Player plugin is now available in Spotter, allowing operators to view and control advanced playback options and streaming capabilities, including HLS streams, directly within Mirasys VMS. You can set default streams for frequent use and configure auto-play settings. System Administrators can add VLC Player to profiles for permanent use via System Manager.

Periodic Refresh Option for Spotter Browser Plugin

System Administrators can enable automatic updates to sites displayed via the browser plugin at regular intervals. This option is enabled in System Manager Device Profiles, where you can configure the interval for reloading a website.

Option to Include Spotter Player when saving stored items in Storage Locker

Operators using the Storage Locker Plugin can now choose to save a copy of Spotter Player with stored items for easier access and review, to have fewer steps needed to download both media and the player simultaneously.

A new checkbox, "Include Spotter Player when saving," allows both the stored item and the player to be saved together, simplifying playback and review of stored media.

Camera Info in Spotter camera tooltip

Administrators can now choose which camera details are displayed in Spotter, offering more tailored insights for users. The selected information will automatically appear in the Camera Description in Spotter and be searchable for Operators within Spotter, improving navigation and data access.

System Administrators can enable operators to see the camera information in the Camera tooltip by adding this as a User group setting in System Manager under the new Camera Info tab in Profiles. This includes details such as VMS Server, IP address, camera model, AI features, resolution, and frame rate. Only authorized users can view this detailed camera information, enhancing control and security.

Free text search in Spotter Alarm search

We have introduced a free text search feature in the Alarm Search tab, allowing Operators to filter alarms based on keywords quickly. This enhances the ability to find specific alarms by name and simplifies alarm management in Spotter. Operators can also search alarms by start and end times and sort results by various criteria.

PDF and SVG support for Spotter Map

System Administrators can now upload and use SVG and PDF images in the System Manager profile maps for the Spotter Map plugin. Operators can benefit from clearer, more detailed maps for better navigation and situational awareness within Spotter.

SVG images offer scalable graphics that retain clarity at any zoom level, improving the visual quality of maps without pixelation.

The ability to use PDF maps allows for easier integrating existing floor plans, building layouts, and other detailed documents into the system.

Automatic Zoom to Fit for System Manager and Spotter Maps

We have introduced the "Zoom to Fit" feature in System Manager and Spotter Maps, which automatically adjusts the map to fit the screen when first loaded. A "Zoom to Fit" checkbox is now available and is selected by default for new maps. This feature simplifies map usage and provides a more seamless experience for administrators and operators.

Maps are automatically resized to fit the screen, offering better visibility and navigation from the moment they load. This ensures maps look optimal on all screen sizes without manual adjustments.

For older maps, the default zoom state remains unchanged, ensuring that users' existing layouts appear as saved and avoiding disruption to familiar setups.

Option to display the name of VMS Server in Spotter Camera view

Operators can now see the VMS Server name in the Video view by enabling this in Spotter settings.

Red Cross Overlay for Video Loss

Operators can now choose to see a red cross overlay on the Camera View when there is no video feed or another error, providing a clear visual indicator of issues. A clear visual marker makes it easy to identify video loss or other errors at a glance, and meets the requirements for government contracts requesting this visual indicator. Show error overlay can be enabled or disabled in Spotter settings.

Option to Password Protect Storyboard .sbd drafts

Password protection and encryption safeguard Storyboard drafts, to ensure that sensitive content remains secure. Passwords apply to drafts based on when they were saved, ensuring consistency and secure access. Easily update passwords, set default options, and manage draft locations for efficient workflow.

Spotter now has a dedicated Storyboard Draft tab in settings, allowing operators to set the draft location, name drafts, and protect them with password encryption. This feature ensures both Storyboard drafts and their versions are secure.

Spotter Web and Spotter Web Mobile
Two-factor authentication for Spotter Web and Spotter Web Mobile

We are excited to announce the addition of Two-Factor Authentication (2FA) to both our Web Application and Web-based Mobile Application.

2FA adds an extra layer of protection to your account by requiring a second form of verification during login.

System Managers can activate 2FA in System Manager for both our Desktop Applications and now our Web-based applications

We highly recommend enabling 2FA for increased protection of your account and data.

Improved Grid Layout in Spotter Web Mobile

We have improved the usability of Spotter Web Mobile with a more easy-to-use menu and improved grid layout.

System Manager
Device search in System Manager VMS Server tab and settings

We have enhanced the search functionality in the System Manager, specifically within the VMS Server tab and recorder settings. Managing extensive camera networks is now more efficient and user-friendly, thanks to introducing a search bar across various settings. Here's what you can expect:

A Unified Search Experience Across Settings

Navigate with ease through your camera settings without the hassle of manually scrolling through extensive lists. Our new search functionality for cameras is available in the following settings, providing a seamless and consistent experience: Camera Settings, Hardware Settings, VCA Settings, Audio Settings, Digital I/O Settings, Alarm Settings, Storage Settings, and Text Channel Settings.

Enhanced Recorder Tab Search

Finding a specific camera across multiple recorders is now possible in the new search bar in the recorder tab, which allows you to quickly identify the recorder and the specific settings where the camera is configured. This feature is especially useful in large setups with numerous cameras and recorders, turning a time-consuming task into a swift action.

Upon searching for a camera, the software intelligently filters out the results, displaying only relevant settings. For example, if you search for the "Garage camera" under a specific recorder:

The camera will be pre-selected in the search field within its settings, allowing for quick adjustments.

The search can be easily reset, enabling you to perform another search without exiting the settings.

This smart search functionality ensures that managing camera settings is more intuitive and less time-consuming.

VMS Server Camera Settings Enhancements
Alphabetical Sorting of Cameras in VMS Server Camera Settings

In the pursuit of offering a more organized and accessible interface, VMS now features the ability to sort camera names and AI server names in both ascending and descending alphabetical order. This improvement, available under System Manager > VMS Server Settings > Camera Settings, allows for quicker navigation and easier management of your devices. Whether you are looking to locate a specific camera or AI server, the new sorting options ensure that you can effortlessly organize your list to your preference.

New AI Column for Enhanced Camera Functionality

The Camera Settings section has been enriched with a new column titled "AI," aimed at providing insights into the AI capabilities enabled for each camera. Located in the general tab list view, this column showcases which AI abilities are activated for a camera, including Facial Recognition (FR), License Plate Recognition (LPR), Object Recognition (OR), and VCA Core. This addition not only enhances the visibility of AI functionalities at a glance but also simplifies the management and activation of AI features for your cameras.

Duplicate Profiles in System Manager

System Administrators can now copy existing profiles in System Manager, making it easier to create new profiles based on existing ones.

The copied profile will include identical Device, Alarm, and Map settings.

General settings such as descriptions and user groups will not be copied. The new profile will be active by default and can be edited and deleted. 

Additional VMS Improvements
Changed default values in Spotter and System Manager

Based on requests from our customers, we have changed the following default values in Spotter:

In Spotter Settings > Display, default image fit is now disabled by default.

In Spotter settings > Advanced > Master server reconnection, Reconnect automatically is now enabled by default

We have also changed the following default values in System Manager:

Storage Locker default retention settings are now set to unlimited by default.

In User groups > Role settings > Streams > Camera stream, Can jump to fast mode is now disabled by default.

Smart Search scrolling

We have improved the usability of our Smart Search when scrolling through list items.

Person similarity search

The Similarity Search now operates significantly faster, delivering quicker results and improving overall search efficiency.

The Object Detection Service has a similarity search cache to speed up Similarity Search, which can be switched on or off. You can enable or disable the similarity search cache when installing the service.

VCA Core counter values

VCA Core counter values are now stored and reset in Spotter.

Confirmation prompt for assigning device shortcuts automatically

In System Manager > Profile > Devices > Camera > Assign device shortcuts automatically, a confirmation prompt has been added to make sure you intended to (re)assign device shortcuts automatically before proceeding.

Spotter activity updating on failover and edge storage material copy

The timeline will now be automatically updated when the material copying is in progress, including being able to see the activity that occurred in the past while the material copy is going.

Performance

We have improved our AI inference and decoding capabilities using multiple NVIDIA GPUs within a single machine. This enhancement brings several key benefits:

Increased AI Processing Power

Optimized Resource Utilization

Reduced Memory Usage

This enhancement has been applied to the following services:

Face Recognition (FR) Service

Object Recognition (OR) Service

License Plate Recognition (LPR) Service

License Plate Recognition Integration Service

Material copy optimization

Material copy has been enhanced to improve performance.

Optimized search for List Management Service

We have optimized the List Management Plugin with faster search results when finding events with free text search and detecting license plates.

MS SQL 2022 Integration

The Mirasys VMS Complete Installer now includes MS SQL and SQL Management Studio 2022. When upgrading an existing installation to V9.9.0 using the complete installer, the current MS SQL version will be updated to MS SQL 2022. However, Mirasys VMS remains compatible with earlier versions of MS SQL as before.

You should not upgrade the MS SQL to the 2022 version unless you meet the following hardware and software requirements.

Support for Axis TU9001 Control board

We have added support and default configuration for the Axis TU9001 Control board.

Driver improvements
VivotekIPCapture Driver

The VivotekIPCapture Driver has been updated with the following feature:

CCFiA/CCRiA

Multi-streaming

Secure connection

50/60fps support

EHIIPCapture Driver
Bi-directional driving data

The EHIIPCapture Driver has been updated to correctly manage vehicle driving bi-directional metadata from the Hikvision H8 model camera.

In System Manager > Camera Settings > Advanced, you can now choose to receive data from license plates in only one direction or in both directions.

If the “Both” direction option is selected (this is the default setting), the system will operate as it currently does, sending all license plate data to the recorder without filtering. If the “Forward” or “Backward” direction option is selected, the driver will filter the license plate data and send to the recorder only those plates captured in the specified direction.

ANPR Smart LPR country detection

When using the Hikvision ANPR camera, the country where the vehicle is registered is now displayed in the Smart LPR plugin using the ISO 3166-1 alpha-2 country codes.

Camera edge storage option

The NewAxisIPCapture driver has been updated to make the AXIS P4707-PLVE Panoramic Camera Edge storage option available in System Manager.

Are You Using any of our EOL Drivers?

If you are using any of the drivers that have reached End of Life (EOL), please contact our support team. Please see the complete list of EOL Drivers here.

It is important for us to understand if these drivers are still in use before they reach End of Support (EOS). Please see Mirasys Policy on EOL/EOS here.

Your feedback will help determine whether these drivers need to be maintained longer or can be phased out entirely.

Thank you.

We have moved our EOL Drivers to Extranet

In V9.9.0, we are making an important change regarding how End of Life (EOL) drivers are distributed: Only drivers that have reached EOL have been moved to our Extranet and removed from the standard installation package. This change helps us streamline the installation process while still making EOL drivers available for our customers who need them. Please see the complete list of EOL Drivers here.

Where to Find the EOL Drivers

If you are using any EOL drivers, they are now available for download on our Extranet. You can access and install only the specific drivers your system requires. Please note that these drivers will not be included in the default installation package moving forward.

Installing an external Driver package

Please see our documentation on how to install an external Driver package here.

Why Are We Making This Change?

By removing EOL drivers from the installation package, we reduce its size and focus the installation on current, fully supported drivers.

We fully prioritize the development and support of current drivers.

You still have access to EOL drivers if needed, but you can choose only those relevant to your system.

Please see Mirasys Policy on EOL/EOS here.

Fixes
Spotter

Smart Search Identity list combo box selection displays identity correctly after selecting identity and deselecting the combo box.

Spotter cameras work as intended, including in rare cases during which the Intel codec did not recover from decoding errors.

Messages in the Spotter info list are displayed correctly after the SMServer reconnects and is currently logged in Operator changes.

Alarm activity calculation is disabled when the timeline is not visible in Spotter.

Spotter works as intended when changing the main license.

Camera activity search works as intended.

The List Management plugin supports names with the letters Ä and Ö.

Spotter log should not contain unreasonable errors and exceptions.

Closing Spotter works as intended.

Spotter memory usage is optimized when using big profiles.

The 2FA authenticator application shows the correct name for the authentication account.

Smart Search and Smart Recognition plugins in Spotter recover as intended when the AI Services have been restarted.

Smart Search works as intended when services are shut down while a search is active.

Spotter closes alarm activity collection correctly on shutdown.

Spotter Web

Client connection is cleaned up correctly when the session has expired.

Security updates.

System Manager

All invalid audio capture devices (out of channel range) will automatically be removed from the VMS, and no error will occur in Hardware Settings after the license update.

Login works as intended after closing and restarting the System Manager and selecting “kick off user.”

Settings export uses the correct time format.

Keyboard shortcuts are disabled for the audit trail combobox control.

Profile loading works as intended when the system data is updated.

A VMS server upgrade from the System Manager application is not possible if the installation file version is higher than the master server version.

Local recorder status is updated correctly during restore.

The upgrade progress (the file transferring progress) in the VMS server update is always positive and within the 0-100% boundary.

The 2FA authenticator application shows the correct name for the authentication account.

The Camera engine settings are working as intended, independently from the RTSP settings.

CSV export works as intended when the recorder has a large number of cameras configured.

VMS Server

SMServer connection works as intended after a new camera is added to Object Recognition.

System

For new installations, we have changed the port range to 10001-10999 for camera communication and streaming in the recorder.
Please note that the old port range, starting from port 8000, will continue to be used in existing installations.

Log information related to material copy across copy types has been improved.

Text channels are as intended after the VMS version update.

Failover and failback work as intended:

failback cannot start before the failover has finished

the correct VMS server settings are used in failover and fallback operations

The failover log event mechanism, which causes the “SMServer” service to overload and increase the number of threads, is working as intended.

Recorder upgrade works as intended when upgraded from V9.9.0 to newer version, and the machine reboot is required.

Clients do not disconnect from the main server when there is no connection to a VMS server.

Spotter in offline mode shouldn’t try to load external control device drivers.

User, user group, and profile data saving works as intended in System Manager after the system data has been updated.

The SMServer service shutdown takes reasonable time (depending on the number of connected clients and VMS servers in the system), and there are no unexpected errors related to alarm searches.

Alarm email image attachments works as intended when the VMS server is using HTTPS.

SM configuration file has been updated to handle the correct reference to EntityFramework assembly.

Failover triggering on VMS Server disk failure in the SMServer works as intended.

Face Recognition (FR), License Plate Recognition (LPR), List Management (LM)

The AI services select TCP or UDP protocol for secured streaming. The System Manager settings for RTSP show an error when secure streaming settings are saved without a certificate.

Storage Locker

It is not possible to export data to the same Storage locker folder.

Drivers
OnvifIPCapture

Milesight camera edge storage works as intended with OnvifIPCapture Driver V1.9.6.0. and the latest Milesight firmware.

Log spamming was reduced from the ONVIF driver.

VideoDefaultSettings, VideoMainStream, VideoAdditionalStreams, Digital IOs, and Edge storage work as intended for i-Pro WV-S22700-V2L. Video Change Settings in Alarm and Device Motion Detection work as intended for live streaming.

Moxa PTZ

Stop commands for moving and zooming are working as intended.

The Moxa PTZ driver sends the movement command according to user actions in the Spotter.

Users can add, delete, and move to prepositions, presets are displayed correctly in the Spotter, and the Moxa PTZ driver sends correct commands.

You can download the release notes as a PDF file here V9.9.0 Release Notes.pdf .

Pagination
Next page
What's new in V9.8.0