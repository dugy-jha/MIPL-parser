# NewArecontIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newarecontipcapture-installation-and-usage

NewArecontIPCapture installation and usage

The H.264 compression mode driver uses RTSP/RTP/UDP/IP protocols for video reception at common frame rates. The HTTP protocol is used for parameter setting/retrieval, MJPEG/H.264 stream receiving in case of camera slow frame rates, and MJPEG continuous receiving.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: default port is 554,

UDP: two sequential ports per video stream are needed in a port range of 3554 to 4556.

The driver may be configured using an XML configuration file to set the following parameters:

Indoor lighting compensation value

Channel specific parameters:

MaxFrameRate - max frame rate for full resolution

MaxFrameRateHalf - max frame rate for half resolution

RTP over RTSP transport protocol

RTP block size (if required by the specific router)

BitrateMode (CBR, VBR, or Auto - the last one tells the driver to skip quality change on camera)

BitrateMin (minimum bitrate for CBR)

BirateMax (maximum bitrate for CBR)

KeyFrameIntervalMs (Intra frame interval in ms, 0 - all intras)

IndoorLightFrequency - light frequency

Limitations

The maximum frame rate value is calculated using the Arecont "secret" formula. The real frame rate can be lower than specified—it depends on network conditions.

Some picture resolutions can differ from settings, e.g., 1600x1200 will be 1600x1184. This happens because the Arecont camera resolution must be divisible by 32 for full and 64 for half mode.

The Arecont max resolution is set on the camera. VMS uses it and half of it. To change the maximum resolution, you need to change it on camera and then add a camera to the VMS.

Arecont cameras have only two full picture resolutions—the max sensor resolution and half of it. The other resolutions are cropped from the max and are not used in the driver.

AV8185 and AV8180 have no IO (information in their documentation is incorrect). 

AV3135 has two sensors—day and night. Both work at specific resolutions. VMS shows resolutions for day mode; real frame resolution can differ from settings.

Arecont cameras can dynamically change picture resolution. Actual frame resolution can differ from settings.

DVMS supports only 30 fps max, so all Arecont cameras will have this limitation (even if they support more than 30 fps).

Arecont 4ch cameras can have issues when H.264 + MJPEG is used. It is better to use one compression format for all channels.




Pagination
Previous page
NewActiIPCapture installation and usage
Next page
NewAxisIPCapture installation and usage