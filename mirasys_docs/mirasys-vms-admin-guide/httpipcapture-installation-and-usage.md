# HTTPIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/httpipcapture-installation-and-usage

HTTPIPCapture installation and usage

The driver uses the HTTP protocol to receive video streams from IP devices.

The driver expects the HTTP URI to be added to the device and placed in the "IP Address" field.

The required port may be specified separately in the "Port" field or in the HTTP URI. The HTTP URI port has a higher priority; if it is set, the DVMS port field will be ignored.

The stream URI requirements: The HTTP URI should be specified in full format, e.g., http://192.168.1.70:8080/video

Stream URI may be checked over third-party players, like VLC.

Limitations

If the camera requires Basic HTTP authorization, the correct user name and password should be set; otherwise, there will be no video.




Pagination
Previous page
GatewayIPCapture installation and usage
Next page
IPCameraCapture installation and usage