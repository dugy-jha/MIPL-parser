# WisenetIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/wisenetipcapture-installation-and-usage

WisenetIPCapture installation and usage

In all compression modes driver uses RTSP/HTTP/HTTPS(TLS)/RTP/UDP/IP protocols for video receiving. Also HTTP/HTTPS protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP/HTTPS ports must be opened:

HTTP : default port is 80,

HTTPS: default port is 443,

RTSP: default port is 554,

UDP: two sequential ports (starting from even value) per unicast audio or video stream in a port range 3556 to 4556.

For the communication via HTTPS (TLS) is needed to select RTSP over HTTP transport which siutable as
for HTTP and for HTTPS.

For example, if there are 4 IP cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561,
3562 and 3563 will be used. If a port is not free, the port pair will be skipped.

The multicast streaming also requires two sequential ports per audio or video stream, but the ports numbers depend from device settings or XML configuration.

For example, the device may be configured to send all streams to the single port only. The ports 40000-40001 should be opened in case if 40000 port is specified for this setting.

Limitations

License plate recognition is configured directly in the VaxALPR plugin installed on the camera in accordance with the manual "VaxALPR On-Camera Software. Software Setup and Camera Configuration. Hanwha Manual". There is no possibility to adjust the accuracy of LPR using XML.

It is recommended to use cameras with Whisenet 5 and Wisenet 7 processors for Vaxtor ALPR plugin (VaxALPR).

Regarding the TLS certificate, when RTSP connection over HTTPS (TLS) is made, camera shares its public certificate during Handshake procedure, therefore client need not store or have camera's public certificate.

Do not set a blank username for authorization. If the username is empty then authorization content headers will not be added to the HTTP requests.

The camera may return non-rotated resolution capabilities in case if "Hallway view" option is set to 90 or 270 degrees (like 800x448 option instead of real 448x800 resolution). The stream is received with correct (rotated) resolution in this case.

Privacy masks are applied based on maximum resolution size according to SUNAPI specifications. As result they may do not correspond to displayed positions in case if cropped image or image with different aspect ration is used. This is normal behavior. Please use maximal resolution in System Manager/Spotter Admin applications for privacy mask editing.

Privacy masks may appear and disappear several times for SNB-9000 camera (firmware version 1.02_160215) during applying of configuration by the driver. This is camera-related issue and it was reported to Hanwha Techwin support, however they have no plan to release new firmware version at the moment.

Privacy masks do no supported for PTZ devices since Mirasys VMS has no possibility to setup mask position using spherical coordinates.

The several cameras like PNM-9030V supports privacy masking only for overview channel. The rest channels display part of overview channel and have no possibility to setup own masks.

Since VMS has no possibility to setup capabilities for each video channel separately, all camera channels will have the same (maximal) number of available masks. However, masks will work only for overview channel in this case. Privacy mask settings for other channels will be ignored.

The Wisenet PNM-9030V sample supports privacy masking feature for "Overview" channel only.

The picture for other channels has no privacy masking support. So, all objects covered by masks on "Overview" channel's picture, may be easily seen on the other ones.

This is Hanwha's concept and it's mentioned in camera's specifications.

The SNB-9000 camera (firmware version 1.02_160215) is unable to change codec by SUNAPI call.

This is camera-related issue and it was reported to Hanwha Techwin support, however they have no plan to release new firmware version at the moment.

Please change the codec manually via Web-interface in case if you'll meet problem with video settings applying.

The SNB-9000 camera changes resolution by alarm (CCRiA feature) during 8 seconds. This behavior is caused by several delays on camera side during stream re-subscribing and cannot be improved on driver side. The changing of frame-rate in alarm (CCFiA) takes 2 seconds because of the similar camera behavior.

So, please remember about these limitations in case if CCRiA/CCFiA features should be used with this camera in your setup.

The driver does not allow to use PTZ functionality for cameras with "Cropped image" features (like SNB-9000 or SNV-8080 cameras).

The cameras with motorized focus/zoom lenses do not support continuous zooming/focusing like PTZ cameras. The zoom/focus change is used as step-by-step adjustment in Web-interface. As result, zoom/focus change is discrete. The driver also keeps sending of repeatable step commands while zoom/focus key is pressed to emulate continuous movement.

Hanwha box cameras (with 'B' character in model, like XNB-xxxx or QNB-xxxx) supports External PTZ feature which allows to use the camera with PT-platform. Unfortunately there is no way to detect is the camera connected to PT-platform or not via HTTP API calls, so box cameras with External PTZ feature support will be detected as PTZ. This is HTTP API / camera hardware limitation.

The Hanwha's devices has the following limitations for preset positions names:

Only alphanumeric symbols (A-Z, a-z, 0-9) are allowed;

Length of preset name is limited by 12 symbols.

 As result the driver since version 1.0.2.0 stores preset position in '*.preset' XML files. In case if file contains no preset positions, the driver tries to load actual information about preset positions from the Wisenet IP device.

Using of XML storage also allows to use Unicode symbols in preset position names.

The GOV Length value is set to half of current frame-rate (i.e. 2 key frames per second) automatically for recording profile and cannot be adjusted via Web-interface or via HTTP API commands. Select another profile as "Record" profile if this limitation is not suitable for your configuration.

The multi-sensor Wisenet IP device may have different resolution capabilities for different channels. For example, the PNM-9030V sample supports 6096x2540 and 2688x1120 resolutions for first channel, up to 2592x1944 resolution for next 4 ones and up to 1920x1080 for 6-th and 7-th channels.

Unfortunately, the VMS has no possibility to specify different resolution sets for different channels - this is software architecture limitation. In other words, all resolutions (6096x2540, 2688x1120 and 2592x1944) resolutions will be available for all channels.

In case if selected resolution isn't supported by the channel, the nearest greater or maximal resolution will be applied instead. For our example in case of 2592x1944 selection the 2688x1120 will be applied for 1-st channel and 1920x1080 for the 7-th one.

Audio channel uses the same video profile that is used for Recording video stream receiving.

It may cause the conflict in multicast configuration applied by video channel (from Dynamic UI configuration) and by audio channel (loaded from XML file).

So, audio channel changes multicast configuration only in case if it was not changed by video channel yet. Otherwise existing multicast configuration is used for multicasting of audio stream.

The device video profile is used for audio receiving and sending. Any change in video profile setting which causes RTSP session re-starting may also cause audio stream re-subscribing.

The VMS has no possibility to configure audio settings in System Manager, so these settings should be configured via XML configuration file. 

By default only audio encoder (<Encoding> option) is specified: AAC for audio input and G.711 for audio output. The other audio options (including volume/gain) are configured to use values that currently selected in camera's Web-interface.

Wisenet cameras may have frame-rate limitation dependent on amount of profiles which are streaming at the same time:

New Q-series can support 1920x1080 stream by total 45fps. For example, QND-6082R camera supports up to 30 fps for H.264 stream with maximal 1920x1080 resolution. In case of streaming from single profile the camera gives 30 fps stream. However, in case of streaming from 2 different profiles with the same H.264 1080p @ 30 fps stream settings, the camera will stream each of them with 22fps only.

New L-series can support 1920x1080 stream by total 30fps.

The Mirasys VMS has an issue with decoding of G.726 audio stream from several samples like

  Wisenet XND-8080R. The issue will be fixed in next driver releases, please use G.711 or AAC encoding in case if you'll meet problem with G.726 audio decoding.

The driver supports only new version of Edge-Storage feature, which is available since VMS version 8.0. The Edge-Storage capability will not be detected for earlier VMS versions.

Wisenet SNF-8010 camera has an issue with searching of recorded data intervals: it detects only intervals intervals whose begin and end is inside or requested period. Other camera samples detects intersections also (i.e. recording start time is before requested period, and end time is inside the period or after it).

The SNF-8010 camera is discontinued already (since 2018 year), so the issue will not be fixed on camera side. Mirasys also has no plans to add separate processing logic for single model to the driver.

The several multi-sensor devices support recording of material by limited amount of channels.

For example, the PNM-9030V sample allows to record video from "Overview" channel only.

In this case the driver will use Edge-Storage feature only for channels which has "Recording" capability in "Recording" attributes group.

The SUNAPI v2.x specifications have the following limitations for HTTP and RTSP requests related to storage functionality processing:

The milliseconds are not available;

The time should be specified in local format (no UTC support) in all requests;

The time intervals returned by device are also in local time.

  These limitations may cause the following issues:

Since time resolution is one second, the switching between recording and edge materials and vice versa may cause repeatable fragments not longer than one second duration or may have missed data no longer than one second;

Conversion between local time and UTC time may cause problems with material selection while switching to or from daylight saving time (DST);

Changing of time zone may cause selection of wrong time interval during interval receiving.

The Wisenet devices support only one RTSP connection for playback at the same time. So, in case of using of multiple channel device the lost data will be received from the device's SD card in series: all intervals from all channels will be posted to a single queue, and will be extracted from queue only if no other intervals are processed at the moment.

The driver can be used with Windows 7 or newer operating system. Older operating systems are not supported.

Pagination
Previous page
VivotekIPCapture installation and usage
Next page
Installing Metadata Drivers