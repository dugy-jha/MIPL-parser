# PelcoIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/pelcoipcapture-installation-and-usage

PelcoIPCapture installation and usage

Driver uses RTSP/RTP/UDP/IP protocols for MPEG-4, H.264 video receiving.
HTTP protocol is used for parameters setting/retrieving, JPEG video receiving
and for PTZ functionality.

If there is a firewall between VMS and the cameras, the following RTSP/UDP/HTTP
ports must be opened:

HTTP: default port is 80 for Sarix cameras and 49152 for non-Sarix cameras,

RTSP: port 554,

UDP: Two sequential ports per video stream is needed in a port range 3556 to 4556.

TCP: 3549 is default port for GENA DigitalInputs notifications.

Please also see the PelcoIPCapture.xml, DigitalIOListener section, port value

For example: if there are 4 Pelco cameras in a VMS, then ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 and 3563 will be used. If a port is not free, it will be skipped.

For the Sarix, Endura and the newest series driver from vesrion 1.8.0.0 will use GENA notification architecture. The driver will automatically configure Windows Firewall to allow incoming connections to DigitalIOListener port. See also addFirewallRule option.

The "DigitalIOListener" section, "address" and "port" options can be used to specify external IP address and port in case port forwarding from external network to the same TCP port.

Limitations

Quality and resolution configuring for JPEG codec for non-Sarix cameras are not supported. All JPEG images will be received in 4CIF. SystemManager camera settings will be ignored in this case.

Pelco Sarix cameras allow to access them via SOAP requests without user authentication by default. So, any unauthorized user can subscribe and configure Pelco Sarix camera. To avoid such behavior please set "Public User Access Level" setting to "Disabled" on Users tab in Web-interface.

Firmware version cannot be retrieved from Pelco IP cameras. This is a feature of Pelco API.

Pelco cameras apply video stream settings approximately 30 seconds. So, CCRiA and CCFiA features cannot be implemented for Pelco IP cameras.

Sarix MPEG-4 encoder doesn't support resolutions greater than 704x576. The driver automatically sets resolution to 704x576 if user tries to apply any greater resolution.

Driver cannot receive number of inputs and/or outputs for IP110 camera from time to time. To fix this problem try to remove camera from the camera list and then add it again.

Actual framerate for JPEG compression may be less than required framerate,because frames capturing over HTTP has delays.

IO functionality for SARIX cameras does not work properly at the moment. The states of the inputs cannot be retrieved. The output component does not work properly because input states are unknown.

List of supported frame-rates may differ for different codecs for Sarix cameras. In case if user tries to apply unsupported frame-rate value, the next greater frame-rate value will be applied (for example, 7.5 value will be applied instead of unsupported 6 value). If user tries to apply greater value than maximal supported value, the maximal value will be applied automatically. Please refer to camera's Web-interface to view list of the supported frame-rate values.

Speed parameter is not supported by Pelco PTZ IP cameras for the following PTZ functions:

Focusing;

Zooming;

Iris changing;

Moving to preset position.

  So, the driver will use these functions as is: camera will process them with constant speed in all cases.

Spectra HD camera sends H.264 video stream with lower frame-rate than required (for example real 1 fps instead of 4 fps applied) in case if frame-rate value is even. Most of odd values (except 1 and 25) are processed correctly. This is a firmware issue.

The driver is unable to parse SOAP response from camera if any non-standard symbols (like umlauts or hieroglyphs) are used in configuration names. Using of these symbols may cause incorrect driver behavior, so please avoid using of these symbols when configuring Sarix camera via Web-interface.

Pelco 1080p cameras may not send H.264 encoded video stream with 1080p resolution for low frame-rates (from 1 to 4). This is known issue of Pelco firmware. Please refer to Pelco Knowledge Base for details:  <http://www.pelco.com/sites/global/en/sales-and-support/faq/faq_main.page?AID=12392>

 To resolve the problem in VMS software please apply the lowest quality for these settings.

The GetAlarmStates call used for digital input querying is deprecated and is not recommended for commercial use by Pelco support team. Querying of digital inputs every 2 seconds may cause camera hanging after 2-3 days of working. So, the digital input functionality is disabled by default, but it may be enabled via XML configuration file in case if it will be required.

  It may be required to re-add the camera after configuration file change.

Port 3549 should be allowed for incoming connections in the Windows Firewall for the DigitalIO functionality for the Sarix, Endura and higher series. See also PelcoIPCapture.xml, DigitalIOListener section, port value.

Older versions of the cameras have a problem if the Digital Outputs requests are sent very often. If the user configures the frequent changes the Output (more often than one switch per minute) the camera may hang after several days. To avoid this issue please disable Digital Outputs functionality using driver configuration file.

Pelco Optera series Panoramic IP cameras (IMM12018, IMM12027 and IMM12036 models) have specific implementation of stream dewarping which was not integrated with native driver yet.

Please use ONVIF IP Capture driver instead for this device series.




Pagination
Previous page
OnvifIPCapture installation and usage
Next page
PSIAIPCapture installation and usage