# How to change programs DEBUG level | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-change-programs-debug-level

How to change programs DEBUG level

In some cases to get more information out, there is need to change normal info level to debug level. This mode gather more data than normal info level and can help solve possible issues.

When level value is changed, this store new data to logs files.

Spotter

Go to user %appdata% folder and on there Spotter folder

Default location C:\Users\%appdata%\AppData\Roaming\DVMS\spotter\versionumber\managementip_5008

On that location find Spotter.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and start Spotter client

DVRServer

Go to DVMS installation folder and on there DVR-folder

Default location C:\Program Files\DVMS\DVR

On that location find DVRServer.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart DVRServer service

SMServer

Go to DVMS installation folder and on there SystemManagement-folder

Default location C:\Program Files\DVMS\SystemManagement

On that location find SMServer.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart SMServer service

WDServer

Go to DVMS installation folder and on there DVR-folder

Default location C:\Program Files\DVMS\DVR

On that location find WDServer.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart WDServer service

Incident Reporting

Go to DVMS installation folder and on there IncidentReporting-folder

Default location C:\Program Files\DVMS\IncidentReporting

On that location find ADVIncidentReporting.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart ADV Incident Reporting service

Storage Locker

Go to DVMS installation folder and on there StorageLocker-folder

Default location C:\Program Files\DVMS\StorageLocker

On that location find ADVStorageLocker.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart ADV Storage Locker service

Storage Locker

Go to DVMS installation folder and on there Export-folder

Default location C:\Program Files\DVMS\Export

On that location find ADVExportService.exe.config file

If you don’t have example Notepad++ installed on your server, then you can copy this file to Desktop and open it via Notepad

On this file find root section and under that line

<root>
<level value="INFO" />


Change this line value to DEBUG and save file

<level value="DEBUG" />


Now you can save file and restart ADV Export service

Pagination
Previous page
Media Exporter Command Line Tool
Next page
Automatic Backup feature