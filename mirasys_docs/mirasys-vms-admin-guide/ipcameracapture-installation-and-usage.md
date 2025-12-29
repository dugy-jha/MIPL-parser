# IPCameraCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/ipcameracapture-installation-and-usage

IPCameraCapture installation and usage

The driver uses RTSP/RTP/UDP/IP protocols for video and audio receiving in all compression modes.

HTTP/HTTPS protocol is used for parameter setting/retrieving and for PTZ functionality.

If there is a firewall between DVMS and the UDP IP devices, the following RTSP/UDP/HTTP/HTTPS ports must be opened:

HTTP: default port is 80,

HTTPS: default port is 443 (if enabled on the camera)

RTSP: port 554,

UDP: two sequential ports per audio/video stream are needed in a port range of 3556 to 4556.

Limitations

UDP cameras sometimes do not process the PTZ stop command. To avoid this issue, the driver sends four stops.

There are no iris settings for UDP/Amano/GANZ cameras. Firmware for UDP/Amano/GANZ cameras allows for changes in video standards, but cameras support only one of them (in general).

2Mpx cameras have a problem with MJPEG 100% quality - it stops streaming. 2Mpx cameras have different resolutions for MPEG4 codec (no 2Mpx).

The IPE1100 M cameras have a maximum resolution setting (SETUP > Video & Audio > Video-In > Video Resolution parameter). This setting determines the list of available resolutions—e.g., the minimum resolution for 2Mpx will be VGA, and smaller resolutions will not be available.

Enabling multiple streaming or multicast streaming features may decrease device performance. Therefore, both video streams will be sent at lower frame rates than currently applied.

Devices of the IPE series send all streams with unstable frame rates if at least one of these streams is configured for MJPEG encoding. The frame rate becomes stable when the MJPEG stream is stopped. This is a feature of IPE series devices.

Devices of IPN/IPX may apply video settings for a long period (70-90 seconds) if the multiple streaming feature is enabled. Please wait for the video stream to start before changing the video settings again.

The IPN/IPX series devices have the following note in the Web Interface: "If a vertical resolution of 1080P is selected, other video streams cannot support a horizontal resolution higher than 1088." The camera behavior may be unexpected if the user tries to apply 1080p resolution for both video streams.

Multicast capture limitations:

Multicast capture can be enabled via an XML configuration file using the StreamingMode option. Refreshing device settings will be enough to activate the changed StreamingMode option.

The driver instance can be configured as a primary or listener. The primary instance can change IP device settings and use additional functionality. Listener instances can receive video and audio streams by multicast and use digital I/O functionality.

The user should guarantee that only one recorder will change the settings of UDP IP devices. Other recorders that use this device should be in listener mode.

The multicast stream uses the same settings until it is restarted, even if stream settings are changed. Changing stream status (starting or stopping) requires 6-10 seconds. So, applying stream settings will take 30-60 seconds.

Please note that the driver uses only the default adapter for multicast streaming. So, multicast may not work correctly if your PC has more than one network card. Please contact Customer Support if you encounter a problem with multicast configuration.

Time synchronization functionality limitations:

The changing of time zone will not affect the system time until reboot. So, to apply the correct time, the driver may reboot the camera after the time zone setting change.

The Daylight Saving Time option (DST) is always enabled for cameras of the IPN/IPX series. This is a limitation of the camera's firmware.

Edge Storage functionality limitations:

The Edge storage functionality is supported for IPX/IPN series cameras only, starting from firmware version 1.8.0.4

The recording on the SD card should be configured manually on the camera's web interface before using this functionality in the VMS.

The IPN/IPX cameras allow recording on SD card only an H.264 stream. Changing the encoding of the profile used for recording will turn off the storage of video material on SD card.

The IPN/IPX cameras allow searching recorded materials by events only. This is a limitation of the camera's SDK. Because of this limitation, video recorded using Continuous Recording settings cannot be handled.

The maximal event duration is 65 seconds (5 seconds pre-recording and 60 seconds post-recording). There is no possibility to configure recording of longer time intervals.







Pagination
Previous page
HTTPIPCapture installation and usage
Next page
LGEIPCapture installation and usage