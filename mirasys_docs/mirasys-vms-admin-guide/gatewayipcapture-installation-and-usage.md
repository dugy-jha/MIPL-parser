# GatewayIPCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/gatewayipcapture-installation-and-usage

GatewayIPCapture installation and usage

The driver uses TCP/IP protocols for video receiving and parameter setting/retrieving in all compression modes. The default Gateway TCP port is 9000. If there is a firewall between VMS and the servers, this port must be opened.

A separate profile (not service) should be used for the Gateway driver. This can be configured in the GatewayIPCapture.xml file (Profile name). Otherwise, the count of used cameras can be incorrect.







Pagination
Previous page
EIPCapture installation and usage
Next page
HTTPIPCapture installation and usage