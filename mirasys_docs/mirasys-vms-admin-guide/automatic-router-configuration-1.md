# Automatic Router Configuration | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/automatic-router-configuration-1

Automatic Router Configuration

When a VMS Server starts up, it tries to discover UPnP devices from the network.
The router needs to support UPnP (Universal Plug and Play), which must be enabled on the device.
The server has continuous UPnP device discovery when running, so if any network changes are done, the server will automatically detect new routers and do port forwarding to them.
Only UPnP devices with external (WAN) addresses are detected.

If the user wants to remove port forwarding automatically, he can do this from the system manager.
After this, the server will remember that the settings were removed and not port forward to this router.
The software does not allow to delete port forwarding mapping if the server is added to the system with an external address.

Deleting the port forward mapping would disconnect the system, and no further configuration would be possible.

If forward port settings are changed, and the connection to the server has not returned after a while, it might be necessary to reboot the router.

Servers need four ports for the server to server communication. The first server that does port forwarding will claim ports 5008, 5009, 5010 and 5011.

The second server will claim ports 5012-5015, the third server ports 5016-5019. And so on. (Assuming all the ports are available).

The first port is used for SMServer communication (5008, 5012, 5016…)
The second port is used for DVRServer process communication (5009, 5013, 5017…)
When connecting to a Master Server, the port is typically 5008. When adding new servers to the master, the port is typically 5009. If there are more than one server on-site, then the ports are 5009 +4, 5009 + 8 etc.

Pagination
Previous page
Port Forwarding
Next page
Single Server Behind Router