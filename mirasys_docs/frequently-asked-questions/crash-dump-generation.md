# Crash Dump Generation | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/crash-dump-generation

Crash Dump Generation

In some rare cases, an application or service may crash unexpectedly. A crash dump file (also called a memory dump) is a file created by an operating system when an application or service crashes or encounters a serious error. It captures a snapshot of the system's memory (RAM) at the exact moment of the crash, which can be used for debugging and diagnosing the cause of the failure, and further on, help to fix the issue.

Locations of Crash Dumps

Mirasys VMS is configured to automatically create a crash dump file on unexpected application and service crashes.

Mirasys services

For the following Mirasys VMS services, the crash dump file is saved to the folder “C:\Windows\system32\config\systemprofile\AppData\Roaming\DVMS\LocalDumps\<service name>“:

System Services

ADVExportServer

ADVIncidentReporting

ADVStorageLocker

SMServer

VMS Server services

DVRServer

WDServer

Gateway service

DVMSGatewayService

Smart Services

AdvFrService

AdvLmService

AdvLprService

AdvOdsService

AdvOrService

Mirasys applications

For the following Mirasys VMS applications, the crash dump file is saved to the folder “C:\Users\<user name>\AppData\Roaming\DVMS\LocalDumps\<app name>“:

Spotter

SystemManager

SystemMonitor

MediaExporter

Pagination
Previous page
Fetch logs
Next page
How to use Mirasys VMS Text Channel