# VMS Performance Counters | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/vms-performance-counters

VMS Performance Counters
How to enable Performance Counters
VMS Recorder

Open System Manager

Double click server Diagnostic

Go to Camera load -tab

Click refresh-button to enable VMS Recorder counters

Or you can make this via DVRServer.exe.config

Stop DVRServer using Windows Services application

Go to DVR Server installation folder

Default installation folder C:\Program Files\DVMS\DVR

Open DVRServer.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save DVRServer.exe.config file

Start DVRServer using Windows Services application

SM Server

Stop SMServer using Windows Services application

Go to SM Server installation folder

Default installation folder C:\Program Files\DVMS\SystemManagement

Open SMServer.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save SMServer.exe.config file

Start SMServer using Windows Services application

System Manager

Go to C:\Users\%username%\AppData\Roaming\DVMS\systemmanager\9.6.1\127.0.0.100_5008

9.6.1 → Open that version which System Manager you are using

127.0.0.100_5008 → Open that server folder where System Manager is connected

Open SystemManager.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save SystemManager.exe.config file

Run Spotter using Run As Administrator rights

Spotter

Go to C:\Users\%username%\AppData\Roaming\DVMS\spotter\9.6.1\127.0.0.100_5008

9.6.1 → Open that version which Spotter you are using

127.0.0.100_5008 → Open that server folder where Spotter is connected

Open Spotter.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save Spotter.exe.config file

Run Spotter using Run As Administrator rights

Gateway

Stop DVMSGatewayService using Windows Services application

Go to Gateway installation folder

Default installation folder C:\Program Files\DVMS\Gateway

Open ServiceLauncher.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save ServiceLauncher.exe.config file

Start DVMSGatewayService using Windows Services application

Spotter Web

Create new user which has administrator rights

Example SpotterWebAdmin

Go to Spotter Web installation folder

Default C:\inetpub\SpotterWeb

Open Web.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save Web.config file

Open IIS Manager

Stop SpotterWeb site

Under "Sites" selection, click "SpotterWeb site," and from the menu that opens by right mouse click, select "Manage Website" and click "Stop."

Change the SpotterWeb application pool identity.

Click "Application Pools"

Click "SpotterWeb Site"

Click "Advanced Settings..."

From "Advanced Settings" dialog, select "Identity" and change its value to "LocalSystem" (this will work if the currently logged in user is administrator. Otherwise select custom user account)

Accept the changes

Start SpotterWeb site

Under "Sites" selection, click "SpotterWeb site" and from the menu that opens by right mouse click, select "Manage Website" and click "Start"

Media Exporter

Go to Media Exported folder

Default is same place where is Spotter

Example C:\Users\dvr\AppData\Roaming\DVMS\spotter\9.6.1\127.0.0.100_5008

9.6.1 → Open that version which Spotter you are using

127.0.0.100_5008 → Open that server folder where Spotter is connected

Open MediaExporter.exe.config file in example Notepad++

Find section

<add key="PerformanceMonitoring" value="False" />


Change this to True

<add key="PerformanceMonitoring" value="True" />


Save MediaExporter.exe.config file

How to open Performance Monitor application

Open Performance Monitor application from Windows Start-menu

This open Performance Monitor application

Performance Monitor

When application is open, you can use red X -button remove default Counter

Now you can use green + -button to add wanted VMS Recorder/Spotter Performance Counters and use them to troubleshooting system.

Performance Counters start with DVMS name

Mirasys VMS Performance Counters
VMS Recorder

VMS Video Processing

Use table header to sort columns

Counter name

	

Description




Realtime items to be sent to clients / sec

	

How many realtime items are added to network send queue (potentially send to network)




Realtime items skipped from client send / sec

	

How many realtime items are skipped from network send queue




Recording video frames captured / sec

	

Number of frames captured in a second for Recording channel




Live video frames captured / sec

	

Number of frames captured in a second for Live channel




Remote video frames captured / sec

	

Number of frames captured in a second for Remote channel




Video frames recorded to file system / sec

	

Number of frames actually recorded in a second




Video frame queue size

	

Amount of frames waiting in processing queue




Average video frame processing time (msec)

	

Average processing time of captured video frames. Measured in milliseconds




Average video frame interval (ms)

	

The average interval between captured video frames. Measured in milliseconds. This counter was added to 7.0 version.




Average video frame size

	

The average size of captured video frames. Measured in bytes.




Video cache flush interval

	

Interval between filesystem video frame cache flushes. Measured in milliseconds




Average video frame decompression time (msec)

	

Average decompression time of captured video frames. Measured in milliseconds




Average video frame resize time (msec)

	

Average resize time of captured video frames. Measured in milliseconds




Average video frame compression time (msec)

	

Average compression time of captured video frames. Measured in milliseconds




Metadata conversion time (msec)

	

How many milliseconds did it take to convert metadata to Mirasys metadata format




Meta data write time (msec)

	

How many milliseconds did it take to write metadata to database




Meta data deletion time (msec)

	

How many milliseconds did it take to delete fixed number (10 or 15) of rows from metadata database




Plate number detection time (msec)

	

How many milliseconds did it take to perform plate number detection




Video content analysis time (msec)

	

How many milliseconds did it take to perform video content analysis

DVMS Memory Management

Use table header to sort columns

Counter name

	

Description




Memory: buffers in use

	

Amount of memory buffers allocated and in use




Memory: Memory buffer allocations / sec

	

How many memory buffers were allocated in a second




Memory: buffers not in use

	

Amount of memory buffers allocated but not in use




Memory: Number of free memory

	

Number of free memory




Memory: free

	

Memory free




Memory: Number of used memory

	

Number of used memory




Memory: used

	

Memory used




Memory: unusable

	

Memory unusable




Memory: Number of managed memory buffers in use

	

How many managed memory buffers are currently in use




Memory: Number of available managed memory buffers

	

How many managed memory buffers are currently in reserve




Memory: Number of buffers allocated / second

	

Number of buffers allocated per second.




Memory: Number of buffers freed / second

	

Number of buffers freed per second.




Memory: Number of free memory pages

	

Number of free memory pages.




Memory: Number of free memory segments

	

Number of free memory segments.




Memory: Amount of free page memory

	

Amount of free page memory.




Memory: Amount of free segment memory

	

Amount of free segment memory.




Memory: Number of used memory pages

	

Number of used memory pages.




Memory: Number of used memory segments

	

Number of used memory segments.




Memory: Amount of used page memory

	

Amount of used page memory.




Memory: Amount of used segment memory

	

Amount of used segment memory.




Memory: Amount of unusable page memory

	

Amount of unusable page memory.




Memory: Amount of unusable segment memory

	

Amount of unusable segment memory.




Memory: Amount of total used memory

	

Amount of total used memory.

DVMS File storage

Use table header to sort columns

Counter name

	

Description




File Storage load MB / sec

	

Amount of written data in Mb per second

SM Server

Average Count of Recorder Events

Counter name

	

Description




ClientDroppedEvent events / second

	

Number of dropped client events per second.




ClientRegisteredEvent events / second

	

Number of registered client events per second.




DVMSLicenseEvent events / second

	

Number of DVMS license events per second.




DvrAlarmEvent events / second

	

Number of DVR alarm events per second.




DvrArchiveFailedEvent events / second

	

Number of failed DVR archive events per second.




DvrCameraSignalStateEvent events / second

	

Number of DVR camera signal state events per second.




DVRDataSignalStateEvent events / second

	

Number of DVR data signal state events per second.




DvrDigitalIOEvent events / second

	

Number of DVR digital I/O events per second.




DvrDomeEvent events / second

	

Number of DVR dome camera events per second.




DvrFileSystemAllDisksFailedEvent events / second

	

Number of all disks failed events per second.




DvrFileSystemDiskFailureEvent events / second

	

Number of disk failure events per second.




DvrFileSystemDiskFailureRecoveryEvent events / second

	

Number of disk failure recovery events per second.




DvrFileSystemInitializedEvent events / second

	

Number of initialized File system events per second.




DvrFileSystemLoadAudioAlarmChannelEvent events / second

	

Number of load audio alarm channel events per second.




DvrFileSystemLoadAudioChannelEvent events / second

	

Number of load audio channel events per second.




DvrFileSystemLoadVideoAlarmChannelEvent events / second

	

Number of load video alarm channel events per second.




DvrFileSystemLoadVideoChannelEvent events / second

	

Number of load video channel events per second.




DvrInsufficientDiskSpaceEvent events / second

	

Number of insufficient disk space events per second.




DVRKeepAlive events / second

	

Number of DVR keep alive events per second.




DvrLicenseUpdatedEvent events / second

	

Number of updated DVR license events per second.




DvrMapNetworkDirectoryFailure events / second

	

Number of map network directory failure events per second.




DvrMotionEvent events / second

	

Number of motion events per second.




DvrSettingsUpdatedEvent events / second

	

Number of updated settings events per second.




DvrSMServerConnectionEvent events / second

	

Number of SM server connection events per second.




DvrUpdateSettingsEvent events / second

	

Number of update settings events per second.




DvrVideoOutBaseEvent events / second

	

Number of video output events per second.




LicenseUpdatedEvent events / second

	

Number of updated license events per second.




ServerCheckFailed events / second

	

Number of failed server check events per second.




SMKeepAlive events / second

	

Number of SM server keep alive events per second.




SMLicenseUpdatedEvent events / second

	

Number of updated SM license events per second.




SystemDataUpdatedEvent events / second

	

Number of updated system data events per second.




UserDataUpdatedEvent events / second

	

Number of updated user data events per second.




WatchdogEvent events / second

	

Number of watchdog events per second.

Average Lifetime of Recorder Events
Use table header to sort columns

Counter name

	

Description




ClientDroppedEvent lifetime in ms

	

Average lifetime of dropped client events in milliseconds.




ClientRegisteredEvent lifetime in ms

	

Average lifetime of registered client events in milliseconds.




DVMSLicenseEvent lifetime in ms

	

Average lifetime of DVMS license events in milliseconds.




DvrAlarmEvent lifetime in ms

	

Average lifetime of DVR alarm events in milliseconds.




DvrArchiveFailedEvent lifetime in ms

	

Average lifetime of failed DVR archive events in milliseconds.




DvrCameraSignalStateEvent lifetime in ms

	

Average lifetime of DVR camera signal state events in milliseconds.




DVRDataSignalStateEvent lifetime in ms

	

Average lifetime of DVR data signal state events in milliseconds.




DvrDigitalIOEvent lifetime in ms

	

Average lifetime of DVR digital I/O events in milliseconds.




DvrDomeEvent lifetime in ms

	

Average lifetime of DVR dome camera events in milliseconds.




DvrFileSystemAllDisksFailedEvent lifetime in ms

	

Average lifetime of all disks failed events in milliseconds.




DvrFileSystemDiskFailureEvent lifetime in ms

	

Average lifetime of disk failure events in milliseconds.




DvrFileSystemDiskFailureRecoveryEvent lifetime in ms

	

Average lifetime of disk failure recovery events in milliseconds.




DvrFileSystemInitializedEvent lifetime in ms

	

Average lifetime of initialized File system events in milliseconds.




DvrFileSystemLoadAudioAlarmChannelEvent lifetime in ms

	

Average lifetime of load audio alarm channel events in milliseconds.




DvrFileSystemLoadAudioChannelEvent lifetime in ms

	

Average lifetime of load audio channel events in milliseconds.




DvrFileSystemLoadVideoAlarmChannelEvent lifetime in ms

	

Average lifetime of load video alarm channel events in milliseconds.




DvrFileSystemLoadVideoChannelEvent lifetime in ms

	

Average lifetime of load video channel events in milliseconds.




DvrInsufficientDiskSpaceEvent lifetime in ms

	

Average lifetime of insufficient disk space events in milliseconds.




DVRKeepAlive lifetime in ms

	

Average lifetime of DVR keep alive events in milliseconds.




DvrLicenseUpdatedEvent lifetime in ms

	

Average lifetime of updated DVR license events in milliseconds.




DvrMapNetworkDirectoryFailure lifetime in ms

	

Average lifetime of map network directory failure events in milliseconds.




DvrMotionEvent lifetime in ms

	

Average lifetime of motion events in milliseconds.




DvrSettingsUpdatedEvent lifetime in ms

	

Average lifetime of updated settings events in milliseconds.




DvrSMServerConnectionEvent lifetime in ms

	

Average lifetime of SM server connection events in milliseconds.




DvrUpdateSettingsEvent lifetime in ms

	

Average lifetime of update settings events in milliseconds.




DvrVideoOutBaseEvent lifetime in ms

	

Average lifetime of video output events in milliseconds.




LicenseUpdatedEvent lifetime in ms

	

Average lifetime of updated license events in milliseconds.




ServerCheckFailed lifetime in ms

	

Average lifetime of failed server check events in milliseconds.




SMKeepAlive lifetime in ms

	

Average lifetime of SM server keep alive events in milliseconds.




SMLicenseUpdatedEvent lifetime in ms

	

Average lifetime of updated SM license events in milliseconds.




SystemDataUpdatedEvent lifetime in ms

	

Average lifetime of updated system data events in milliseconds.




UserDataUpdatedEvent lifetime in ms

	

Average lifetime of updated user data events in milliseconds.




WatchdogEvent lifetime in ms

	

Average lifetime of watchdog events in milliseconds.

SMServer Internal Queues

Use table header to sort columns

Counter name

	

Description




Total number of events in recorder queues

	

Total number of events in recorder queues.




Total number of events in client queue

	

Total number of events in client queue.

System Manager
Use table header to sort columns

Counter name

	

Description




Number of buffers in use

	

How many memory buffers are currently in use.




Number of available buffers

	

How many memory buffers are currently in reserve.

Spotter
Use table header to sort columns

Counter name

	

Description




Number of realtime video images / second received from network

	

Number of realtime video images received from network per second




Number of realtime video images / second skipped before decompression

	

Number of realtime video images skipped right after receiving them from network




Number of realtime video images / second decompressed

	

Number of realtime video images decompressed per second




Number of realtime video images / second operated

	

Number of realtime video images decoded and resized per second




Total number of realtime video images / second sent to screen

	

Number of realtime video images sent to UI per second




Video image decompression time (ms)

	

Average video image decompression time in milliseconds




Video image operations time (ms)

	

Average video image decoding and resizing time in milliseconds




Number of playback video images / second received from network

	

Number of playback video images received from network per second




Number of playback video images / second decompressed

	

Number of playback video images decompressed per second




UI: Number of images received / second

	

Number of video images received in UI per second




UI: Number of images skipped / second

	

Number of video images skipped in UI per second




UI: Number of images received in UI thread / second

	

Number of video images received in UI thread per second




UI: Number of images written to surface / second

	

Number of video images written to display surface per second




UI: Image surface write time (ms)

	

Average image surface write time in milliseconds




UI: Off-screen drawings / second

	

Number of video drawings to back buffer per seconds




UI: Off-screen draw time (ms

	

Average back buffer draw time in milliseconds




UI: Video renderings / second

	

Number of video renderings per second




UI: Video rendering time (ms)

	

Average video rendering time in milliseconds

Gateway

General

Use table header to sort columns

Counter name

	

Description




Number of active user sessions

	

The number of active Gateway sessions




Number of image conversions / second

	

The number of images converted to JPEG.




Number of images sent over the network / second

	

The number of JPEG images sent to all clients

Realtime video streaming

Use table header to sort columns

Counter name

	

Description




Realtime video streaming

	







Image realtime stream count

	

The number of realtime video streams opened in the Gateway.




Image realtime stream on skipping state count

	

The number of realtime video streams that are currently skipping images.




Number of images received from network / second

	

The number of realtime images received by the Gateway from the recorders.




Number of images received and skipped from network / second

	

The number of realtime images received and skipped by the Gateway.

Memory

Use table header to sort columns

Counter name

	

Description




Number of buffers in use

	

How many memory buffers are currently in use.




Number of available buffers

	

How many memory buffers are currently in reserve.

Media Exporter
Use table header to sort columns

Counter name

	

Description




Number of exported video samples / second

	

How many images were exported in a second.




Video sample write time in seconds

	

How many seconds did it take to write an image to a media file.




Video sample conversion time in seconds

	

How many seconds did it take to convert an image to write format.




Number of exported audio samples / second

	

How many audio samples were exported in a second.




Audio sample write time in seconds

	

How many seconds did it take to write an audio sample to a media file.




Number of exported text samples / second

	

How many text samples were exported in a second.




Text sample write time in seconds

	

How many seconds did it take to write a text sample to a media file.




Input queue count

	

How many items are in a queue waiting to be written to a media file.




Input queue data size MB

	

How much memory (MB) is used for input queue items.

Pagination
Previous page
Device Compatibility Tool
Next page
List Management Service update from 9.6.1 to 9.6.2 fails