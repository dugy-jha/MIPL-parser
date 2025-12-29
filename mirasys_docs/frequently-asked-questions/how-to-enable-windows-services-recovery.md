# How to enable Windows Services recovery | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-enable-windows-services-recovery

How to enable Windows Services recovery

If you have encounter problem that Windows Service has crashed but not started again. Then you should look is that service recovery options enabled or not configured.

This is very good way to keep service running if there is not possible to monitor these. If service keep crashing, then it's clear indicator that something is wrong and it's better to look logs to resolve problem.

You may need to use this with Proxies when VMS is 8.3.x or older.

Step-by-step guide

Go to Windows Serviceshttps://www.digitalcitizen.life/ways-access-services-windows

On there open you wanted service and go to Recovery tab

On this tab you can select what happens when service crash and what is action after that

First Failure: Restart the Service
Second Failure: Restart the Service
Subsequent failures: Take No Action
Reset fail count after: 0 days
Restart service after: 15 minutes


There is also option to restart computer if this is needed.

Pagination
Previous page
How to fix error "Cannot get logical disk information"
Next page
Screen flickering on Nvidia GPU