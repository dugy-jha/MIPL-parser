# NewPanasonicIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/newpanasonicipcapture-installation-and-usage

NewPanasonicIPCapture installation and usage

In all compression modes, the driver uses RTSP/RTP/UDP protocols for video receiving, HTTP/HTTPS for parameters setting/retieving and for PTZ functionality.

In H.264/MPEG4 compression mode driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving and MJPEG stream continuous receiving.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: default port is 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

NewPanasonicIPCapture.xml file is used to configure:

Driver behaviour:

Unicast

Multicast:Primary

Multicast:Listener

Transmission priority:

Bitrate

Framerate

Best effort

Advanced VBR

VBR

Minimum bitrate (for Best effort mode only)




Pagination
Previous page
NewMobotixIPCapture installation and usage
Next page
NewSamsungIPCapture installation and usage