# NewBoschIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/newboschipcapture-installation-and-usage

NewBoschIPCapture installation and usage

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP or HTTPS ports must be opened:

HTTP: default port is 80,

HTTPS: default port is 443,

RTSP: default port is 554,

UDP: two sequential ports in a port range from 3556 to 4556 are required per video/audio stream.

For example, if there are 4 IP cameras in a DVMS, ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

For MPEG-4 video stream-receiving driver uses the Bosch RCP+ SDK library. It opens random UDP ports for video data receiving. The driver may be configured using an XML configuration file to set the following parameters for the Bosch IP devices:

PTZ protocol (PelcoD, OSRD, BiCom)

Fish-eye video channel (only one can be used)

Jpeg stream (Recording, Live or Remote, default Remote)

Edge storage functionality support

Time sync (enabled / disabled)

Control mode (active/passive)

Transport

Key frame interval

Video loss check (enabled / disabled)

Limitations

All Bosch devices should have a user and password set. In other cases, drivers will not recognize the camera (the password shouldn't be empty)

The System Manager will be able to update the driver to 1.3.0.0 from older versions with subscribed Bosch cameras starting from VMS 7.0 version. For older VMS versions, cameras should be removed from DVMS and added again after the driver updates.

If the camera was added without audio channels, to enable them, the camera should also be removed and added to DVMS again.

The driver does not remove or change the old BoschIPCapture driver, but it uses rcpp.dll like the old one.

So, to install the driver, there should be no connected Bosch cameras. Otherwise, the driver installation will fail.

For NTSC cameras connected to the Video-Jet servers series for the MPEG-4 codec, the maximum resolution is 352x240 (CIF). The D1 resolution does not work, so the CIF resolution will be shown instead of D1.

A combination of NTSC and PAL cameras connected to one Video Jet server is prohibited.

The actual framerate for the MJPEG video channel may be lower than the values specified in the settings.

The quality setting in the VMS uses the bitrate value on the camera or video server. So, real picture quality may be the same for different values (if the frame can pass through specified bitrates).

Bosch PTZ cameras use OSRD protocol for controlling the camera. This protocol does not allow a change of iris/focus speed. So, irising and focusing can be performed with a predefined speed value. The speed values can be set via Web-interface. These settings for VG4 AutoDome camera may be found here: Settings > Advanced Mode > Camera > Lens > Setting Group 1

OSRD protocol does not allow you to delete prepositions. Also VG4 camera doesn't allow rewrite existing preposition without confirmation. The camera will show "Overwrite current scene?" question as OSD menu with [Yes] and [No] buttons.

Focus/Iris changing is used for selection confirmation. The driver sends Iris command after preposition saving to avoid a user from manual confirmation of preposition rewriting. This algorithm has an issue: if the preposition slot is empty (not stored yet), you will see Iris changing text.

Bosch video servers pass PTZ commands to cameras, connected through serial port. There is no way to configure the camera's identifier via standard server options. So, connected cameras should be correctly configured (camera's hardware settings) for enabling PTZ control:

PTZ protocol should be Pelco-D

PTZ camera identifier should be the same as the video channel's number. For example, for a camera connected to the second video input, the camera ID should be set to 2.

Other serial port settings should be equal to the server's (baud rate, parity bit, stop bit, etc.).

Bosch video servers have no internal PTZ functionality. It only passes commands to their serial ports with connected cameras. So, the driver cannot detect the capability connected to the serial port camera and whether it is PTZ.

All server video channels will be shown as PTZ because of this feature.

NBC255 and NVC255 have VGA and QVGA resolutions. DVMS will show D1 and CIF instead. (Cannot detect those models from device properties)

Multiple streaming is done according to the encoders' capabilities.

Each video channel has two encoders with the number of supported resolutions, so not all resolutions are available for Recording and Live streams.

Some resolutions are supported only by special combinations on the first and second encoders, so the Live stream resolution can differ from the settings if it cannot be set with the current Recording resolution.

The remote stream is MJPEG; it has all available resolutions.

Streaming limitation

To change H.264 resolution and framerate for secondary stream is it required to disable the "Copy Stream 1" mode in the Web Interface (Settings -> Advanced mode -> Camera -> Encoder Streams -> Stream 2 -> Property will NOT be in the "Copy Stream 1" state for the "Stream 2");

It is not possible to apply several resolutions (each video channel has two encoders with different sets of supported resolutions);

Remote stream is MJPEG that has all available resolutions.

MJPEG in multiple streaming mode does not work for old series with firmware 4.x

Motion detection for PTZ cameras should be configured on camera's Web page after each camera movement (Bosch limitation).

Privacy zones for PTZ cameras are not supported.

Cameras that have COM port will be shown as PTZ in DVMS. They can be connected to PTZ platform and PTZ will work.

Driver synchronizes PC's time with camera using UTC (GMT+00:00) time for Edge-Storage functionality. Edge-Storage will not work correctly if time will be changed to another one.

Edge-Storage functionality works only for network loss situations between camera and VMS.

  If VMS was restarted or driver was closed - VMS will not receive recorded video from camera.

  Also, recording should be configured on camera to use Edge-Storage functionality in VMS.

Multicast capture limitations

The driver instance can be configured to be used as Active or Passive. Active instance is able to change IP device settings and use additional functionality. Passive instances are able to receive video streams and audio stream by multicast and allows to use digital I/O functionality.

The Passive will not change following camera settings:

Codec

Quality

Resolution

Framerate

    The camera should be added to Active recorder before using in Passive configuration.

User should guarantee that only one recorder will change settings of the camera. Other recorders which use this camera should be in Passive mode.

It is required to specify IP address of the network adapter through which camera is connected to receive multicast streaming correctly in case if more than one network adapter is available. The network adapter marked in Windows as default will be used if no option configured. For audio channel network adapter (in case of several network adapter used in PC) should be set in XML file, dynamic UI is applied only for video channel.

Time Synchronization is disabled for the Passive and Edge Storage may not work properly.

Use should guarantee time synchronization for PC with Active mode recorder and PC with Passive mode recorder.

Old Bosch series with firmware 4.x have the following limitation:

HTTPS mode does not work

MJPEG in multicast mode does not work (only JPEG requests over HTTP)

Privacy zones for firmware 6.22 are not supported.

Old Bosch series (like Gen4) do "auto bounding" sometimes. During this process stream from camera is not fluent.

In Passive mode old cameras with MPEG4 support should be set to correct compression format or "No signal" will be shown.

Edge storage recording should be set to 1st edge storage stream on camera's Web-interface.

The Bosch IP devices may return no information about audio intervals recorded on device's storage via RCP+ requests (by num = 90 + channel ID). As result Audio Edge functionality will not work correctly. The issue was reported to Bosch technicians (at 20/Nov/2019), but there is no solution yet.

Not all Bosch cameras can detect Motion, so it should be cheked on camera's web page if it supports Motion Detection or not

To use camera in secured mode

Install certificate on camera and PC with Recorder

Set RTP over HTTP streaming mode in camera settings in System Manager;

Set correct camera credentials (for sending audio to camera, if it is not needed - any credentials can be used, authentication will be done using certificate); audio to camera is not secured, so it needs correct credentials to work.

Bosch camera with H.264 and H.265 support should be set to required codec before adding to DVMS, because some cameras have different list of supported resolutions / framerates for each codec.

Camera supported resolutions depends from currently set codec (H.264 / H.265). So, camera will be added with currently selected codec, DVMS will not change it during camera add.

Video loss check is used only for encoders with analog cameras to detect that camera is working or not. It should not be used for other Bosch devices.

If audio codec was changed, need to format SD card, because driver will try to receive audio using current settings. If AAC is set to camera but recording was done for G711, edge audio data will not be received correctly.

If multiple streaming is used, all channels should have the same codec (H.264 or H.265), Bosch cameras can not stream both at the same time. 

Bosch devices are not processing RTSP PAUSE command correctly (continue to send stream after that).

So, we use RTSP TEARDOWN to stop stream if no motion (when camera based MD is in use).




Pagination
Previous page
NewAxisIPCapture installation and usage
Next page
NewIQEyeIPCapture installation and usage