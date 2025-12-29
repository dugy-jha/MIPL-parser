# Failover Servers | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/failover-servers

Failover Servers

❗ If you need to failover also the VCA channels, the failover server must contain the correct amount of the activated VCA channels.

Mirasys VMS supports failover video servers as a Mirasys VMS option.
Failover servers are VMS Servers on a passive standby until the system recognizes that one of the active video recording VMS Servers has broken down; at this point, a failover server takes the place of the broken server.
The failed server can be repaired and replaced as a new failover server, while the failover server that took its place can continue operating as an active server.
Note: When a failover server takes the place of an active server, any Spotter plugins (such as Grafana or List Management Application) that are not built-in are not included in the switch and must be re-installed manually after a server restore. 

Recording and failover servers should be of a similar hardware setup and share drive letter assignments and version numbers.
Analogue cameras connected to a server’s capture card will not be transferred to the failover server. Only previously assigned IP cameras are reassigned during the switch.

Failover Functionality

When adding a new server into the system, the administrator can select whether the added server is a standard server or failover server.
There can be any number of failover servers (0-n).
If the server is the standard server, the administrator can choose if that particular server will be added to the failover monitoring, i.e., in case of server failure (hardware or software), this server will migrate to the available failover server.
It is important to note that the Master server needs to be installed on hardware separate from those operating with recording licenses or failover licenses.
The minimum hardware setup consists of three servers: one Master Server, one video recording VMS Server, and one standby failover server.

Failover migration will be triggered in the following conditions:

The Master Server has lost the connection to a VMS Server, and the timeout set by the administrator has been reached

A VMS Server has informed the Master Server that connection to all the material disks (recording storage) on the server has failed

Manual data recovery from server hard drives can be attempted if the disks are still functional

A server’s Watchdog service has informed the Master Server that it cannot initialize the recording service

A recording is continuous after the failover server has taken over to keep the system operational.
The only exception is the timeout time between disconnect and failover trigger. The administrator configures this.
After a failover server has assumed the recording role of a failed server, a system backup will automatically be created to set a new baseline.

During the failover restore process and the following system backup:

Users cannot perform manual backup operations

Any following broken servers are added to a failover queue 

The failover queue is handled after the failover restore has been completed.

Failover summary since V9.5.0

In V9.5.0 VMS, failover functionality was renewed to work quicker than before. It can be triggered manually. In the same version, failback functionality and material copying from failover server to recorder after failback was also implemented.
Failover log was also added where the user can see all occurred failovers and how those are processing, and the user can also trigger failback and material copying manually.

Description

Failover in V9.5.0 was changed not to use system backup files. Instead, SMServer will store recorder settings with schedules and motion masks to recorder settings cache and uses these settings when doing the failover.
Recorder settings, schedules and masks are requested from the recorder when SMServer makes connection to the recorder.
As a part of the making failover quicker, recorder startup was also optimized to start as quickly as possible.

There are now also smaller network disconnection detection times added. In earlier version the smallest time was 1min, but now there are options for 10s, 20s, 30s, 40s and 50s.

Recorder settings cache

Recorder settings are cached to folder "C:\Program Files\DVMS\SystemManagement\RecorderSettingsStore"

Recorder masks are cached to folder "C:\Program Files\DVMS\SystemManagement\RecorderMasksStore"

Recorder schedules are cached to folder "C:\Program Files\DVMS\SystemManagement\RecorderSchedulesStore"

Failover process

When failover is started (triggered manually by user, by network connection lost or by critical recorder failure), SMServer will do following operation

Check if there is failover server available that belongs to same failover group as failed recorder and there is connection to the failover server

Creates failover log entry about the failover

Get settings, masks and schedules of the failed recorder from recorder settings cache

Saves failed recorder settings to failover server

Makes changes to system data that failover server has taken the tasks of the failed server

Makes changes to the system data that failover server is now acting as normal recorder and failed recorder is in broken state

Sets failover progress result to failover log

Sends system change notification to clients

Manual failover triggering

User can trigger manual failover from System Manager UI in recorder settings tab. Manual failover is possible, if

there is connection to a failover server that belongs to same failover group as the selected recorder

selected recorder has failover enabled

User has role that allows to trigger failover manually

Select the broken VMS server from the list

Click Start failover from selected VMS server to the failover server




Pagination
Previous page
Using TruCast
Next page
Minimum requirements