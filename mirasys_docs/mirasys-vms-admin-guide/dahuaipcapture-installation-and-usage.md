# DahuaIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/dahuaipcapture-installation-and-usage

DahuaIPCapture installation and usage

The driver uses RTSP/RTP/UDP/IP protocols for video receiving in all compression modes.

The HTTP protocol is used for parameter setting/retrieving. If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 554,

UDP: two sequential ports per video stream are needed in a port range of 3556 to 4556.

For example, if there are 4 Dahua IP cameras in a DVMS, ports 3556, 3557, 3558, 3559, 3560, 3561, 3562, and 3563 will be used. If a port is not free, it will be skipped.

Limitations

Multiple streaming features may have limitations dependent on the device used (for example, the resolution on the Extra stream cannot be greater than that on the video Mainstream). Please refer to the device manual to learn these limitations.

The CCRiA (Can Change Resolution in Alarm) feature is not supported because it takes longer to apply a new resolution than the signal lost timeout.

Cameras with two dependent sensors, for example DH-SDT4E425-8P-GB-APV1, are not fully supported.
Our VMS does not support different resolutions for different channels of the same device. All channels will have the same resolution list, but only supported resolutions can be applied.
The same is valid for changing the resolution in alarm functionality.

If Dahua/Stanley devices do not change the resolution or framerate correctly, please update it to a new firmware. Driver will print the following message in the DVRLog.txt:

"Can't configure video channels for device <ip>:80, result code: 12002 (Request timeout).” " Device may not accept new video settings without correct Bitrate parameter. The camera sends an incorrect bitrate range, and the driver will calculate an unacceptable Bitrate by Quality and try to apply it in both CBR and VBR modes. It is possible to override the Bitrate range using the following option in the DahuaIPCapture.xml <BitrateMap enabled="yes" Driver has an internal bitrate map for most resolutions up to 1920x1080 for the H.264 codec only. It is possible to add more bitrates for higher resolutions and JPEG codec, as shown in the examples in the driver's XML.

Dahua device may be added with a lower maximal frame rate than some resolutions support. Please update the firmware. If it is unavailable, please remove the Dahua device from DVMS, set the required video settings using the Web Interface, and add it again.

If the Dahua device returns many "400" or "500" HTTP errors in response, please update it to a new firmware. In case the firmware update is not available, then there are several parameters in the DahuaIPCapture.xml:

<UseEventManager>false</UseEventManager> To disable the "EventManeger" poll requests

<InputCheckTimeout>1000</InputCheckTimeout> To adjust the interval between digital inputs requests, only if disabled the <UseEventManager>false</UseEventManager> option

<Control digitalInputs="false" motionDetection="false" /> To disable digital inputs and motion detection on camera hardware

Audio functionality limitations:

The driver uses audio functionality "as is" without adjusting audio parameters (like output gain). Please configure these parameters via the Web Interface.

The driver supports G.711 and G.726 audio encodings. The AAC encoding is not supported.

For some firmware versions, Two-Way audio may not work after network disconnections. Please remove the device from DVMS, reboot it, and add it again. To disable this feature for a particular device, set the following option: <TwoWayAudio>NO</TwoWayAudio>

Multicast capture limitations:

Multicast capture can be enabled via an XML configuration file using the RTPMode option. This option is read on stream startup, so a refresh of device settings will be enough to activate the changed RTPMode option.

The user should guarantee that only one recorder changes the settings of IP devices. Other recorders that use this camera should not change settings.
Please disable camera settings changes using the following option <ChangeSettings>false</ChangeSettings>
In this mode, driver will not change the following camera settings:
= Quality
= Resolution
= Framerate

<ChangeSettings>true</ChangeSettings>
The driver will change the camera settings according to the DVMS settings and receive audio and video data from the camera using a multicast connection. Please configure this mode only for the primary recorder.

For the secondary recorder, the following options will be configured the same as for the primary recorder:
= Multiple streaming option
= Video Codec for all streams

Encrypted streaming features known issues and limitations:

Dahua IP Capture driver supports receiving encrypted video streams from the IP devices. Processing of encrypted stream is based on 3-rd party Dahua libraries (NetSDK and PlaySDK from Dahua)

Stream encryption should be enabled via Web UI before using it in the Mirasys VMS. To enable it, go to device settings, then select the "System" group, then the "Security" or "Safety" subgroup (the name may differ for different devices). Select the ìSystem Serviceî tab in the settings dialog, then enable the "Audio and Video Transmission Encryption" checkbox.

If the IP device supports stream encryption, the system will add the "AES-256 Encrypted" transport and select it as the default transport. If you do not need to use stream encryption ñ just select any other transport based on your requirements.

The AES-256 algorithm is used for stream encryption according to Dahua's GDPR specification document. The key-frame encryption is used. In other words:
= The stream encryption may be used for H.265, H.264 and MPEG-4 encodings;
= The MJPEG stream cannot be encrypted and received via SDK libraries as is.

MPEG-4 encryption is supported. However, no device was available to test it in Mirasys. So, the implementation was made based on SDK documentation, but it was not tested.

The audio encryption is available via NetSDK but has not been implemented in the Driver.

The encryption is not supported for multicast streaming.

For quick start video capture in Multicast mode, it is possible to configure addresses and ports on the device and in the driver XML file and disable video settings adjustments by the following option <ChangeSettings>false</ChangeSettings>.

Zoom may not work correctly for the Stanley IPC-STAN-6100IRV camera. It is a camera firmware issue.

The driver doesn't support Unicode in PTZ preset (preposition) names.

Please do not try to search the camera with <All drivers> option and the <default> credential or wrong password - it may lock user account. Please add the device using a single 'DahuaIPCapture' driver instead.

This driver does not support Windows XP.

Pagination
Previous page
CanonIPCapture installation and usage
Next page
EHIIPCapture installation and usage