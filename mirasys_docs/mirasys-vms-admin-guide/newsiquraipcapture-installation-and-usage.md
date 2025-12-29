# NewSiquraIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/newsiquraipcapture-installation-and-usage

NewSiquraIPCapture installation and usage

In all compression modes the driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving and for PTZ functionality.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: default port is port 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

For example: if there are 4 Siqura codecs in a DVMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

Limitations

H.264 decoder may sometimes fail to decode the received picture frame generating an error in the DVR log file.

Sometimes an analog dome-camera does not process PTZ commands. For example, dome camera sometimes does not stop after controlling has ceased, or does not move after abrupt direction change. Moreover, another HTTP command with the same parameters will be ignored, until a HTTP command with different parameter is received. Probably, it is a feature of Siqura video-server.

MJPEG video from Siqura MD2x/HD2x cameras stops for a moment during live. It seems like one frame skips. The same behavior occurs in Web-interface. This is camera problem.

Siqura MD2x cameras with old hardware base do not support Output functionality. The driver cannot detect hardware information, so output will be shown in DVMS in any case. 

Siqura devices do not support continuous Iris changing - this is firmware feature.

All preset commands described in MD2x/MD6x/HD2x/HD6x protocol (filename "NKF - Protocol Hotkey 20090805") as commands for access to special camera functionality will be disabled in PTZ module. So, supported preset count for Siqura PTZ cameras will be less than 256.

Live MJPEG Encoder on Siqura PTZ cameras work with lower priority than other encoders (MPEG-4 and H.264). So, real framerate values may be less than required for MJPEG HTTP channel, especially in low-light-level conditions.

Driver stores preposition names in XML file. Unicode preset names are supported since driver version 1.9.2.0




Pagination
Previous page
NewSamsungIPCapture installation and usage
Next page
NewSonyIPCapture installation and usage