# EIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/eipcapture-installation-and-usage

EIPCapture installation and usage

The driver uses RTSP/RTP/UDP/IP protocols for video receiving in all compression modes.

The HTTP protocol is used for parameter setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 554,

UDP: two sequential ports per video stream are needed in a port range of 3556 to 4556.

For example: if there are 4 El.MO or Dynacolor IP cameras in a DVMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

Limitations

The WinInet library is used to send/receive HTTP data between DVMS and the e-Vision/Dynacolor camera. The 8.0 version of this library has a limitation: only 2 HTTP connections may be opened at the same time (please refer to the following article: http://support.microsoft.com/kb/183110).> This issue becomes actual after Internet Explorer is updated to 8.0 or higher.

If the camera's Web interface is opened on the same PC where this driver is used, a few HTTP requests may not be sent because of this limitation. In this case, the camera may not be found by Auto-Search, or some functionality may not work at all.

The "Video OCX protocol" option should be set to "RTP over UDP" (or "RTP over RTSP(TCP)" in some cases) for correct receiving of the RTP/RTSP video stream. This option cannot be set via CGI request, so please set it manually via the Web interface (Streaming tab) before using the camera.

The El.MO and Dynacolor cameras (except Dynacolor HD WDR IP cameras) have specific resolution settings. The camera may support different resolutions for different codecs. For example, cameras of the NH-series support the following resolutions (maximal framerate is described in brackets):

MJPEG video codec - 1280x960(12.5 fps), 640x480(25 fps);

MPEG4 video codec - 640x480(25 fps), 320x240(12.5 fps), 352x288(12.5 fps), 176x144(12.5 fps).

When you try to set an unsupported resolution, the most suitable resolution will be applied. Please refer to the camera settings (Streaming -> Video Format page, "Video Resolution" section) for detailed information about the camera's supported resolutions.

The El.MO and Dynacolor cameras support only one or two frame rates (for example, 25 or 12.5 for PAL cameras of the NH-series). Other frame rates may be applied using the "Frame Skip" setting. Usually, the camera supports skipping at 5, 10, and 15 frames internally. If the camera supports 25 fps for a specified resolution, the camera will send a stream with 5, 2.5, and 1.67 fps for appropriate frame skip settings. So, the real framerate may be greater than that applied in VMS when you try to set an unsupported framerate. The most suitable value will be used.

The video stream for cameras of the NH series has an unsteady frame rate for VGA resolution with the highest frame rate and quality settings (for both MPEG-4 and MJPEG codecs). The real frame rate changes between 18 and 30 values, but the average frame rate value is lower by 1-2 fps than required. This is a camera issue.

Dynacolor and El.MO cameras apply each request for stream settings, changing approximately 20 seconds. This is a camera feature.

The IP PTZ cameras have the following issues:

The camera always returns a 503 HTTP error code for each IO command—this is a firmware problem. The IO module is temporarily disabled for cameras in the IP PTZ series.

The camera inverts the "focus" command: it performs the "focus near" action for the "focus far" command and vice versa. This is a firmware problem.

The camera does not restore the connection after unplugging the network cable. After the connection is restored, the camera should be rebooted manually.

The HD WDR IP cameras have the following issues:

The camera sends MPEG-4 frames at a greater frame rate than required. For example, the camera can send up to 16 frames per second for maximal resolution (1280x960) instead of 12.5

The camera does not support Frame Skipping for maximal resolution (1280x960) for the H.264 codec. This is a camera feature. As a result, only one framerate (maximal, 25 or 30 fps) will be available for maximal resolution for the H.264 codec.

The V-series cameras have a problem with the H.264 codec. After applying 100% quality for the H. 264 codec, the camera sends an incorrect video stream (the VLC player doesn't play it, and VMS shows a lot of frame-skipping messages). This issue occurs occasionally.

The 5 Megapixel 360∞ Fisheye cameras support only fish-eye views. At the moment, they do not support selecting another viewing area.

Multiple streaming limitations:

Starting from DVMS 6.1.1, multiple streaming features are supported for Full-HD Quad Stream cameras. Other cameras will be used as single-stream devices.

Recording and Live streams support H.264 encoding only. Remote stream supports both MJPEG and H.264 encodings.

Resolutions on different streams depend on each other. The following rule applies for resolution: the resolution of a Live stream cannot be greater than the resolution of a Recording stream. The same rule applies to Remote and Live streams. Please refer to the device manual or Web Interface to learn about these resolution limitations.







Pagination
Previous page
EHIIPCapture installation and usage
Next page
GatewayIPCapture installation and usage