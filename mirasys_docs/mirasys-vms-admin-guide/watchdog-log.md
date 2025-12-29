# Watchdog log | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/watchdog-log

Watchdog log

By default, the system shows the watchdog logs from all servers.
However, you can select one or several servers from the list on the left.
You can sort the logs by clicking the column headings.
To update the list without closing the window, click the Refresh button.

Additional Watchdog Delivery Methods

The Watchdog functionality includes three new protocols: TCP, SMS (requires an external SMS module), and customizable e-mail form. 

Each new protocol has its driver:

C:\Program Files\DVMS\DVR\WDEventProviders\

WDEventProviderSMS.xml

WDEventProviderSMTP.xml

WDEventProviderTCP.xml

At this moment, these files need to be edited manually. Each XML file contains the documentation regarding the configuration options.
The new configuration options include filtered and conditional warnings (i.e. “send warning X only once in every 60 minutes” or “send warning X only if condition Y is not met in two minutes”), and customizable warning message format.
After the files have been edited, Watchdog needs to be restarted for the changes to take effect. 

Note: This feature is recommended only for advanced users. XML files are highly vulnerable to spelling errors and mistyped strings and keys.
Even a tiny error can cause fatal errors. Mirasys takes no responsibility for XML errors caused by editing the files.

Pagination
Previous page
Watchdog settings
Next page
Watchdog event list