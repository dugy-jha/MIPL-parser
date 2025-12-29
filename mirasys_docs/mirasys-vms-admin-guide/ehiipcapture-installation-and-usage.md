# EHIIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/ehiipcapture-installation-and-usage

EHIIPCapture installation and usage

The driver uses RTSP/RTP/HTTP/HTTPS/UDP/IP protocols for video receiving in all compression modes. Also, HTTP/HTTPS protocols are used for parameter setting/retrieving and for Remote stream video. If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP/HTTPS ports must be opened:

HTTP: default port is 80,

HTTPS: default port is 443,

RTSP: port 554,

UDP: two sequential ports per video stream are needed in a port range of 3556 to 4556.

For example, if there are 4 cameras in DVMS, ports 3556, 3557, 3558, 3559, 3560, 3561, 3562, and 3563 will be used. If a port isn't free, it will be skipped.

The EHIIPCapture.xml file can be used to select a 360-degree view (channel) - please specify channel numbers that should be used in the following section in XML:

<Channel360>1</Channel360>
<Channel360>2</Channel360>


After setting channel numbers for a 360-degree camera, the camera must be removed and added again to detect the correct capabilities for the channels.

Multicast streaming also requires two sequential ports per audio or video stream, but the port numbers depend on device settings or XML configuration.

For example, the device may be configured to send all streams to a single port only. If the 40000 port is specified for this setting, ports 40000-40001 should be opened.

Limitations

Only one audio multicast stream is supported. One multicast IP address is used for the audio channel and for the video channel but the multicast audio port for the same stream should be greater than the video port by at least 2, multicast video port for another stream (Live, for example) should be greater than the video port of previous stream (Recording, for example) at least 6.

The audio channel uses the same multicast IP address as the video stream receiver. If different multicast addresses are defined, this may cause a conflict in the multicast configuration applied by the video channel (from the Dynamic UI configuration) and the audio channel (loaded from the XML file).

You must enable IGMP Snooping on the network switch for multicast communication.

For HTTP/HTTPS transport, the following logic is implemented: The RTPoverHTTP dynamic field is added if the communication over HTTP is used or if the communication over HTTPS is used. The device supports the RTPoverHTTPS feature.

Regarding the TLS certificate, when an RTSP connection over HTTPS (TLS) is made, the camera shares its public certificate during the Handshake procedure. Therefore, clients need not store or have the cameraís public certificate.

Multiple streaming mode is supported correctly only from DVMS 6.1

The compression format for Recording and Live streaming should be the same in multiple streaming mode

Cameras reboot after changing the compression format, so it requires about 30 seconds to restore video after changing the compression format.

The remote stream has the same resolution as the Recording stream for devices with two streams per channel ("Main" and "Sub"), so the resolution setting is not used for such a stream, which is an HTTP JPEG capture.

For devices with 3 streams per channel, this limitation does not exist.

Some versions of Hikvision firmware return a list of resolutions the camera does not support. These resolutions can be applied in DVMS, but camera images will have artifacts.

Hikvision cameras support only 6 RTSP sessions at the same time. This is a limitation of the Hikvision firmware.

Motion detection should be configured manually on the device before use in the DVMS. MD functionality may not work correctly with old firmware versions. Please use the latest firmware version to use all driver features.

Receiving input states should be enabled in the XML configuration file and configured in the device web interface (e.g., enable sending input states with "Notify Surveillance Center").

The third stream of Hikvsion devices is used as a Live stream and 2nd as a Remote.

Video loss detection should be configured manually on the device before using it in the DVMS. It can also be disabled/enabled in the configuration file.

Pagination
Previous page
DahuaIPCapture installation and usage
Next page
EIPCapture installation and usage