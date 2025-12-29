# VivotekIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/vivotekipcapture-installation-and-usage

VivotekIPCapture installation and usage

In all compression modes driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

For example: if there are 4 Vivotek IP cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

Limitations

Sometimes camera goes to the "HTTP only" mode according to network capabilities detection mechanism (camera internal mechanism). To return camera to the "RTP" mode it should be rebooted.

Camera skips channel settings while switching from the "quality priority" mode to the "frame rate priority" mode. Video mode can be set in driver XML file.

Default viewing mask for high resolution doesn't show all picture. It can be configured using Web-interface.

Maximum frame rate for high resolutions is lower than declared.

Commands for iris changing are not working for tested SD7323 camera.

AAC audio decompression is supported from VMS 7.4.4 or higher.

Sony H-series devices (like SNC-HM662 camera) uses Vivotek OEM SDK unlike other Sony G6 cameras. The Vivotek native driver should be used for these devices instead of Sony native driver.

The Windows XP is not supported since driver version 1.6.1.0

CCRiA and CCFiA features available only for devices 8xxx series or higher

When resolution is changed by alarm, user can see one invalid frame. This is device issue - camera send one invalid frame - and driver cannot skip it, because all headers looks ok.




Pagination
Previous page
StanleyIPCapture installation and usage
Next page
WisenetIPCapture installation and usage