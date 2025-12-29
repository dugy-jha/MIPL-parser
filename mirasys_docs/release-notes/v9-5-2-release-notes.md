# Mirasys VMS V9.5.2 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-5-2-release-notes

Mirasys VMS V9.5.2 release notes
Release date: 20.01.2023
Optimizations 




System Manager

Optimized: Watchdog events data manipulation now works faster in big set-ups.

Optimized: System settings will not be updated unless changed.

Optimized: Unnecessary recorder settings loading removed.




Spotter

Optimized: Playback and activity calculation for timeline in the archive. Automatically opened streams limited to the first eight streams. Optimized: Storyboard limits increased to 180 streams per storyboard.

Optimized: CPU monitoring is turned off by default and can be enabled or disabled from the config file.

Optimized: Performance counters are turned off by default.







Fixes 




Recorder Server

Fixed: License checking in metadata stream.




System Manager

Fixed: Option added to support RGB drawing, which only works correctly with some Intel display adapters.

Fixed: Email sending to Microsoft Office 365.

Fixed: Storage settings show cameras correctly when there are gaps in the configuration.

Fixed: French and German translations.

Fixed: Channel indexing when there are gaps in the configuration.

Fixed: Diagnostics will not show Windows event logs in the log files drop-down list.




Spotter 

Fixed: Activity calculation and time zone usage in playback mode. The timeline shows the camera activities correctly, and playback shows the time with the correct timezone.

Fixed: Option added to support RGB drawing, which only works correctly with some Intel display adapters. 

Fixed: User handling in Spotter when changing users.

Fixed: Archive SDK and Spotter playback synchronizer on playback start.

Fixed: Dutch translations and German application texts.

Fixed: Thumbnail size calculation.

Fixed: Spotter DirectX joystick issue.

Fixed: PTZ commands are handled in the right order.




Spotter Web 

Fixed: Streaming management loading upon login after updating to the latest version.

Fixed: Dutch and German translations.




Gateway 

Fixed: Recorder activity search.

Fixed: MXPEG codec in Gateway TestSDKApplication.




Drivers  

Fixed: Licence Plate Recognition Service supporting Axis LPR version 2.4 and newer.  

Fixed: Trucast automatic settings in Spotter are working correctly with Axis.

Fixed: Axis EasyLPR handling time synchronization correctly.

Fixed: PTZ functionality from Axis Q3708 (PVE camera model)

Fixed: Bounding box information was added to Hikvision LPR detection events.

Fixed: Hikvision works correctly with PTZ functionality

Fixed: Bosch driver works with camera model FLEXIDOME multi 7000i.

Fixed: Dahua driver updated to work with the latest firmware.

Pagination
Previous page
Mirasys VMS V9.5.3 release notes
Next page
Mirasys VMS V9.5.1 release notes