# Mirasys VMS V9.9.6 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/mirasys-vms-v9-9-6-release-notes

Mirasys VMS V9.9.6 release notes
Release date: 7.11.2025
System

The failover network timeout adjustment works as intended with the added timeout options.

Freeing event handlers on clients works as intended.

Parsing of VMS server settings is optimized on clients.

Reconnection to the main server works as intended.

System Management Service

SMServer API calls can’t be authenticated with a disabled user’s credentials.

The SMServer can recover the VMS server connection if the VMS server settings in the data cache are corrupted.

Settings backup works as intended with a high number of files.

Clients get the latest camera information when they connect to the main server.

VMS Service

The stream passed to the VCA engine is passed in the correct resolution.

The text channel event names are displayed correctly.

Storing the pre-recording data works as intended in case of an unexpected shutdown.

The VMS server handles the audio capture settings as intended.

The VMS Server works as intended when a new version of the driver is installed.

The file system file creation was updated to use all sub-channels in the file count calculation.

The ‘Removed’ VCA trigger can be used as an alarm trigger.

The NOT operator is used correctly with VCA events.

Adding and removing cameras doesn’t affect the other configured cameras.

Export Service

The Export Service ignores incorrect export tasks.

System Manager

Handling the connection loss to the main server while approving the EULA works as intended.

The opened settings item is highlighted in the System Manager system, recorder, profile, and user tab tree component.

The Spotter role for showing failover events displays the default state correctly.

All settings dialogs can be opened using drag-and-drop.

The virtual memory usage is displayed correctly in the VMS server diagnostics.

Cancelling the identity import and export works as intended.

The identity list is imported correctly when the same list already exists in the List Management settings.

The VMS settings can be opened if the MIA SDK parameters are missing from the XML configuration.

Connections to the VMS servers are displayed correctly after a VMS server address has been changed.

The identity export progress dialog works as intended, so that the export can be canceled by the user.

The identity modification dialog is not opened when the user clicks on the list header.

The sorting of identities works as intended in the List Management settings.

Selecting multiple client plugins in the profile settings works as intended.

Exporting reports to PDF format in the Audit Trail search works as intended with all languages.

Spotter

The latest Spotter Player version is copied with export.

The spacing in the menu controls is set correctly.

Sharing tab contents, layouts, and bookmarks with other users works as intended.

The dropdown lists in the Smart Search show the content as intended.

Opening alarms for viewing from the alarm list works as intended.

Grid layout calculation works as intended with all resolutions.

Spotter playback works as intended.

Identities loading is optimized in Smart List Management.

The Spotter profile tree is updated correctly after the settings restore.

Exporting reports to PDF format in the Camera Audit, Incident Reporting, and Smart Search works as intended with all languages.

Taking camera PTZ control works as intended when the camera is in a connection-establishing or disconnected state.

Failover, failback, and failover material copy events are shown as intended in the information list.

The correct status of the camera is displayed in the profile tree and video window after the settings update.

Gateway

Gateway handles alarms as intended.

Alarm manager is cleaned up as intended in the Gateway service.

Gateway SDK

The Gateway sample application functions as intended in the event of a main server connection loss.

Drivers
ONVIFIPCapture 1.9.19.0

The alarm created by a specific camera trigger is created only for events from this particular camera.

In case a camera sends invalid frame rate capabilities, the ONVIF driver uses its own maximum frame rate capability.

The initial states of inputs and outputs are shown correctly in the Spotter.

ONVIF events with empty data items are processed correctly.

NewBoschIPCapture 18.0.0

Bosch camera driver returns the correct firmware version information.

The RTP over HTTP for audio works as intended with the Bosch camera driver.

EHIIPCapture 2.1.21.0

The VMS server startup works as intended if the Hikvision camera is offline.

EasyLPR works as intended with the Hikvision camera.




You can download the release notes as a PDF file here: Mirasys VMS V9.9.6 Release Notes.pdf

Pagination
Next page
Mirasys VMS V9.9.5 release notes