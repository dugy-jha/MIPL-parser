# How to add retry count information to Metadata | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-add-retry-count-information-to-metadata

How to add retry count information to Metadata
Step-by-step guide

First stop VMS services (WDServer, DVRServer, SMserver)

Then go to folder C:\Program Files\DVMS\DVR\MetadataAnalysis and open file MetadataAnalysisTCPDriver.xml

If Channel Name context not include RetryCount attribute you can add this

Example <Channel Name="MetadataTcpSendAll" RetryCount="5" Enabled="true" Address="127.0.0.1" Port="5151" ThreadQueueLimit="1000" SendFormat="UdpVca" Source="Default">

VMS version need to be V8.2.1 or higher

Default value is 5

When editing is done and the file is saved you can start again VMS services

Pagination
Previous page
How to change Alarm, Audit trail and Watchdog Event database retention times
Next page
Correct order to stop and start VMS Services