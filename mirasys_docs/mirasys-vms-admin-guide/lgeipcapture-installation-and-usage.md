# LGEIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/lgeipcapture-installation-and-usage

LGEIPCapture installation and usage

The driver uses RTSP/RTP/UDP/IP protocols to receive video streams and input states in all compression modes. HTTP protocol is used for parameter setting/retrieving.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default ports are 80 and 81,

RTSP: port 554,

UDP: Two sequential ports per video stream and two sequential ports per metadata stream (input states) are needed in a port range of 3556 to 4556.

For example, if there are 2 LG Electronics IP cameras in a DVMS, ports 3556, 3557, 3558, 3559, 3560, 3561, 3562, and 3563 will be used. If a port is not free, it will be skipped.

Limitations

A few LG Electronics devices do not allow the device model to be received. For these cameras, the model name will be displayed as "LG Electronics IP camera".

The LDW2010F-N camera sends a QCIF stream with 160x112 resolution instead of 176x112 resolution. This is a camera feature.

LG Electronics devices' digital outputs have one specific feature: they have a duration option and cannot be closed for a long time. The device automatically opens the output when the duration period has expired.

The SOAP API doesn't support commands for switching focus and iris modes between auto and manual values. So, if the user wants to use iris/focus adjustment in DVMS, he should change this value via the Web interface to manual.




Pagination
Previous page
IPCameraCapture installation and usage
Next page
NewActiIPCapture installation and usage