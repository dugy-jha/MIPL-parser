# NewIQEyeIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newiqeyeipcapture-installation-and-usage

NewIQEyeIPCapture installation and usage

The driver uses RTSP/RTP/UDP/IP protocols for receiving H.264 compressed video and audio streams. HTTP protocol is used for parameters setting/retrieving and MJPEG stream continuous receiving.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: default port is 554,

UDP: two sequential ports per audio/video stream are needed in a port range 3554 to 4556.

Limitations

IQEye cameras have one resolution and several cropped resolutions. Cropped resolutions do not used in driver. Driver use only down sample process to change picture size (size / 2, size / 4 and size / 8). Down sampling is enabled for cameras which support it (cameras IQ73xx, IQ04xx, IQD4xx, IQ54xx do not support it).

IQ712 camera has limitation for maximum fps for MJPEG  - 15 fps.

IQEye cameras (except IQ73xx) have only one resolution for H264 ñ 640x480. Others can be used only for MJPEG.

H.264 codec supports only 5,10,15,30 frame rate values for all cameras. Other values used only for MJPEG, they will be scaled to listed above if H.264 codec will be active.

For IQA25S camera for MJPEG codec 2560x1920 and 1280x960 resolutions support maximum fps value 7, for 640x480 and 320x240 resolutions - only 10 fps max.

For IQA25S camera for JPEG codec resolution max /2 should work on 10 fps, but it works as is - max fps is 7, if specified higher - it set 5 or 4 fps, this is firmware issue.

The driver supports only G.711 audio stream receiving. AAC codec is not supported at the moment.

Pagination
Previous page
NewBoschIPCapture installation and usage
Next page
NewMobotixIPCapture installation and usage