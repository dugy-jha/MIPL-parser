# NewAxisIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newaxisipcapture-installation-and-usage

NewAxisIPCapture installation and usage

The driver uses RTSP/HTTP/HTTPS/RTP/UDP/IP protocols to receive audio and video multicast streams and H.264/MPEG-4 compressed unicast streams. The HTTP protocol is also used for parameter setting/retrieving and audio stream and JPEG video stream receiving in unicast mode.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP/HTTPS ports must be
opened:

HTTP: The default port is 80,

HTTPS: The default port is 443,

RTSP: The default port is 554,

UDP: Two sequential ports per video stream are needed in the port range 3556 to 4556. If Multicast mode is enabled, two additional sequential ports per audio/video stream should be opened according to the device configuration.

For example, if there are 4 IP cameras in a DVMS, ports 3556, 3557, 3558, 3559, 3560, 3561, 3562, and 3563 will be used. If a port is not free, it will be skipped. The 1024-1025 and 1028-1029 ports should also be opened in addition to the 3556-4556 range if the device is used in Multicast mode and it is configured to use 1024 port for the audio stream and 1028 port for a video stream.

The driver may be configured using an XML configuration file to enable the following functionality if the Axis IP device supports this functionality:

Multicast audio/video capture

Axis Views

If you use Axis LPR and have several network adapters, you need to set the correct IP address (addresses) in the configuration file.

Limitations

For HTTPS (TLS) support, you need to generate and install the CA certificate on the PC certificate store and generate a certificate for each camera using a guide from Axis ("HowTo. AXIS Device Manager. HTTPS certificate management").

The AXIS driver doesn't support the "PTZ Control Queue" option. If this option is enabled, the AXIS device will be detected as non-PTZ.

Privacy zones may be shifted by a few pixels from the rectangle applied in DVMS. The shift depends on image rotation and mirror settings (shifted to the right for a normal image). This is a camera firmware feature.

If the "Aspect ratio correction" option is enabled on the Axis device, the real image resolution may differ from that in VMS. For example, the real resolution will be 768x576 for the 704x576 setting or 192x144 for the 176x144 setting. Please disable this option if your system does not require aspect ratio correction.

If the network connection is lost, Axis cameras of the P33 Series send a few seconds of video and then don't send anything for 5-10 seconds after the connection is recovered. This behavior is caused by the camera's DHCP implementation. Please use a static IP address to avoid this behavior.

The IP device should be configured manually in the following way in case you want to use the Edge storage feature:

It is not possible to receive Coordinated Universal Time (UTC) from the camera, so the time zone should be set to "GMT+0:00." The daylight saving time option should also be switched off. 

Camera events should be configured for video recording according to user preferences. The event duration should be at least 3 seconds.

It is recommended that automatic SD cleaning be used to have the required space for video recordings.

The video recordings on the camera's storage may contain gaps of up to 10-15 seconds. This is a camera feature, so please do not use maximal settings for video recording to avoid such gaps.

Axis multi-view cameras (e.g., M3007) can be configured to receive video from a specific stream using the XML configuration file. Different views have different capabilities, so the camera should be re-subscribed to VMS to take changed StreamConfiguration options into use.

Privacy zones functionality can be used if the recording channel uses the "Overview" fish-eye view.

Other views don't support privacy masking functionality because these views are parts of the "Overview" view.

Multicast capture limitations

Axis IP devices support multicast capture with Stream Profiles feature support (devices with firmware versions 5.0 or higher) and can be configured via XML file. Older devices will always use unicast streaming.

The Stream Profiles support may be checked via the Web interface: the section "Video & Audio >> Stream Profiles" should be available. The user may use any existing profile for multicast streaming configuration or allow the system to create a new one. Please see the "MulticastProfiles" section in the XML configuration file for more details.

Please do not use the same stream profile for different streams - it may cause conflicts during the video settings application.

Multicast capture can be enabled via XML configuration file using the StreamingMode option. This option is read on stream startup, so a refresh of device settings will be enough to take the changed StreamingMode option into use. Please note that DVMS has optimization for channel restarting since version 7.4.1, so in this case, it will be required to change one of the video options for each camera to restart the stream.

The driver instance can be configured to be used as a Primary or Listener. The primary instance is able to change IP device settings and use additional functionality. Listener instances are able to receive video streams and audio streams by multicast and allow the use of digital I/O functionality.

The Listener recorder will not change any configuration on the camera side. For example, if no configured profile is available on camera, it will not be created, and the driver will not be able to receive the video. The camera should be added to the Primary recorder before using it in the Listener configuration. 

The additional streams (Live and Remote) are active in case they are opened in clients only. So, to use updated Multiple Streaming settings, you must start (or keep open) these streams for the Primary recorder after the stream settings have been changed in DVMS. Otherwise, the camera cannot use the latest stream settings.

Motion Detection and Change option in alarm features (CFiA/CRiA) cannot be used in multicast mode because of timeout issues specified above.

Users should guarantee that only one recorder will change the settings of Axis IP devices. Other recorders which use this camera should be in listener mode. 

The Axis cameras may not support more than one multicast stream in case if camera is configured to use specific port for multicasting (non-zero "Video port" setting in  "System Options >> Network >> RTP" group). The camera will return RTSP 461 "Unsupported transport" error for stream start attempt if one multicast stream is already started. Please configure automatic port selection (set "Video port" setting to 0) to avoid this behavior.

It is recommended to specify IP address of the network adapter through which camera is connected to receive multicast streaming correctly in case if more than one network adapter is available.

Each Unicode character is stored as symbol code (%u0227, for example) and required 6 bytes for it. So, length of Unicode preposition name may be limited by 11 symbols instead of 64.

Axis P1428-E camera supports only 2 4K (3840x2160) streams at the same time. Please avoid using of 4K resolution for all streams in multiple streaming feature and minimize amount of rules which use 4K resolution for recording to SD card.

The driver allows to switch control mode between "Active" and "Passive" since version 2.5.5.0. In "Passive" mode the driver will not change any video-related parameters, so in this mode the following functionality will not work:

Privacy zones configuring

Change options in alarm (i.e. CFiA/CRiA features)

If the camera accepts video parameters via RTSP or HTTP stream URI, the driver will start stream without them. In other words, the stream settings applied via Web-interface will be used.

Applying of privacy masks may take long time (creation of every zone may take up to one second), so it may slow down stream startup. To speed up video subscribing the driver applies privacy masks after video stream startup.

The driver versions before 2.5.7.0 has an issue with privacy masks creation for multiple-sensor devices. The driver always used template for first channel, so privacy zones might displayed incorrectly (for example, displayed on wrong channel).

Please remove privacy zones manually via Web-interface or just reset device to factory defaults in case if you'll meet such behavior. After this driver will create privacy masks using correct templates on next video channel start.

The Axis Zipstream technology (<http://www.axis.com/global/en/technologies/zipstream)> may be used with the driver. The driver has no option for configuring of this feature, so it should be enabled manually via Web-interface.

Please note that:

The changes of video settings (including Axis Zipstream options) made via Web-interface will affect to the video streams started after the changes. So, it will be required to restart video stream to take the updated settings into use.

The VMS software required to receive one intra-frame per second to perform post-processing of video stream (VCA, motion detection, etc.). Using of "Dynamic GOP" option may cause a problems with post-processing, so using of this option is not recommended.

The Windows XP is not supported since driver version 2.5.0.0

The new Axis cameras (firmware 5.50 and newer) uses new API for Motion Detection that currently does not supported by the driver. The VMD feature will be disabled for these cameras until new API support will be added to the driver.

Native Axis Licence plate recognition application uses HTTP POST requests to send ANPR data. So, the driver starts the HTTP server to receive those HTTP POST messages. If the PC has more than one  network adapter, you need to set correct IP address of the network adapter that is used to communicate with camera to driver's XML file, AxisANPR/NetworkInterface parameter. In other cases, the camera will not send ANPR data to the PC. If Failover is used, it is required to set both addresses - master server and failover.

Axis changed date.cgi API to time.cgi API to set / get time from / to camera. But this new time.cgi API works slowly, so the driver receive time from camera with some delay. Also, time.cgi still does not have miliseconds, so this time sync is not precise. The Driver tries to calculate time difference between camera and PC with Recorder, but this calcultion is not presice enough. This calculation can be switched off in config file in case if time is synced outside of VMS.




Pagination
Previous page
NewArecontIPCapture installation and usage
Next page
NewBoschIPCapture installation and usage