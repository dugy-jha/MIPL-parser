# StanleyIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/stanleyipcapture-installation-and-usage

StanleyIPCapture installation and usage

In all compression modes driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

For example: if there are 4 cameras in VMS, then ports 3556, 3557, 3558, 3559,
3560, 3561, 3562 and 3563 will be used. If a port isn't free, it will be skipped.

Limitations

Driver detects capabilities for currently enabled profile only. If user changed profile in camera web interface, it is required to update camera capabilities in VMS (re-start auto-search in System Manager or re-add camera).

In VMS is not possible to set different number of resolutions for different compression formats, so in System manager will be displayed all supported resolutions. If some resolution is not supported by compression format, the nearest valid resolution will be used.

Different resolutions support different maximum framerate, so driver will use the nearest valid framerate value. For example, if maximum framerate for 1080p resolution is 15 fps and user applies 30 fps in System Manager settings, the driver will set 15 fps to camera.

H.264 video stream doesn't have quality setting, so to control stream quality constant bitrate mode (CBR) is used. 1% of quality in System Manager means minimum bitrate value and 100% quality means maximum bitrate value.

For multiple streaming each stream will have only one codec and one resolution. For example, first profile in camera has the following combinations:

      -> H.264 :1920 x 1080

      -> H.264 :720 x 480

      -> JPEG :720 x 480

      -> JPEG :352 x 240

  So, first stream will have H.264 codec and 1920x1080 resolution, second stream will have H.264 codec and 720x480 resolution, third stream will have JPEG codec and 720x480 resolution. And fourth combination (JPEG codec and 352 x 240 resolution) will be used for first stream again. Multiple streaming can be disabled in driver XML file.

Privacy zones can be bigger then displayed in System Manager, because  Stanley cameras use fixed blocks to set mask (20 blocks in horizontal and 12 block in vertical).




Pagination
Previous page
SIPIPCapture installation and usage
Next page
VivotekIPCapture installation and usage