# NewSonyIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newsonyipcapture-installation-and-usage

NewSonyIPCapture installation and usage

The driver uses the following protocols for video receiving:

HTTP/HTTPS protocol is used for receiving MJPEG video and motion detection stream;

RTP/UDP/IP protocols are used for receiving MPEG-4, H.264 video stream and audio stream;

RTSP protocol is used for controlling of RTP stream for G5 (5-th generation) and newer devices;

HTTP protocol is used for sending audio stream to camera.

HTTP/HTTPS protocol is also used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP/HTTPS ports must
be opened:

HTTP: default port is 80,

HTTPS: default port is 443,

RTSP: default port is 554,

UDP: two sequential ports per video stream are needed in a port range 3556 to 4556.

For example: if there are 4 SONY IP cameras are configured for receiving MPEG-4 or H.264 video in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

The driver may be configured using XML configuration file to set the audio parameters for the SONY G5-G7 IP devices.

Limitations

The SNC-DM160, SNC-DM110 and SNC-CM120 camera models support a Light Funnel function:

The driver sets Light Funnel always to "auto" mode. When it gets active in low illumination, it increases the image sensitivity, but with 1280x960 resolution it switches automatically to a lower, 640x480 resolution.

Activation/deactivation delay for light funnel is about 40 seconds.

Light funnel does not work when one of the following is set:

The image size is one of the following:

JPEG - 960x720: MPEG4 - OFF

JPEG - 768x576: MPEG4 - OFF

JPEG cropping is on

SolidPTZ is on

Iris open is on.

Please note that when Light Funnel is off, the max frame rate is 15 fps. For more details, please see the camera's user guide.

With high picture resolutions, the frame rate may be lower than requested.

Analog Video-Out feature notes

The driver disables Analog Video-Out feature for SONY G4 IP cameras (4-th generation). Enabling of this feature causes a limitation of supported codecs and resolutions (for example, SCN-CS20 camera will support only 640x480 resolution)

The driver doesn't change Analog Video-Out setting for G5/G6 SONY IP cameras. Please note that the camera's performance may be affected if this feature is be set to "On"

Motion Detection feature notes

Please configure motion detection zones manually via the web interface before using the Motion Detection driver functionality.

SONY cameras may not send the correct motion events stream when the Motion Detection page is opened on the camera's web interface. This means that MD functionality will not work correctly in this case.

Other limitations

SNC-DM160, SNC-DM110 and SNC-CM120 cameras support 1280x960, 960x720 and 768x576 resolutions and are used only with JPEG compression, but these resolutions are also shown with MPEG-4 in System Manager camera settings. If one of these resolutions is selected with MPEG-4, the actual resolution is always 640x480.

SNC-CS20, SNC-DS60 and SNC-DS10 cameras support 768x576 resolution only with JPEG compression, but this resolution is shown in System Manager also with MPEG-4.

All P models of G3 cameras (3-rd generation) have maximum framerate of 8 fps (N models 10 fps) with H.264 compression, but System Manager camera settings shows 25 fps as a maximum. Because some camera models can give up to 12 fps the driver uses that value as the framerate maximum.

With JPEG compression System Manager shows framerates of the G2 cameras (2-nd generation) as 1 to 25, but the cameras supports only 5, 6, 8, 10, 15, 20 (and 30 in NTSC mode) fps.

Preset functionality and Privacy zones functionality will not work correctly in VMS 5.9.8. This issue is caused by incompatibility of some program interfaces.

In some scenarios SONY cameras start to send video for MJPEG codec with greater frame rate than required. For example, after zooming SONY SNC-Z20P camera sends MJPEG video stream with 24-25 fps, even if frame rate setting set to 20 in System manager. This is a feature of the camera's firmware.

SONY SNC-Z20 camera sends MJPEG video stream with lower framerate than required when maximal resolution and quality settings are set. For example, maximal frame rate for 736x544 resolution and 100% quality setting cannot be greater than 3. This is camera feature.

SONY SNC-Z20 camera supports Zoom and Focus functionality, but it doesn't support Pan/Tilt functionality at all. However, VMS shows Pan/Tilt control on Device window in any case (even if Pan/Tilt is not supported by camera and this control is disabled by the driver). This is a VMS issue.

SONY SNC-Z20 camera doesn't support preset functionality. But the "Add Preposition" button is always enabled for it in VMS 5.4.4. This is VMS issue.

SONY SNC-CH210 supports 2048x1536 resolution only for MJPEG video codec (aspect ratio setting should be set to 16:9 value). For other codec maximal resolution value is 1600x1200.

A few of G5 cameras (5-th generation) have limitation to privacy rectangle size. The rectangle cannot be greater than 1/16 of camera image:

640x480 pixels for SNC-CH220/DH220 cameras (relative to the maximal 1920x1080 resolution)

200x140 pixels for SNC-EM520/EM521 cameras (relative to the maximal 800x600 resolution)

So, real privacy zones may be lower than applied by users because of this camera's feature.

SONY G5 cameras send HD video stream with speed up to 15 Mbps. Subscribing HD resolution high-quality video for H.264/MPEG-4 codec or HD resolution video for MJPEG codec from more than one camera may cause lags in video stream. For example, real frame-rate will jump within 2..13 interval for 15 fps setting.

SONY G5/G6 cameras restart own video encoder after video options changing. This operation takes 3-8 seconds, so CCRiA and CCFiA features (change options by alarm) cannot be used with these cameras.

SONY SNC-VB630 camera starts H.264 stream by motion with 10-20 frames per second instead of applying 50 fps when 1% of quality is selected. Please use 2% quality value to avoid this behavior.

The SONY G6 cameras uses quality settings (variable bit-rate) to set quality of H.264 stream. Previous camera generations uses Constant bit-rate (CBR) option for MPEG-4 and H.264 encodings.

Multiple streaming feature is available for SONY G5 and G6 devices and for VMS version 6.1.1 and newer. Older SONY devices do not support this feature.

The SONY G5/G6 cameras apply video settings during several seconds and may stop streaming during this procedure. So, starting of any stream may cause re-subscribing of other active streams.

SONY G5 cameras have the following limitations for the Multiple streaming feature

The SNC-RS44/RS46/RS84/RS86 cameras support up to 3 streams. Other G5 devices support only 2 streams (Recording and Live)

Resolution of second stream cannot be greater than 640x480 except case when it is equal to resolution of first stream.

Resolution of third stream should be equal to current resolution of first or second stream.

The G5 cameras may not start video stream in case in MJPEG is selected for Live stream with maximal resolution. This issue is caused by unexpected camera behavior (RTSP PLAY request returns error code 451). Please change encoding or decrease resolution settings in case if you met this issue.

The driver will select suitable resolution automatically during settings applying in case if current resolution is not supported by the camera. So, stream resolution may differ from settings applied in VMS. Please refer to camera's Web-interface to learn video settings limitations.

The SONY G5/G6 cameras may have an issues with encoding/decoding of G.726 audio stream (noise, no audio, etc.). Please use G.711 codec in case of problems with G.726 codec.

Audio output (sending to camera) may not be restored after signal lost for SONY G6 cameras.

Camera may return HTTP error 503 code. To restore audio output funtionality please reboot the camera via Web Interface, "System" – "Initialize" - "Reboot".

The SONY G7 camera limitations

"Output modes":

The SONY G7 can work in the several different "Output modes". The "Output mode" option can be changed in the "System" –  "Installation" section of the Web Interface.

Before changing this mode it is recommended to remove camera from the VMS. After changing the output mode it is necessary to re-add the camera to the system.

Multiple streaming feature is available only in the following "Output modes":

"4K Multi streaming"

"Intelligent cropping (FullHD)"

"Intelligent cropping (VGA)"

The camera in the "HDMI" output mode can not be detected and added.

The available list of video resolutions, video codecs and frame rates is limited and depends on selected "Output mode" and "Aspect ratio". Please re-add camera to the VMS after changing this mode.

The SONY G7 cameras have frame rate values with the floating point. The driver will round the value to nearest integer.

The H264Quality option is not acceptable for the SONY G7 device series. The driver will convert the “Quality” value into the bit rate value for the H.264 codec.

For the SONY G7 cameras in the "4K" output modes the H.264 high resolution stream cannot be decoded correctly by VMS video codec if "B picture" option is enabled on camera. The driver disables it by default.

If the Edge Storage recording is enabled the bit rate will be limited to 8Mbps or less for the H.264 codec.

SONY H-series devices (like SNC-HM662 camera) use different SDK than other SONY G6 cameras and cannot be added by native SONY driver. Please use Vivotek IP Capture driver instead for this device series.

SONY SNC-EMX32R/52R devices use different SDK than other SONY G6/G7 cameras and cannot be added by native SONY driver. Please use BOSCH driver (NewBoschIPCapture) instead for this device series.

The Time synchronization feature uses the following rules:

The time synchronization procedure is initialized by any of the following condition:

Windows system time change;

Windows time-zone change;

Any error occurs on previous time synchronization;

Previous successful synchronization was performed more than 30 minutes ago.

      These conditions are checked every 5 minutes

The new time will be set to IP device in case if difference between device's and recorder's times is 10 or more seconds

The SONY HTTP API allows to apply time in GMT format, so the driver will not update time-zone settings on IP device

Change options in alarm (CRiA/CFA) feature can be used in "Active" control mode only. In case of "Passive" mode the driver will not change any option on the IP camera, so stream will keep going without resolution or frame-rate changing.

The Windows XP is not supported since driver version 2.6.0.0




Pagination
Previous page
NewSiquraIPCapture installation and usage
Next page
OnvifIPCapture installation and usage