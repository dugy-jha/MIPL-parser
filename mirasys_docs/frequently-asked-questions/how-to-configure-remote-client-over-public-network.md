# How to configure remote client over public network | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-configure-remote-client-over-public-network

How to configure remote client over public network

When there is the case that there is a need to configure remote clients using a public network.
Spotter software is streaming camera images directly from the server. 
If there are multiple servers where the remote client needs to contact, then it's recommended to build a VPN connection between servers and remote clients.
In this guide, we are looking at how to configure server and remote clients over a public network.
These next ports need to open from the public network to the VMS server

5008 - 5011 TCP

On the server-side, you need to change the VMS server address to pointing the server DNS name.

To change this double click Change VMS server addresses

This opens a new window where you can edit the recorder address. To change this click the Change VMS server addresses button.

This opens a new window where you can fill New VMS server address. On default this show server DNS name.

When a new server address is filled, you can apply these settings.

Now when settings are applied, the next step is to edit the remote client hosts file. Default location for this file is C:\Windows\System32\drivers\etc. 

To edit this file you need to use Notepad as Administration rights or copy-paste this file to Desktop and edit there using Notepad.

Add the end of this file line where is told what is server public WAN IP address and server DNS name which has applied earlier.

When this new line is added to the file, you can save it and then open Spotter and connect this DNS name.
You may need to edit Spotter connection settings to pointing this new address if this is not done before.
When Spotter has made the connection to this new address, it automatically checks that files are good to go and make a connection to this server.
If all ports are forwarded correctly Spotter shows camera images from this server.

Data Encryption

There is also possible encrypt communication between the server and remote client.
This can be done in System Manager and in General system settings.
To get these settings you need to open System Manager and double click General system settings which open a new window.
On this new window, you can enable Data encryption and apply these settings.
After this communication between the server and remote client is encrypted.

Pagination
Previous page
How to edit host file
Next page
Check HDD/SSD/M.2 health