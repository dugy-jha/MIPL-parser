# NewSamsungIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newsamsungipcapture-installation-and-usage

NewSamsungIPCapture installation and usage

In all compression modes, the driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP/HTTPS protocols is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following ports must be opened:

HTTP: default port is 80,

HTTPS: default port is 443,

RTSP: port 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

For example: if there are 4 Samsung IP cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

NewSamsungIPCapture.xml file is used for:

Configuration of driver behaviour:

Unicast

Multicast:Primary

Multicast:Listener

Video channels settings:

Video channel protocol (RTP over UDP, RTP over RTSP)

Bitrate mode (CBR/VBR)

Limitations

The capabilities of Samsung cameras cannot be retrieved for earlier firmware versions. All camera capabilities (excluding camera model name) for these cameras are hard-coded into the driver. So, all cameras should be updated to the latest firmware version.

Samsung cameras do not support configuring of inputs using CGI commands. Input configured as "disabled" by default. Please set input configuration to "NO" (i.e. "Normal Open") in the web-interface before adding the camera to the VMS.

Samsung camera frame rates may differ from settings (+/- 3 fps) 

Driver stores preset names in XML file (Unicode names are supported)

The Samsung PTZ devices do not support speed parameter for "move to preset" command. So, move-to-preset speed will always be the same.

Samsung cameras apply each privacy zone configuration by separate request (add/remove). For modifying of zone position we should remove previous configuration and add new position by different requests. Each add/remove request is processed by the camera during 0.6 - 0.8 second. So, updating of positions of 10 privacy zones may takes up 16 seconds.

Time-zones for discontinued cameras may be set incorrectly during time synchronization.

The IP device should be configured by user manually in the following way in case is user want to use Edge storage feature:

There is no possibility to know is any file is writing at the moment. So please do not set Post-Alarm duration option to long timeouts - it may case skipping of this interval by the driver.

It is recommended to switch off "Record 1 fps forcibly" option. However, this option may be disabled for some settings of recorded profile (please refer to camera's manual for details). You can use separate video profile for recording video for HD and Full-HD cameras in this case.

It is recommended to use automatic SD cleaning to have a required space for video recordings.

Samsung cameras of 7000 series have an issue with recording of video data by event. The camera doesn't record anything however events configured for recording were signaled. The camera starts writing of video after rebooting or sometimes after resetting camera's settings to factory default. This is camera issue.

Old Samsung camera models like SNP-570 and SND-460 which uses STW SDK (STW cameras in next notes) with firmware version prior than 1.3.5 do not support retrieving camera properties. These cameras will be detected as "Samsung IP Camera" and will work in PAL video mode only.

Samsung STW cameras don't support "switch output off" command. Outputs will be switched off automatically by camera according to output settings in Web-interface.

Samsung STW cameras send MPEG-4 stream with 12.5 FPS for 10 and 15 FPS settings.

Samsung STW cameras decrease video quality value for MPEG-4 codec automatically during moving. This is camera feature (according to information from Samsung Techwin Support).

Frame rate has fluctuations in MPEG-4 compression mode for Samsung STW cameras. This caused by receiving RTP packets with incorrect sequence number. This is camera problem.

A video stream from Samsung STW cameras has FPS fluctuation if exposure settings for camera are invalid. To correct the settings, use the "Camera Setup" button on Live View page in Web-interface. 

Samsung STW cameras take disabled state (returns HTTP responses with status code 500 for all requests) after the connection was lost for a short time and then recovered. The problem is reproduced with 30% probability for MJPEG codec only.

FPS settings are applied incorrectly for MJPEG video stream. This camera problem is actual for Samsung STW cameras with firmware version 1.3.5 or previous. So, real FPS for MJPEG video stream may be lower than required.

MJPEG stream stops after a long working time (for example, during overnight tests). This is because camera returns HTTP responses with status code 500 for all requests. In this case camera should be rebooted manually. This issue is actual for Samsung STW cameras.

SNP-1000A camera sends MJPEG stream with 8-9 FPS for 10 FPS and D1 resolution settings. This is firmware problem.

SNP-1000A camera stops processing HTTP requests after losing and restoring network connection (for example, after "No signal" during 2 minutes). This is because camera returns HTTP responses with status code 403 for all requests. In this case camera should be rebooted manually.

SNP-1000A and SNC-550 cameras do not support MPEG-4 RTP services. Only MJPEG video stream is available for these cameras.

SNP-1000A camera pans between 0 degree and 350 degrees. Degree values between 351 and 359 are not available - this is camera feature.

SNP-1000A camera does not support continuous move commands. The driver implements emulation of continuous moving mechanism. This mechanism reduces to following issues:

Camera moving will be discrete.

MJPEG stream sometimes stops for a few second during camera moving with highest speed. Probably, camera firmware isn't able to process video stream and a lot of moving commands at the same time.

Incorrect camera moving in bottom position when try moving down. The camera inverts vertical scale and moves up if command "move down" is received and camera passes through bottom position. But next” move down" command will not be inverted and camera will move to bottom position again.

Preposition storing does not work for SNP-1000A camera with current firmware version. Firmware update is required.

The cameras of 7002 series have limitation for number of active profiles. The number of active video streams will be limited by 2 if each of them will use 1024x768 or greater resolution. So, multiple streaming feature may not work correctly for these cameras.

The driver supports G.711 audio encoding only. So G.711 encoding should be selected manually via Web-interface if camera supports more than one audio encodings.

VMS doesn't support privacy zones for PTZ cameras. So, the privacy zone support will be detected if camera doesn't support pan/tilt movement.

Samsung devices with WR3.0 software platform version have an issue in SSL implementation which doesn't allow to use POST commands. As result privacy zones functionality cannot be used when HTTPS support is activated. Samsung promised to fix it in the next firmware release.

Samsung devices with WR3.0 software platform version send video stream with low frame-rate (for example, 2-3 instead of applied 20) in case if audio stream was subscribed before video stream. This behavior is caused by RTSP module implementation on camera side. Please save camera settings again without any change to return the camera to normal streaming mode.

In case of using constant bitrate (CBR) settings for Samsung devices with profile support the VMS quality is converted to bitrate settings as a percentage using the following limits:

2Mbps - 15Mbps     for resolution width 1600px and greater;

1024Kbps - 10Mbps  for resolution width between 1024px and 1600px;

512Kbps - 5Mbps    for resolution width between 640px and 1024px;

64Kbps - 2Mbps     for resolution width lower than 640px.

Correct VMS quality should be set to fit required network bandwidth. Other cameras use standard quality settings, not bitrate.

Bitrate can be limited to 6Mbps in case if video profile configured in Record mode to internal flash card (Edge Storage). The driver will not change GOP size value for video profiles configured in Record mode. To avoid this limitation please configure separate profile for internal recording material using camera's Web Interaface (in the "Video profile" section).

To use VBR with audio and multiple streaming camera should have firmaware 2.x or higher. With old firmware video for multiple streaming will not work.

Multicast is not enabled for Samsung models with old SDK (non-profile cameras). All those models work with Unicast only. Those cameras cannot be used in several VMS instances!

Unicast mode: The driver will change camera settings according to VMS settings and receive audio and video data from the camera using the unicast connection.

Multicast:Primary: The driver will change camera settings according to VMS settings and receive audio and video data from the camera using the multicast connection.

Multicast:Listener: The driver will not change the following camera settings:

Quality

Resolution

Framerate

For Multicast:Listener the following options will be configured in the same way as Multicast:Primary:

Multiple streaming option

Video Codec for all streams

If the camera should be used in several VMS instances, one VMS should be set to Multicast:Primary, and others should be Multicast:Listener.

Several Multicast:Primary configurations or Multicast:Primary and Unicast configurations are not allowed, in other case camera should be overloaded with continious concurrent settings change.

Multicast address and port should be set for each profile on camera's Web interface, or multicast will not work. When multiple streaming is on, driver creates MLIVE profile - multicast address and port should be set to it too.

Area zoom and Centering functionality is available for Samsung cameras with SUN API 2.0 support.

Iris change is slow due to camera limitation). One click - one change.

When the camera is moved (or zoomed) auto iris and auto focus are applied.

To support Audio in Edge Feature VMS version 7.4.3.71 or higer is requred.

The new camera series (like QNO/QNV/QND-7010R samples) have limitations for using of 2 megapixel and greater resolutions for H.264 streams:

Over 2MP resolutions ( 2592x1520 / 2560x1440 / 2304x1296) The maximal frame-rate will be divided between amount of active streams:

20 fps / 2 streams = 10 fps per stream;

20 fps / 3 streams = 6 fps per stream.

One over 2MP stream + 2MP streams:

15 fps per stream for dual streaming configurations (example: 2592x1520 @ 20fps + 1920x1080 @ 20fps)

10 fps per stream for triple streaming configurations (example: 2592x1520 @ 20 fps + 1920x1080 @ 20 fps + 1920x1080 @ 20 fps)

2MP (1920x1080) streams only:

No limitation for 2 streams (20 fps per stream)

15 fps per stream for 3 streams

Changing option by alarm (CCFiA/CCRiA) functionality is available for devices which allows to change options faster than 2 seconds. The devices released before year 2015 do not support this feature.

The Windows XP is not supported since driver version 2.2.18.1




Pagination
Previous page
NewPanasonicIPCapture installation and usage
Next page
NewSiquraIPCapture installation and usage