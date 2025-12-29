# How to change Alarm, Audit trail and Watchdog Event database retention times | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-change-alarm-audit-trail-and-watchdog-event

How to change Alarm, Audit trail and Watchdog Event database retention times

Stop WDserver, SMserver and DVRserver

Then go to folder C:\Program Files\DVMS\SystemManagement (default location)

Locate Database.xml file

Copy this file to your desktop and open it example in Notepad

Then edit these lines and put wanted days on here

<MaximumAlarmEventRows value="2147483647 />
<MaximumAlarmEventDays value="2147483647" />
<MaximumAuditTrailRows value="2147483647" />
<MaximumAuditTrailDays value="2147483647" />
<MaximumWatchdogEventRows value="2147483647" />
<MaximumWatchdogEventDays value="2147483647" />


2147483647 means unlimited days
There is no need to make changes to rows

After these save this file again and copy it back to C:\Program Files\DVMS\SystemManagement (default location)

Then delete file Database.xml.tmp, if you don’t delete it system fill use default variables

Then start VMS services again

System create tmp file again for Database.xml file

Useful information

If the database is full, then 10 000 oldest rows are deleted (alarm rows or audit trail rows, depending on which ones are older)

Maximum rows limits are checked every time when new data is added to the database

Maximum days limits are checked periodically: the first check is done 1 minute after SmServer start, and then every 30 minutes

If the maximum days limit is exceeded, then rows older than the maximum days are deleted

However, not more than 10 000 rows are deleted at a time

Pagination
Previous page
Configuring VMS to use an external Microsoft SQL Server
Next page
How to add retry count information to Metadata