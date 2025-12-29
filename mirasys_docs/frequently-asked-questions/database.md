# VMS Databases | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/database

VMS Databases

Mirasys VMS uses a Microsoft SQL Express server to store data.

DvmReportContext

This database is created when a user uses the Spotter Camera Audit plugin.

This database includes these tables

__MigrationHistory

DvmAuditHistories

DvmAudits

DvmReportHistories

DvmReports

DvmsData

This database includes these tables

AlarmAction

Contains alarm action information

AlarmConfig

Contains alarm configurations

AlarmEvent

Contains alarm events (= triggered alarms)

AlarmExport

Contains details of alarm export

AuditTrail

Contains audit trail information

Export

This database includes these tables

__MigrationHistory

ExportParameters

ExportTasks

Failover

This database includes these tables

__MigrationHistory

FailoverLogEntryDbs

IncidentReporting

This database includes these tables

__MigrationHistory

DailyReports

Evidences

Histories

IncidentReports

Numberings

Organizations

Positions

ReportInfoes

Reports

Reports

RecorderDB

This database includes these tables

Edge

Contains edge storage intervals

MetadataEvents

Contains metadata events, has a reference to RecorderMetadata

OriginalMetadata

Contains original metadata, has a reference to RecorderMetadata.​

RecorderMetadata

Contains information about metadata (channel, time, Mirasys metadata, etc.)

RecorderFailover

This database includes these tables

__MigrationHistory

AlarmDatas

Channels

CopyTasks

FailoverInfoes

StorageLocker

This database includes these tables

FailoverInfoes

FileMetadatas

Histories

Identities

Settings

WdContext

This database includes these tables

__MigrationHistory

WdEvents

Contains WatchDog data

Other information

When the VMS system includes a Management server, this server gathers these details from the servers to its databases.

DvmsData

AlarmAction

AlarmConfig

AlarmEvent

AuditTrail

WdContext

WdEvents

Pagination
Previous page
How to reset usernames and password to default
Next page
How to configure Hikvision DS-6716HUHI-K