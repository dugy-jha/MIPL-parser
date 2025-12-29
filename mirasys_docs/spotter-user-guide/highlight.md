# Highlight | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/highlight

Highlight

The metadata objects for LPR and FR events contain bounding box elements and labels (identity name in FR metadata and license plate number in case of LPR metadata). These bounding boxes and labels can be displayed in the Spotter application if the VCA visualization plugin is enabled and the user selects to show VCA in the video view control panel.

VCA visualization requirements

Spotter needs to get metadata to visualize objects.

The license must have VCA channels.

VCA must be enabled for the camera in System Manager settings or license plate recognition or face recognition needs to be used

The database must be installed (for metadata playback)

For best results, hermeneutic motion detection should be used

Both VCA Core and Mirasys metadata can be used, although there can be some differences in how objects are detected

​​​Visualization

Highlight moving objects such as cars and walking persons 

Show the track that the object has taken on the camera screen 

Show textual info shows textual info related to the tracked object

Show VCA zones and lines after they have been configured using the VCA configurator

Show a client-only VCA event counter

Reset all counters on a camera screen

VCA visualization can be set on for all cameras from the tab menu

VCA visualization states are kept in memory and stored on a local PC for each user

camera VCA state is remembered so that when the camera is opened, its VCA states are set to ones that were used before

VCA visualization can be set on / off also with AVM

The client-only VCA counters are local to the Spotter application and not integrated into the Mirasys Reporting+ application.They are meant for short term reporting and can be reset by clicking on the counter on the camera screen.

Smart recognition metadata visualization

There are two “Highlight“ menu items for the “license plate” and “face” moving objects visualization (drawing borders and name/license plate number):

Show license plates

Show faces

Smart recognition visualization items

The menu items are enabled only when the camera is configured for any VCA detection.

Settings for VCA visualization in Spotter

The line color can be changed

Line thickness can be changed

Trail maximum length can be changed

The zone color can be changed

​​​Advanced settings

​​In advanced settings, there is a setting to allow VCA for all cameras, even if the VCA is not configured for the camera. This is useful in cases where metadata is received from 3rd party system (for example, from data drivers) that will not use recorder VCA.




Pagination
Previous page
Image Controls
Next page
View