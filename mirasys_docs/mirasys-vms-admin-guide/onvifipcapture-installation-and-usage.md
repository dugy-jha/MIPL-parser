# OnvifIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/onvifipcapture-installation-and-usage

OnvifIPCapture installation and usage

In all compression modes driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: default port is 554,

UDP: two sequential ports per unicast audio or video stream is needed in a port range 3556 to 4556.

For example, if there are 4 IP cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562, and 3563 will be used. If a port is not free, it will be skipped.

The multicast streaming also requires two sequential ports per audio or video stream, but the ports numbers depends from device settings or XML configuration. For example, the device may be configured to send all streams to the single port only. The ports 40000-40001 should be opened in case if 40000 port is specified for this setting.

Limitations

PTZ Area Zoom command is combined by default with PTZ Center command, if supported

The PTZ Center command is performed with little accuracy, since the accuracy is highly dependent on the camera mechanism, vertical and horizontal angles of view, optical aberrations (e.g. distortion) of the current lens. There is currently no place to enter and store these settings.

The driver requires media profile for receive presets from the IP device. So, they may be loaded after video stream was subscribed.

The driver uses timestamps for authentication on the device according to the ONVIF specifications. So, time on ONVIF-compliant device and time on PC whereVMS Recorder installed should be synchronized before using of this device.

The driver doesn't support Unicode preposition names.

Multiple streaming feature may have limitation dependent from used device (for example, resolution on encoder1 cannot be greater, that resolution on video encoder2). Please refer to device manual to learn these limitations.

Multiple channel devices may support different capabilities for different channels. For example, first channel supports H.264 and MPEG-4 stream with 1920x1080 resolution and second stream supports H.264 encoding only but with greater 4096x2160 resolution. The VMS architecture does not allow to pass different capabilities for different channels, so capabilities from all channels will be combined (i.e. MPEG-4 encoding and 4096x2160 resolution will be available for both channels in sample above).

The driver will select suitable option automatically in case if user will try to apply option value that doesn't supported by current video channel.

In some cases user can face "No signal" problem because of wrong configuration applied on the ONVIF-compliant device ("ter:Action > ter:ConfigurationConflict" message will appear into the log file). In this case user should correct settings in VMS according to device capabilities if Multiple streaming is enabled. If Multiple streaming option is not used, please apply minimal settings on additional streams via Web-interface or disable them at all.

ONVIF compliant devices may not be able to switch streaming mode from "single stream" to "triple stream" without applying of settings for second stream. In other words, Remote stream may not be setup correctly in case if Live stream was not started after Multiple Streaming feature was enabled.

The driver applies settings for different streams in series, not at the same time. So, starting of additional streams may take more time that starting of Recording stream only.

The driver uses PTZ service version 2.0 according to the ONVIF specifications. However, old devices may use previous 1.0 version of PTZ service, so the driver will not detect PTZ capabilities correctly. Please use XML configuration file to specify correct PTZ Service version in this case.

The driver uses Pull-Point mechanism for receiving states of digital inputs and to monitor motion detection stream. If ONVIF-compliant device supports this mechanism, it should set WSPullPointSupport capability in tds:GetCapabilitiesResponse according to section 9.9 of ONVIF Core specification. The digital inputs and VMD functionality will not be detected if this capability is set to unsupported.

Audio functionality limitations

The driver use audio functionality "as is" without adjustment audio parameters (like output gain). The manufacturer specific parameters like "input/output interval" or "output duration" has no appropriate options in ONVIF specifications. Please configure these parameters via Web-interface manually before camera usage.

Multicast capture limitations

Multicast capture can be enabled via XML configuration file using StreamingMode option. This option is read on stream startup, so refresh of device settings will be enough to take changed StreamingMode option into use.

Please note that VMS has optimization for channel re-starting since version 7.4.1, so in this case it will be required to change one of video option for each camera stream to restart them. The audio settings should also be updated to take the option into use.

The driver instance can be configured to be used as Primary or Listener. The primary instance is able to change IP device settings and use additional functionality. Listener instances are able to receive video streams and audio stream by multicast and allows to use digital I/O and VMD functionality.

The driver selects combination of video sources, video encoders and media profiles during capabilities detection. It is required to select the same encoding on both Primary and Listener instances to allow them to select the same media profile. Otherwise the Listener driver instance will try to subscribe another profile and will receive another multicast stream or will not receive any data at all.

The Listener recorder will not change any configuration on ONVIF-compliant device side. For example, if there is no media profile available on camera - it will not be created and the driver will not be able to receive the video or audio stream. The ONVIF device should be added to Primary recorder before using in Listener configuration.

The additional streams (Live and Remote) are active in case if they are opened in clients only. So, to take updated Multiple Streaming settings into use it is required to start (or keep opened) these streams for Primary recorder after stream settings have been changed in VMS. Otherwise the latest stream settings will not be applied to camera.

User should guarantee that only one recorder will change settings of ONVIF-compliant IP devices. Other recorders which use these devices should be in Listener mode.

It is required to specify IP address of the network adapter through which camera is connected to receive multicast streaming correctly in case if more than one network adapter is available. The network adapter marked in Windows as default will be used if no option is configured.

The driver may write message about invalid multicast configuration (like:  ter:InvalidArgVal > ter:InvalidMulticastSettings). This message means that something is wrong with multicast configuration and video or audio stream cannot be started.

Please specify Multicast section in XML configuration file to resolve the problem or adjust values if this section already exists.

Several ONVIF-compliant IP devices (Axis, for example) allows to keep video stream while the client changing it's video parameters. As result, such device will keep active stream for Multicast:Listener instance with previous settings and start another stream for Multicast:Primary instance with updated settings.

It is required to enable video options monitoring on listener side by using VideoSettingsMonitoringInterval parameter. More details may be found in comments in the configuration file.

Video Motion Detection functionality limitations

The device should support 'tns1:VideoSource/MotionAlarm' topic-set to support motion detection functionality. The custom topic sets like 'tns1:VideoAnalytics/tnssamsung:MotionDetection' may also be supported, but they will work for single-channel device only because these topic sets have no video source or channel identifiers as source data in event notifications.

There is no IP device related motion detection settings in VMS available. So, the motion detection settings (areas, sensitivity, object size and etc.) should be configured on IP device manually before using this functionality in VMS.

The motion detection may be used with Multicast streaming. The "Recorder and camera hardware" option should be enabled on both Primary and Listener recorders to pause/resume video stream correctly.

There is no possibility to detect time of video options applying without camera configuration change. The driver adds support of CFiA/CRiA features for all devices, but it cannot guarantee that camera will switch options by alarm fast enough.

  Please try CFiA/CRiA feature on test setup before taking them into use with security systems.

Other notes

The driver uses "RTP over RTSP" transport for video/audio streaming by default since driver version 1.5.0.0

The digital inputs returned by the ONVIF-compliant device are sorted by token name to be sure that they will not be reordered by the device on initial state request. As result real input numbers may differ from VMS values (like "1", "2", ..., "10" list will be sorted  as "1", "10", "2", ..., "9").

Change options in alarm (CRiA/CFA) feature can be used in "Active" control mode only. In case of "Passive" mode the driver will not change any option on the IP camera, so stream will keep going without resolution or frame-rate changing.

The Windows XP is not supported since driver version 1.5.0.0




Pagination
Previous page
NewSonyIPCapture installation and usage
Next page
PelcoIPCapture installation and usage