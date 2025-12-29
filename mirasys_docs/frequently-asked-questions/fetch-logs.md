# Fetch logs | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/fetch-logs

Fetch logs

Usually, logs are easiest to fetch from System Managers "Export logs"-section (DVR, SM, WD but not Gateway). In some cases this is not possible, so logs must be fetched manually. If the system is not easily accessed one should always fetch all logs described in this article.

Step-by-step guide (DVR and WD logs)

Go to C:\Program Files\DVMS\DVR\logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (SM logs)

Go to C:\Program Files\DVMS\SystemManagement\logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (Gateway logs)

Go to C:\Program Files\DVMS\Gateway\logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (Spotter Web logs)

Go to C:\Users\Public\logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (Application logs, Spotter and System Manager etc.)

Go to C:\Users\%username%\AppData\Roaming\DVMS\DVR Application\Logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (Spotter Player)

Go to C:\Users\%username%\AppData\Local\DVMS Client\Sandbox\Spotter Player\VMSVersionNumber\roaming\modified\@APPDATA@\DVMS\DVR Application\Logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Step-by-step guide (Windows logs)

Open Start-menu

Search "Event Viewer"

On the left side of the Event Viewer choose Windows logs

Right-click System logs

Save all events as

Choose a path, name the file and save in .evtx-format

Repeat steps 4-6 with Application logs

Add logs to a new folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

VCA Core logs

Go to location C:\Windows\System32\config\systemprofile\AppData\Local\vca-cored\logs

Copy whole "Logs" folder

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Installer logs

Go to location C:\Users\%usrname%\AppData\Local\Temp

%temp%

Make zip file from DVMS logs files

Right-click the folder → Send to → Compressed (zipped) folder

Attach logs to ticket

Pagination
Previous page
How to fix error in V7 "No disks configured recorder "Local recorder""
Next page
Crash Dump Generation