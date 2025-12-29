# AVM DS Spotter configuration | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-video-wall/Video-Wall-Guide/avm-ds-spotter-configuration

AVM DS Spotter configuration
Log Each DS User In (Run as Administrator) 
Use automatic login 

Open File

Click Settings

Select General

Enable Use automatic logon

Enable External AVM API (Needed ONCE for ALL DS and OC – ALL WINDOWS USERS!)

Go to the Advanced tab

Enable External AVM Api

 If the default 8084 port is used (very rare case) you can change to another port (then has to change all machines to the same port)
 Netstat -a

Allow traffic for configured AVM API port 
Make sure the firewall does not block IP traffic to 8084 port!

 Easiest is to disable the firewall (IN ALL MACHINES, OC AND DS, but you could also make a hole for 8084 (or another port if you need to use another port)

Pagination
Previous page
AVM DS configuration process
Next page
AVM OC configuration process