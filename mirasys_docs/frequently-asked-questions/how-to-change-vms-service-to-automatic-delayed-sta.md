# How to change VMS Service to Automatic (Delayed Start) | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-change-vms-service-to-automatic-delayed-sta

How to change VMS Service to Automatic (Delayed Start)

In some cases, you may need to change VMS Services to start delayed.

This can be done in Windows Services.

First open Windows Services and search there wanted VMS Services (WDServer, SMServer, DVRServer or DVMSGatewayService).

Double click wanted VMS Service.

This opens a new window where you can see the service Startup type.

Change that to Automatic (Delayed Start) and click OK.




Now service is starting delayed. This means that the first Windows normal services starts and after that Mirasys VMS service.

Repeat these steps all wanted VMS Services.

Pagination
Previous page
How to install CA certificate to Windows 10 store
Next page
Lost Microsoft SQL Express password/user