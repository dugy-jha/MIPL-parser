# General | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/general-1

General

VMS server name

Description

Password

Protocol

Multicast Address

VMS server failover settings

Multicast address

When a single workstation stream is opened multiple times, the server – and the network – face unnecessary strain as each stream is treated as a separate entity.
Multi-casting enables a single stream to be opened and sent to multiple workstations simultaneously.
When using multi-casting, the stream for each video channel is sent to the LAN only once.
All applications on the LAN can receive the single stream, so network bandwidth usage is lower than when sending a stream for each application separately.
The feature needs to be configured in System Manager and through network settings.
Please refer to your network infrastructure service for information on enabling multi-casting support on the network level.

To configure multi-casting in System Manager:

In the server’s General settings, change the protocol from TCP (default) to RTP Multicast.

Edit the multicast address. 

Repeat steps 1-2 for all required servers in the system. Note: Each multicast address needs to be separate.

VMS server failover settings

When adding a new server to the system, it can be defined to be a failover server.
A failover server is a backup server that shall assume any server duties determined to be under failover protection.


Failover servers must have the same file system (same drive letters) as the VMS Servers under failover protection, and they can only be used for IP camera backup purposes.


When in standby mode, failover servers appear under a separate folder in the VMS Server list.
When any VMS Server is deemed to be broken or inaccessible, they have moved under the “Broken VMS Servers” folder.


Any available failover server shall take the responsibilities of the failed server.
Failover settings can be controlled from the general settings of the selected server.
The failover transition is done if all material disks are broken or the server is inaccessible for longer than a defined period. 

Use as a failover VMS server

This setting define that the server is used as a failover VMS server

VMS Server failover is enabled for this VMS server

This setting defines the selected server role that will be transferred to the failover server during the error situation

Delay failover to prevent data loss

During material copy from the failover recorder, the restored recorder checks its recorded data first, then copies only missing material (including video, audio, text data, metadata, and ANPR data).

This functionality can be enabled in the System Manager > VMS Servers General dialog, checkbox Wait for the recorder to apply settings).

Delay Failover can be enabled only for recorders V9.7 or newer, as recorders pre-V9.7 do not support selective material copy, and data will overlap.

Use automatic failback

This setting enables the automatic failback feature to this server

Use automatic material copying

This setting enables the automatic material copying feature to this server

For example, under failover protection, if inaccessible for longer than 2 hours, the failover switch would happen.




Pagination
Previous page
The VMS Servers
Next page
Port Forwarding