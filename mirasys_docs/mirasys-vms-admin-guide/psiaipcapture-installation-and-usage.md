# PSIAIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/psiaipcapture-installation-and-usage

PSIAIPCapture installation and usage

In all compression modes driver uses RTSP/RTP/UDP/IP protocols for video receiving. HTTP protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 554,

UDP: two sequential ports per video stream is needed in a port range 3556 to 4556.

For example: if there are 4 cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

Limitations

Only primary video channel is supported (if camera has several channels)

Pagination
Previous page
PelcoIPCapture installation and usage
Next page
RTSPIPCapture installation and usage