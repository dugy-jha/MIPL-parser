# More Than One Server Behind Router | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/more-than-one-server-behind-router

More Than One Server Behind Router

Scenario 2: More than one server behind a single router (WAN address)

If the user configures a more extensive system with multiple servers on a single site, he can add the servers to the System Manager application with the external or internal IP addresses.
When adding a new VMS Server, if the server has done automatic port forwarding, a note shows that he can choose between an internal IP address and an external IP address.
If the server is to be used from the WAN, then the external IP address should be chosen.
The exact ports that the server has done port forwarding to can be found by starting the System Manager on the local server.
When adding a server to a Master Server when not on the local site (cannot use the local IP address), the user must know the external IP address and know the first port that the port forwarding was done to.
If the added server is a single, standalone server, the port is most likely 5009.
If multiple servers are on the same site, they most likely get the ports starting with 5009, 5013, 5017, 5021…

Pagination
Previous page
Single Server Behind Router
Next page
More Than One Server On Multiple Sites