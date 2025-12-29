# NewActiIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newactiipcapture-installation-and-usage

NewActiIPCapture installation and usage

In all compression modes, the driver uses RTSP/RTP/UDP/IP protocols for video receiving. The HTTP protocol is used for parameter setting/retrieval.

If there is a firewall between DVMS and the cameras, the following RTSP/UDP/HTTP ports must be opened:

HTTP: default port is 80,

RTSP: port 7070,

UDP: two sequential ports per video stream are needed in a port range of 3556 to 5556.

NewActiIPCapture.xml file is used to configure:

Driver behavior:

Unicast

Multicast:Primary

Multicast:Listener

The camera's stream mode and mounting type (for fisheye cameras) accept de-warping on the camera.

Possible values for stream modes: SINGLE, DUAL, EPTZ, MD_PRESET, FISHEYE_VIEW

Possible values for mounting types: WALL, CEILING

The first PTZ channel ID for ACTi video servers:
General and IP device-specific configuration is available
E.g:
<Device address="192.168.1.75" port="80">
<FirstPTZChannelID>2</FirstPTZChannelID>
</Device>
For device 192.168.1.75:80, the first PTZ channel ID will be 2, the next one (for a multichannel device) will be 3, etc.

Limitations

ACTi TCM-5311 can stop sending the correct stream when abruptly changing the backlight.

ACTi MPEG4 cameras need a delay between setting parameters and starting stream (about 3 sec).

ACTi CAM-6510 doesn't work correctly on 1 fps, so this value is not available for this camera. Acti CAM-6510 camera does not support quality changing, so quality for all values are the same.

ACTi cameras have different frame rates for different compression formats. Settings are converted automatically to the nearest correct value.

ACTi E96, B54, B55, and B56 cameras do not support de-warping on camera, so XML configuration has no effect on those models.

ACD video servers work only with one PTZ camera connected to each channel, with a camera ID = 1. For example, ACD2100 works only with one camera, and ACD2200—with four cameras. ACD multichannel devices have different RS485 ports for PTZ camera connections, and all camera IDs must be equal to 1.

The real frame rate for ACTi cameras can be different from the settings. It depends on the camera settings (lens compensation and shutter speed) and the level of illuminance.

Video cameras do not support I/O functionality. They work in PAL, but the factory default is NTSC. After applying the factory default, the camera does not work.

SED2100 works with ACTi libraries. SED2100 needs to save reboot after every changing of parameters (it takes 30-60sec)

Preset names are stored in XML file (no camera's preset management)

For KCM, the K2 fish eye camera can be used in two video stream modes: SINGLE and EPTZ. Stream mode is detected during camera subscribing to DVMS, then driver will keep this mode. To change stream mode, the camera should be removed from DVMS, stream mode should be changed over the camera's web interface, and then the camera can be subscribed. The driver will set it automatically for all other KCM and TCM series in SINGLE video stream mode.

ACTi driver uses constant bitrate settings that are scaled from the corresponding VMS quality value:

CAM values: 256K, 384K, 500K, 750K, 1M, 1.5M, 2M, 2.5M, 3M

ACM values: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, UNLIMITED

TCM/KCM values: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, 3.5M, 4M, 4.5M, 5M, 5.5M, 6M, UNLIMITED

So, VMS quality 50% will be scaled to a 1Mbit/sec bitrate value. The correct DVMS quality should be set to fit the required network bandwidth.

ACTi video servers have no internal PTZ protocol; they re-send PTZ commands to the camera's COM port in transparent mode. Currently, only the PelcoD protocol is implemented. If an analog camera connected to an ACTi video server cannot work with PelcoD, the driver cannot be used to control the camera.

Not all stream modes are supported by ACTi fish-eye models. E.g., ACTi I51 supports only DUAL (Panorama), FISH_EYE, and EPTZ stream modes. Other settings will have no effect and will be used in stream mode, which is set on the camera.

Stream mode and mounting type should be set before the camera is added to DVMS. To change those values, the user should remove the camera from DVMS, make changes in the configuration file, and add the camera to DVMS again.

Multiple streaming for the fish-eye camera is supported only for those stream modes:

DUAL - 2 streams

MD_PRESET - 2 streams in WALL mounting type, 3 in CEILING

Digital PTZ is working for the fisheye camera only in EPTZ stream mode.

If resolution or stream mode was changed, presets for fisheye camera becomes invalid, need to remove them from DVMS and re-assign again.

MPEG4 is off for DUAL stream mode because it is available only for 1st stream

6VGA and 4VGA stream modes are not supported.

The Stream mode settings in the NewActiIPCapture.xml file are only for the fish-eye cameras. Other camera's stream mode settings will be received from the camera when it is added to DVMS. If camera has DUAL stream mode setting - multiple streaming will be active, if SINGLE - not.

In DUAL stream mode, the frame rate in stream 1 has to be higher or equal to it in stream 2. Otherwise, the frame rate in stream one is limited to the stream two frame rate. For example, the frame rate settings in stream one and stream 2 are 30 and 25. The actual frame rate in stream 1 is 25

KCM/TCM cameras cannot enable privacy masks on the second stream. So, privacy masks are enabled only for single-stream modes (the camera should have a single-stream mode before adding it to DVMS). KCM/TCM cameras have a general issue related to privacy masks and resolutions higher or equal to 1920x1080—the privacy mask can be set only on the left part of the screen (ACTi limitation).

ACTi ACM cameras have an issue with privacy mask settings. The privacy mask position is correct only for maximum resolution; for smaller resolutions, the privacy mask position can be different from the settings.

The ACTi ACM series can return Motion Detection capability, but there is no configurable MD on the camera's web page. For those models, "Recorder and camera hardware" MD cannot be used.

Multicast is not enabled for ACTi CAM models. All those models work with Unicast only. Those cameras cannot be used in several DVMS instances!

Unicast mode: The driver will change the camera settings according to the DVMS settings and receive audio and video data from the camera using a unicast connection.

Multicast:Primary: The driver will change the camera settings according to the DVMS settings and receive audio and video data from the camera using a multicast connection.

Multicast:Listener: driver will not change camera settings, just receive audio and video data from camera using multicast connection.

If the camera is to be used in several DVMS instances, one DVMS should be set to Multicast:Primary, and others should be Multicast:Listener.

Several Multicast:Primary configurations or Multicast:Primary and Unicast configurations are not allowed; in other cases, the camera should be overloaded with continuous concurrent settings changes.

Edge storage is supported only for DEBI series starting from firmware 6.07.23 and higher.

The camera is synchronized to UTC (GMT +00) to avoid local time issues.

RTP over RTSP mode will not work for the following camera series. These cameras do not support this mode or have not been fully tested:

VIDO AMU-xxx

ACTI KCM-xxx

ACTI ACM-xxx







Pagination
Previous page
LGEIPCapture installation and usage
Next page
NewArecontIPCapture installation and usage