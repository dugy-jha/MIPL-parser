# CanonIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/canonipcapture-installation-and-usage

CanonIPCapture installation and usage

In all compression modes driver uses RTSP/RTP/UDP/IP protocols for receiving video stream and input states.

HTTP protocol is used for parameters setting/retrieving.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default ports are 80,

RTSP: port 554,

UDP: two sequential ports per video stream and two sequential ports per metadata stream (input states) are needed in a port range 3556 to 4556.

For example: if there are 2 IP cameras in a DVMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

CanonIPCapture.xml file is used to configure driver behavior:

Unicast

Multicast:Primary

Multicast:Listener

Parameters for PTZ speed limitation:

PanSpeed (1 - 100%, limit speed for required percentage value)

TiltSpeed (1 - 100%, limit speed for required percentage value)

ZoomSpeed (1 - 100%, limit speed for required percentage value)

PTZQueueSize (PTZ queue size, can be optimized for slow cameras)

Limitations

Old Canon cameras with firmware 1.0.3 or earlier can reboot on each resolution change. This can take 1-5 minutes to complete.

VB-S cameras have 2 H.264 streams, which can be used for recording and live in VMS. Other series only has the 1 H.264 channel.

VB-S cameras have a limitation of a maximum framerate of 15 for selected resolutions. If one of those combinations is set, fps will be changed even if DVMS settings are different:

1920x1080 - All sizes

All sizes - 1920x1080

1280x960 - 1280x960

1280x720 - 1280x720

VB-M, VB-H, VB-S series camera Moving Object detection differs from conventional motion detection. The detection creates a static "Background image" and compares any scene change within the detection area with this image.
The camera sends an "Event ON" status notification when the object enters the detection area and sends an "Event OFF" status when an object comes out from the detection area and the scene is changed back to the original "Background image."”
If the "Event ON" status continues over 5-minute periods, the camera regards this as a new background, sends the "Event OFF" status, and resumes Alarm detection standby mode.

Unicast mode: The driver will change the camera settings according to the DVMS settings and receive audio and video data from the camera using a Unicast connection.

Multicast:Primary: The driver will change the camera settings according to the DVMS settings and receive audio and video data from the camera using a multicast connection.

Multicast:Listener: the driver will not change camera settings; just receive audio and video data from the camera using the multicast connection.

If the camera is to be used in several DVMS instances, one DVMS should be set to Multicast:Primary, and others should be Multicast:Listener.

Several Multicast:Primary configurations or Multicast:Primary and Unicast configurations are not allowed; in other cases, the camera should be overloaded with continuous concurrent settings changes.

CCFIA and CCRIA are disabled for the VB-M series because cameras from this series require a reboot after settings change.

Pagination
Previous page
ArchiveCapture installation and usage
Next page
DahuaIPCapture installation and usage