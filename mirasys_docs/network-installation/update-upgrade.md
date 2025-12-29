# Update & Upgrade | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/update-upgrade

Update & Upgrade
Updating a Server 

To update a server, first, remove the current software version and then install the new software version.

Back up system settings and server settings in System Manager before removing the current version and then restore the settings after the update is completed.

To remove the current server version:

Backup existing Mirasys VMS settings using → Backup\Backup settings

Click Start, point to Settings, click Control Panel, and then double-click Uninstall programs.

Click DVMS and then click Uninstall

DVMS installer

Filesystem support selection is made during DVMS install in this dialogue:

Use File System V7 or older - old storage will be used in V7 format without any changes to its structure. All calls to the V7 file system will be passed over the new API -> old API wrapper.

All previously recorded data (video, audio, text, alarms etc.) will be accessible after the DVMS update.

Use File System V8/V9 and remove old data - old storage will be erased and formatted to a new File System format. All previously recorded data is lost.

Use File System​ V8/V9 and leave old data - old storage will be left as is, but DVMS will be configured to use a new File System format.

This is useful if there is some additional disk that can be used for new data, and there is some need to keep old storage for some time to access previously recorded data.

Previous data can be opened as an archive in Spotter. The installer will create archive information if this option is selected in the installer.

Notes for installer's option 3 (Use File System​ V8/V9 and leave old data)

If there were several disks used in DVMS V7, then each disk will be opened as a separate archive in V8 or later after the DVMS update.


DVMS V7 has a recording mechanism similar to RAID 0 (stripe recording).
Still, in this case, it writes 1st second to one disk, 2nd - to another, so as a result, if each disk is opened separately, it will have gaps in places where those data is written to another disk.

If text channels are used in V7, then to generate archive information correctly, DVMS V8 or later should be installed on top of V7 (without V7 uninstall).

If V7 is uninstalled first - text channel event names and search tags information will not be written to the archive information file.

Also, if V7 will be removed with the "Remove settings" checkbox set, then also channel names, manufacturer, and other information will be lost so that archive information will be generic (like Camera 1, Audio 1 etc.)

Notes for alarms database

If V7 is updated to V8, then the alarm database should be removed, so the option "Yes" should be set to this installer dialogue.

In another case, the alarm database will not be updated, and previously recorded alarms will not be fetched from file storage.

Limitations

DVMS with V7 file system support has those limitations:

Can't launch several archiving processes at the same time, so if the timed archive was launched - the manual archive would fail until the first process is finished.

If disk connection will be lost or disk will be unplugged and plugged again - it will not be recovered back until DVRServer restart.

Future file system features will not be supported

Updating Client Programs

The client programs are updated automatically to the same program version as the Master Server when they are started.
To manually update the client programs, remove the current version and install the new version by running the VMS installer.

To remove the current version:

Click Start, point to Settings, click Control Panel, and then double-click Uninstall programs.

Click DVMS and then click uninstall and then review the installation instructions earlier in this Guide.

Updating VMS Servers From Master server

Updating VMS Servers remotely through the Master Server has been possible since Mirasys VMS 6.2.5.

Update the Master Server to the latest version. In the System Manager, edit the licenses for the individual VMS Servers through the 'Licenses' list in the 'System' tree.

After updating the licenses, you can update the VMS Servers remotely using the 'Update servers' tool in System Manager.

In case the VMS Servers have an earlier version, you need to install Mirasys VMS 6.2.5 or newer on them manually to enable remote server updates.

In some cases, the VMS Servers might need a restart of the PC after a remote software update.
Monitor the servers after a remote update, and if they do not return online in 10 – 15 minutes, restart the PC they are running on.

Please remember the different 32-bit and 64-bit versions when doing remote updates. If a system is partially 64-bit, do not push a 64-bit update to all servers.

Updating Components

In addition to camera drivers and Spotter Plugins, it is possible to also update metadata drivers from the System Manager.

Spotter Plugins are updated by removing the old version and adding a new version *.spi file to the system.
Metadata drivers offer the possibility to update the drivers to the whole system or only selected servers.

Contact Mirasys for more information on available metadata drivers and updating them.

Pagination
Previous page
Mirasys Gateway Server Installation
Next page
Upgrading VMS version