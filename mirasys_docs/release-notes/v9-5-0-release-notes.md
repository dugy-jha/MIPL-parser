# Mirasys VMS V9.5.0 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-5-0-release-notes

Mirasys VMS V9.5.0 release notes
Release date: 4.7.2022




What’s new?
Failback

With the Failback feature, the user can quickly move the server functionality from the failover server back to the fixed server.

The user can trigger Manual failback from the failover log.

Automatic or manual material copying

Users can also start material copying from the failover server to the fixed server. This way, the user can secure that materials, which Mirasys VMS server has been recorded can be found.

RTSP Server

RTSP/RTSPS server is used to stream video from the server to any third-party client that supports RTSP/RTSPS protocol.

Failover log

We have added the Failover log feature to the UI in System Manager. Using the failover log administrator can see active and finalized failovers and start manual failback &manual material copying from the failover server.




What's improved?
Shorter time to set to go on PTZ home position

New added values; 10 s, 20 s, 30 s, 40 s, 50 s

Alphanumeric sorting of device and device groups in the profile ( a -> z)
Remove PTZ and take control of prompts and warnings.
Added the filtering by list type to the live view to the Easy LPR

Now the user can filter which lists are shown in the Easy LPR live view.

More extended periods to playback time limit added

Values 1-10 days, 15, 15, 20, 25 and 30 days added 

Added button to copy pre- and post-recording times to all cameras

The user can easily copy pre- and post-recording times to all cameras.

We have renewed the failover functionality; it is much faster, and the user can manually trigger failover
Automatic lock/log offsetting was added to the user group level
Force user logout
Block deletion was added to the user settings

The administrator can now set the Block deletion to the specific user.

Windows Server 2022 support added
SQL Express 2019 included in the VMS Complete package




Fixes
VMS Server

Compatibility issue with old V7 recorders

Easy LPR and Axis LPV are not working correctly when daylight saving happens.

The camera's IO ordering was changed after the user saved server settings.

Spotter

The problem with the storyboard video clip playback

Real-time audio is stopped if one of the audios is closed.

Spotter Diagnostic plugin is not working correctly.

Spotter live cause audio click noises, no problem on playback mode.

Spotter AVM crash when trying to reserve PTZ control when that is already on.

Synchronization issue with video and audio when playing from exported clip

A spotter is using 100% CPU in a big system setup.

Easy LPR: multiple rows deleted

Invalid row in Easy LPR export data

Spotter Web

Add IO support to the Spotter Web Mobile version.

Spotter Web alarms are not working correctly.

Spotter Web cameras don't work after quickly switching between tabs.

Spotter Web streams don't start with correct parameters after logging in.

Spotter Web closes streaming when the controller server starts connecting to the offline server.

When adding four cameras or more using an Automatic grid, this remembers only the first camera when the user logs out and logs in.

Spotter Web can only log in if there is a Spotter role enable

Spotter Web's continuously streaming option does not work.

Pagination
Previous page
Mirasys VMS V9.5.0.5 release notes
Next page
Mirasys VMS V9.4.1 release notes