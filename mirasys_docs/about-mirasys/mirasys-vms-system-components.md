# Mirasys VMS System components | Mirasys Help Center

Source: https://documentation.mirasys.com/about-mirasys/about/mirasys-vms-system-components

Mirasys VMS System components
System servers

Servers are devices configured to perform tasks and play specialized roles for a networked system.
These devices are usually desktop computers or specialized computer hardware that can be placed in server racks, but they can also be virtual devices running within another computer’s programs.
They often run operating systems or software that maximizes their performance in their tasks.
In the VMS, servers are devices that run Mirasys server services that form the basis of the system.
Actual server hardware requires little specialization, with the exception of devices meant to run DVRServer requiring two NICs and lots of digital storage space.

Note that the 8.5 and newer versions of Mirasys VMS also need a DNS (Domain Name Service) server to work properly.
It’s used for hostname searches during the logins with client software, and with connections between servers.

Failover servers

Mirasys VMS 7.0 and later releases support failover servers.
Failover servers are networked devices that are on a passive standby until the system recognizes that one of the active Slave servers has broken down; at this point, a failover server takes the place of the failed server.
The failed server can be repaired and replaced as a new failover server, while the failover server that took its place can continue operating as an active server.
Currently, only Slave servers can be placed under failover protection, as Failover Server is not yet configured to replace failed Masters running SMServer.

Failover servers expected to function as recording Slave servers must have the same file system (same drive letters) as the Slaves under failover protection, and they can only be used for IP camera backup purposes.
When in standby mode the failover servers appear under a separate folder in the server list.
When any Slave is deemed to be broken or inaccessible, they are moved under the “broken recorders” folder and any available failover server takes on the responsibilities of the broken Slave.
Failover settings can be controlled from the general settings of the Slave.
The failover transition is done if all material disks on the affected recording server are broken or the Slave is inaccessible for longer than a user-defined period of time.

Note: When a failover server is taking the place of an active server, any Spotter plugins (such as the ANPR+ license plate recognition software or Activity Map Plugins) are not included in the failover switch and must be re-installed manually after a server restore.
Contact Mirasys for more information on failover functionality and licensing.

Pagination
Previous page
Mirasys System Services
Next page
Glossary