# Mirasys VMS V9.2 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-2-release-notes

Mirasys VMS V9.2 release notes
What’s new?
PTZ camera groups for all home position 

In Spotter there is the possibility to run all profile PTZ cameras to home if the user has the Spotter user role. This operation can be done from UI (Devices ribbon), shortcut and from the input device. 

Bookmark improvements
User rights

Following new user Spotter roles were added:

Possibility to run all current profile dome cameras to their home positions (if camera dome profile setting flag: IsDomeTakeControlAllowed,​​ is set). 

Role can set in Spotter roles -> Devices -> Dome cameras. Default value is false.

New bookmarks editing and managing roles:




Bookmarks handling improvements
Password protect

When saving a shared bookmark, password protection is possible to add in the bookmark.







When opening for viewing shared, password-protected, bookmark first time under session (or after settings changed refresh) password is asked.




Multi-select for bookmarks

It is now possible to select multiple bookmarks for operations:




Add bookmark to storyboard

Bookmarks can now easily be exported to a Storyboard:




Add or exclude bookmarks from export

By default, bookmarks are included in exported clips




Clip reuse in Storyboard

It is possible to import media clips to the storyboard

Supported media file formats are: .sef, .sef2, .esef

If the imported media file is password protected, then the password is asked during import

Imported media clips are added to the end of the storyboard, and the storyboard description is replaced with the imported storyboard clip description (if it is not empty)

Bookmarks are imported too from the media clip

Imported media clips can be edited in the storyboard, and exported to a new storyboard clip

Imported media clips are included also in storyboard draft files

The storyboard preview window can show also imported clips. A storyboard cannot be edited while the preview window is open.

Spotter person search plugin (optional)
Description




There are three modes

Playback mode: all persons are detected (this is the default mode)

Person search mode: the selected person is searched from played videos

All persons search mode: search all persons, try to display the same person only once

Thumbnails

Found persons are shown in a thumbnail list. There are separate lists for all persons and selected person search results.

Thumbnail mouse click (or Enter key) shows the thumbnail location in the video

Thumbnail mouse double click opens the thumbnail video playback in the new tab

Known limitations

The current version does not allow using other plugins with the person search plugin. This means that the following features are unavailable:

Zooming

Auto crop

360 image de-warping

VCA engine update

Find full documentation in our V9.2 - VCA Installation and Configuration Guide
V9.2 has an updated VCA engine. It is strongly recommended to perform a settings backup before the update and restore the backup after the update.
In rare cases, we experienced VCA license problems. Please contact support for further information.

Alarm, audit trail and watchdog event database retention times

It is now possible to configure the retention time of the events in the alarm, audit trail and watchdog database. 
This can be configured in the Database.xml configuration file.

V7 file system support

​DVMS V9 has a new file system format that is incompatible with V7 but to make it easier for customers V8310 and later versions have an option to work with V7 file system support.

DVMS installer

Filesystem support selection is done during DVMS install in this dialogue:




Use File System V7 or older - old storage will be used in V7 format without any changes to its structure, all calls to the V7 file system will be passed over new API -> old API wrapper. All previously recorded data (video, audio, text, alarms etc.) will be accessible after the DVMS update.

Use File System V8/V9 and remove old data - old storage will be erased and will be formatted to new File System format, all previously recorded data will be lost.

Use File System​ V8/V9 and leave old data - old storage will be left as is, but DVMS will be configured to use the new File System format. This is useful if there is some additional disk that can be used for new data and there is some need to keep old storage for some time to access previously recorded data. Previous data can be opened as an archive in Spotter, the installer will create archive information if this option will be selected in the installer. 

Notes for installer option 3 (Use File System V8/V9 and leave old data)

If there were several disks used in DVMS V7 then each disk will be opened as a separate archive in V8 or later after the DVMS update.
DVMS V7 has a recording mechanism similar to RAID 0 (stripe recording) but in this case, it writes 1st second to one disk, 2nd - to another, so as a result if each disk is opened separately it will have gaps in places where those data is written to another disk.

If text channels are used in V7 then to generate archive information correctly DVMS V8 or later should be installed on top of V7 (without V7 uninstall).
If V7 will be uninstalled first - text channel event names and search tags information will not be written to the archive information file.
Also if V7 will be removed with the "Remove settings" checkbox set then also channel names, manufacturer and other information will be lost, so archive information will be generic (like Camera 1, Audio 1 etc.)​

Notes for alarm database

​If V7 is updated to V8 then the alarm database is recommended to be removed, so the option "Yes" should be set to this installer dialogue:




If the SMServer alarm database is not updated, old alarm entries will remain in the alarm database in SMServer, but the alarm material stored on the recorder side is not available.
It is anyway highly recommended to update the alarm DB when upgrading to V8/V9.

Limitations

​DVMS with V7 file system support has those limitations:

Can't launch several archiving processes at the same time, so if the timed archive was launched - the manual archive will fail until the first process will be finished.

If disk connection will be lost or disk will be unplugged and plugged again - it will not be recovered back until DVRServer restart.

Future file system features will not be supported

Support for Axis joystick jog wheel and keyboard

Axis device driver supports AXIS T8311 Joystick, AXIS T8312 Keypad and AXIS T8313 Jog Dial.







Online help link to Spotter and System Manager help

DVMS applications have a link to online help to Mirasys documentation and training platform.


Other minor changes

Better visualization for selected camera

Better visualization of bookmarks

Support for 1x1 fixed grid

Support for longer auto log off and lock times

Support for larger AVM setup (12x6 Display Servers)

Windows event logs included in the log export

Changelog V9.2 - 2021/03/31

Optimizations to failover and setting restore

Optimizations to VMS server thread usage

Optimizations and fixes to AVM usage

Fix: Motion search plugin improvement

Fix: Alarm email image generation 

Fix: Spotter bookmark edit doesn't work correctly if DirectX drawing is used

Fix: Gateway image decoding issues

Fix: Support for all codecs in Gateway

Fix: Gateway playback skips images

Fix: Alarms not found from old master alarm database

Fix: Export user roles not set correctly in System Manager

Fix: Several fixes to Spotter layout loading

Fix: Old capture card settings handling in System Manager

Fix: PTZ tour as home position stops after a few minutes

Fix: VCA tampering event sent multiple times

Fix: Continuous recording causes 100% CPU load

Fix: Spotter crash when switching user

Fix: System Manager crash when saving storage settings

Fix: Joystick default setups works only in English Windows

Fix: Alarm popup works incorrectly with alarms that last only a short time

Fix: Spotter crash when saving Spotter settings

Fix: Spotter stuck when closing Spotter window

Fix: Spotter map images are updated only after Spotter restart

Fix: Several optimizations and fixes to Spotter camera carousel plugin

Fix: Spotter crash when closing camera audit plugin

Fix: Several fixes to small Spotter memory leaks

Fix: Get tab content failed from Spotter Pubic Web API

Fix: Old pre-recoding footage not removed correctly

Fix: Cannot use the digital output in Spotter grid

Fix: Edge storage not working correctly

Fix: Long prerecording not working for megapixel cameras

Fix: Spotter crash on storyboard draft save

Fix: Error loading VMS server settings System Manager

Fix: Creating a bookmark from the alarm in Spotter does not work correctly

New Hikvision driver

New Bosch driver

New Wisenet driver

New Mobotix driver

New Universal Data Driver

Other minor and cosmetic changes

Pagination
Previous page
Mirasys VMS V9.3 release notes
Next page
Mirasys VMS V9.1.1 release notes