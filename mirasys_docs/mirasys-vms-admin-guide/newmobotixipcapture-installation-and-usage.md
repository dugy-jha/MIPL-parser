# NewMobotixIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/newmobotixipcapture-installation-and-usage

NewMobotixIPCapture installation and usage

In all compression modes the driver uses HTTP protocol for video receiving and for parameters setting/retieving.

If there is a firewall between DVMS and the cameras, the following ports must be opened: HTTP: default port is 80.

Limitations

Real FPS is limited with resolution settings (camera feature): greater resolutions have lower real fps values. For example, for 800x600 resolution maximal FPS is 9 for MJPEG codec.

The audio data may be received as part of MxPEG frame according to HTTP API documentation. So, audio stream is not available for MJPEG stream.

Stream mode changed from "fast" to manual - this setting can be changed in the web-interface.

Pagination
Previous page
NewIQEyeIPCapture installation and usage
Next page
NewPanasonicIPCapture installation and usage