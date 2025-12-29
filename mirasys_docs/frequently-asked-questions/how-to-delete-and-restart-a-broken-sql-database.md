# How to delete and restart a broken SQL database | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-delete-and-restart-a-broken-sql-database

How to delete and restart a broken SQL database

Sometimes there might be problems with the SMServer and the SQL database may be broken. This solution repairs the SQL databases.

These are the databases: DVRServer, WDServer, SMServer 

Step-by-step guide

Go to the Master Server

Shut down all VMS processes: WDServer, DVRServer, SMServer

Open the SQL Management Studio. Use of administrator rights may be needed

Go to "Databases"

Right-click each database "DvmsData", "RecorderDB" and "WdContext" and delete the databases.

Restart VMS services:WDServer, DVRServer, SMServer

In the SQL Management studio, close the folder hierarchy to the root level and press refresh. Check that the "DvmsData", "RecorderDB" and "WdContext" databases are created.

Test if the system works better

Optional steps: If there are problems with access rights try this:

3.1 Go to Security - logins - NT AUTHORITY\SYSTEM
3.2 Click "Server roles"
3.3 Select "sysadmin"
3.4 Press OK

Pagination
Previous page
Screen flickering on Nvidia GPU
Next page
Create memory dump using Windows Task Manager