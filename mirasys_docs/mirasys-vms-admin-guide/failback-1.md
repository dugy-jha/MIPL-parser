# Failback | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/failback-1

Failback

Supported from V9.5.0

In V9.5.0 failback can be done either automatically or manually and there is no need to use settings backup to revert the failover.
The Failback uses same functionality as failover, but in reverse order by moving server functionality from failover server back to failed server. Manual failback can be triggered from failover log.
Automatic failback will trigger failback when automatic failback is enabled and connection to failed server is restored successfully.

Failback process

When failback is triggered (manually or automatically):

Check that there is valid failover log entry and the failover state in the log is correct

Check that failover server is still acting as normal recorder

Check that failed server is still in broken state

Check that failover is enabled in the license

Check that there is no ongoing failback process running for the failed recorder

Update the failover log that failback is started

Get failover server recorder settings, configuration files, masks and schedules from recorder settings cache

Set failed recorder settings

Mark failover server to act as failover server again and mark failed recorder to be in ok state

Update the failover log that failback has been performed

Send system change notification to clients

Manual failback triggering

Failback can be triggered manually from failover log. Manual failback is possible if

failover has performed successfully

failback is not in progress or failback is not performed already

user has role that allows to trigger failover manually

Automatic failback

Automatic failback can be enabled from server general settings when failover is enabled for the server. Automatic failback will not occur if maintenance mode is on.
Automatic failback is triggered when SMServer service connects successfully to failed server.
Failback functionality will then get all failover log entries from failover log database for the failed server where failover has been done successfully and failback process has not been done successfully and failback process is not ongoing.
If one or more log entries are found, failback process (described above) is processed.
If there are more than one failover log entry that fulfills the automatic failback requirement, newest log entry is used for failback process.
When the failback process have been successfully done, log entry that was used for failback is updated that failback is done successfully. For other log entries, failback and material copying are marked as done successfully.


Material copying from failover period

Material copy is done from failover server to main server, this task is added to server's processing using DVRFailoverService.

DVRFailoverService has those methods:

StartDataCopy - add new material copy task to server processing queue

UpdateClientInfo - update client information for server in case of connection between server and SMServer was lost to communicate with failover server correctly

UpdateFailoverTaskStates - update material copy state in case of connection between server and SMServer was lost

Server saves material copy task to database and process those tasks one by one. If some task will be failed, server save last task times and state and continue with other tasks.

What is copied during material copy for a specified time period (start of failover operation and end of failback operation):

Audio data for all configured audio channels

Video data for all configured video channels

Text data for all configured text channels

Metadata for all configured video and text data channels

ANPR data for all configured video channels

Alarms for all configured alarm id's

Server process each channel listed above one by one and save last received channel time. If connection between servers will be broken or some error will happen, recorder saves last state of material copy task and continue from last unprocessed channel (and last processed channel time).

Server use playback functionality for audio, video, text and metadata and ANPR and Alarms search services to get required data for specified time period.
Also, due to Geniune channels security limitations we can't use server as ZpaServer and ZpaClient at the same time, so calllbacks are not working in communication server to server.
So, ANPR and Alarms search services now have additional methods to get required data without using callbacks.

Failover log

Click Open failover log from the VMS servers tab

The Failover log shows Active Failovers and Finalized Failovers

Start Failback for the selected server

3. Set fixed VMS server to the network with the same IP address

4. Select the server from the list

5. Click Start failback to the selected server

When the failback is successfully done, Failback OK message with the start time, end time and duration is shown

Start material copying to the selected server

Select the server from the list

Select the first material copy, which has not been finalized from the list

Click Start material copying to the selected server

Pagination
Previous page
Building Failover system