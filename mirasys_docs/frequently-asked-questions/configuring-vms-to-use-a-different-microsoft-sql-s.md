# Configuring VMS to use an external Microsoft SQL Server | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/configuring-vms-to-use-a-different-microsoft-sql-s

Configuring VMS to use an external Microsoft SQL Server

Information regarding how to configure Mirasys VMS to use an external MS SQL Server installation than the default MS SQL Server Express.

Currently is possible to use different names for databases. Before making any modifications you need to stop VMS services; WDServer, SMServer and DVRServer.

If there are any temp files, remove those before starting services again. Because the system may detect that those files are modified and restore data from temp file, which overwrite SQL connection string changes.

Database configuration files location

You can find in these locations database configuration files, which need to be modified if using an external Microsoft SQL Server.

C:\Program Files\DVMS\SystemManagement\Database.xml

C:\Program Files\DVMS\DVR\dvr.xml

C:\Program Files\DVMS\DVR\DatabaseConfigurationFailover.xml

If this file is missing, you can create it manually.

C:\Program Files\DVMS\Export\DatabaseConfiguration.xml

C:\Program Files\DVMS\IncidentReporting\DatabaseConfiguration.xml

C:\Program Files\DVMS\StorageLocker\DatabaseConfiguration.xml

Connection string

Mirasys uses the connection string method to make a connection to Microsoft SQL Server. More information can be found here.

Example of connection string

XML
<ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=DvmsData;Integrated Security=True" />


In this example

Data Source=localhost\sqlexpress

Server address and instance name

Initial Catalog=DvmsData

Database name

Integrated Security=True

Use Windows authentication

Second example of connection string

XML
<ConnectionString value="Data Source=WIN-1234ASD,1433;Initial Catalog=DvmsData;User Id=LoginUsername;Password=UserPassword;Integrated Security=False" />


Data Source=WIN-1234ASD,1433

Server address and port for connection

When using SQL Server, there is no need to fill instance name

If needed, you can add the instance name ServerAddress\InstanceName

WIN-1234ASD\SQLEXPRESS,1433

Initial Catalog=DvmsData

Database name

User Id=LoginUsername

Log in username to make a login to SQL Server

Password=UserPassword

Password for username

Integrated Security=False

This means that the login method to SQL Server is used by SQL Server’s user management

Third example of connection string

<AnprConnectionString value="Data Source=WIN-1234ASD,1433;Initial Catalog=Anpr;User Id=LoginUsername;Password=UserPassword;Integrated Security=False" />


Data Source=WIN-1234ASD,1433

Server address and port for connection

When using SQL Server, there is no need to fill instance name

If needed, you can add the instance name ServerAddress\InstanceName

WIN-1234ASD\SQLEXPRESS,1433

Initial Catalog=Anpr

Database name

User Id=LoginUsername

Log in username to make a login to SQL Server

Password=UserPassword

Password for username

Integrated Security=False

This means that the login method to SQL Server is used by SQL Server’s user management

Configuration

Before making changes to database files, it is need to stop these services.

WDServer

DVRServer

SMServer

ADV Export Service

ADV Incident Reporting Service

ADV Storage Locker Service

Database.xml

C:\Program Files\DVMS\SystemManagement\

Open the Database.xml file example using Notepad.

Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “DvmsData”, “WdContext”, “DvmReportContext“, and “Failover” values with your database names.

Please note that “DvmsData“ is mentioned two times in this configuration.

In “DvmsDatabaseName value” and “ConnectionString value”.

If you need to change data retention times, please check this guide.

The DvmReportContext database is created when the end user uses the Spotter Audit Plugin.

Save the Database.xml file.

dvr.xml

Browse to C:\Program Files\DVMS\DVR\

Open the dvr.xml file example using Notepad.

Fill this information end of the file before </dina>.

XML
<!-- Read database configuration from dvr.xml file. The format for settings in dvr.xml is -->
<Metadata>
     <Database>
     <DatabaseName value="RecorderDB" />
     <Enabled value="True" />
     <ParameterMarker value="@" />
     <ProviderType value="System.Data.SqlClient" />
     <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=RecorderDB;Integrated Security=True" />
     <CreateDatabaseCommand value="CREATE DATABASE RecorderDB"/>
     <CreateTablesCommand value="USE RecorderDB CREATE TABLE RecorderMetadata (Id int NOT NULL IDENTITY(1,1) PRIMARY KEY, SourceType int NOT NULL, EventTime bigint NOT NULL, FormatType int NOT NULL, Channel int NOT NULL, MetaData nvarchar(MAX) NULL ) CREATE NONCLUSTERED INDEX IX_RecorderMetadata ON RecorderMetadata ([Channel] ASC, [SourceType] ASC, [FormatType] ASC, [EventTime] ASC)CREATE INDEX IX_EventTime ON RecorderMetadata (EventTime)" />
     <InsertCommand value="INSERT INTO RecorderMetadata(SourceType, EventTime, FormatType, Channel, Metadata) VALUES(@SourceType,@EventTime,@FormatType,@Channel,@Metadata)" />
     <DeleteRowsCommand value="DELETE FROM RecorderMetadata WHERE EventTime in (SELECT TOP {0} EventTime FROM RecorderMetadata ORDER BY EventTime ASC)" />
  </Database>   
</Metadata>


Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “RecorderDB” value with that database name.

Please note that this is mentioned two times in this configuration.

In “ConnectionString value” and “CreateTablesCommand value”.

Save the dvr.xml file.

dvr.xml with Anpr database

If you are using the EasyLPR feature in the VMS Server, this has its connection string name.

Browse to C:\Program Files\DVMS\DVR\

Open the dvr.xml file example using Notepad.

Fill this information end of the file before </dina>.

XML
<!-- Read database configuration from dvr.xml file. The format for settings in dvr.xml is -->
<Metadata>
      <AnprConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=Anpr;Integrated Security=True"  />
      <AnprMaxRows value="10000" />
  </Database>   
</Metadata>


Edit the “AnprConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “Anpr” value with that database name.

The Anpr database is created when the end user uses the Spotter EasyLPR Plugin.

Save the dvr.xml file.

dvr.xml with RecorderDB and Anpr databases

Browse to C:\Program Files\DVMS\DVR\

Open the dvr.xml file example using Notepad.

Fill this information end of the file before </dina>.

XML
<!-- Read database configuration from dvr.xml file. The format for settings in dvr.xml is -->
<Metadata>
     <Database>
     <DatabaseName value="RecorderDB" />
     <Enabled value="True" />
     <ParameterMarker value="@" />
     <ProviderType value="System.Data.SqlClient" />
     <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=RecorderDB;Integrated Security=True" />
     <CreateDatabaseCommand value="CREATE DATABASE RecorderDB"/>
     <CreateTablesCommand value="USE RecorderDB CREATE TABLE RecorderMetadata (Id int NOT NULL IDENTITY(1,1) PRIMARY KEY, SourceType int NOT NULL, EventTime bigint NOT NULL, FormatType int NOT NULL, Channel int NOT NULL, MetaData nvarchar(MAX) NULL ) CREATE NONCLUSTERED INDEX IX_RecorderMetadata ON RecorderMetadata ([Channel] ASC, [SourceType] ASC, [FormatType] ASC, [EventTime] ASC)CREATE INDEX IX_EventTime ON RecorderMetadata (EventTime)" />
     <InsertCommand value="INSERT INTO RecorderMetadata(SourceType, EventTime, FormatType, Channel, Metadata) VALUES(@SourceType,@EventTime,@FormatType,@Channel,@Metadata)" />
     <DeleteRowsCommand value="DELETE FROM RecorderMetadata WHERE EventTime in (SELECT TOP {0} EventTime FROM RecorderMetadata ORDER BY EventTime ASC)" />
     <AnprConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=Anpr;Integrated Security=True"  />
     <AnprMaxRows value="10000" />
  </Database>   
</Metadata>


Edit the “ConnectionString value” and “AnprConnectionString value” to match these SQL Server details, where you want to make the connection.

If you want to use your database name, replace the “RecorderDB” value with that database name.

Please note that this is mentioned two times in this configuration.

In “ConnectionString value” and “CreateTablesCommand value”.

If you want to use your database name, replace the “Anpr” value with that database name.

The Anpr database is created when the end user uses the Spotter EasyLPR Plugin.

Save the dvr.xml file.

DatabaseConfigurationFailover.xml

Browse to C:\Program Files\DVMS\DVR\

If the file is missing, you can create it manually.

Example of DatabaseConfigurationFailover.xml

XML
<?xml version="1.0" encoding="utf-8"?>
<configuration connectionString="Data Source=localhost\SQLEXPRESS;Initial Catalog=RecorderFailover;Integrated Security=True;MultipleActiveResultSets=True" providerName="System.Data.SqlClient" />


Open the DatabaseConfigurationFailover.xml file example using Notepad.

Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “RecorderFailover” value with that database name.

Save the DatabaseConfigurationFailover.xml file.

Export Service DatabaseConfiguration.xml

Browse to C:\Program Files\DVMS\Export

Open the DatabaseConfiguration.xml file example using Notepad.

Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “Export” value with that database name.

Save the DatabaseConfiguration.xml file.

Incident Reporting Service DatabaseConfiguration.xml

Browse to C:\Program Files\DVMS\IncidentReporting

Open the DatabaseConfiguration.xml file example using Notepad.

Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “IncidentReporting” value with that database name.

Save the DatabaseConfiguration.xml file.

Storage Locker Service DatabaseConfiguration.xml

Browse to C:\Program Files\DVMS\StorageLocker

Open the DatabaseConfiguration.xml file example using Notepad.

Edit the “ConnectionString value” to match these SQL Server details where you want to make the connection.

If you want to use your database name, replace the “StorageLocker” value with that database name.

Save the DatabaseConfiguration.xml file.

Changing the database name after configuration

If there is a need to change the database name after the first configuration, you only need to replace the database name with the new one.

After the database name change, the Mirasys VMS will not transfer data from the old database to the new one. This needs to be done manually.

Default database XML files
Database.xml
XML
<?xml version="1.0" encoding="utf-8"?>
<Database>
  <Enabled value="True" />
  <MaximumAlarmEventRows value="100000" />
  <MaximumAlarmEventDays value="2147483647" />
  <MaximumAuditTrailRows value="2147483647" />
  <MaximumAuditTrailDays value="2147483647" />
  <MaximumWatchdogEventRows value="100000" />
  <MaximumWatchdogEventDays value="2147483647" />
  <ProviderType value="System.Data.SqlClient" />
  <DvmsDatabaseName value="DvmsData" />
  <!-- <ConnectionString value="Data Source=10.99.100.153;Initial Catalog=DvmsData;User Id=sa;Password=test;Integrated Security=False" /> -->
  <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=DvmsData;Integrated Security=True" />
  <ParameterMarker value="@" />
  <Tables>
    <AlarmConfig value="AlarmConfig" />
    <AlarmAction value="AlarmAction" />
    <AlarmEvent value="AlarmEvent" />
    <AuditTrail value="AuditTrail" />
    <AlarmExport value="AlarmExport" />
  </Tables>
  <WdDatabase>
    <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=WdContext;Integrated Security=True" />
  </WdDatabase>
  <DvmReportDatabase>
    <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=DvmReportContext;Integrated Security=True" />
  </DvmReportDatabase>
  <FailoverDatabase>
    <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=Failover;Integrated Security=True" />
    <MaximumFailoverLogEntryRows value="5000" />
  </FailoverDatabase>
</Database>

dvr.xml
XML
<!-- Read database configuration from dvr.xml file. The format for settings in dvr.xml is -->
<Metadata>
     <Database>
     <DatabaseName value="RecorderDB" />
     <Enabled value="True" />
     <ParameterMarker value="@" />
     <ProviderType value="System.Data.SqlClient" />
     <ConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=RecorderDB;Integrated Security=True" />
     <CreateDatabaseCommand value="CREATE DATABASE RecorderDB"/>
     <CreateTablesCommand value="USE RecorderDB CREATE TABLE RecorderMetadata (Id int NOT NULL IDENTITY(1,1) PRIMARY KEY, SourceType int NOT NULL, EventTime bigint NOT NULL, FormatType int NOT NULL, Channel int NOT NULL, MetaData nvarchar(MAX) NULL ) CREATE NONCLUSTERED INDEX IX_RecorderMetadata ON RecorderMetadata ([Channel] ASC, [SourceType] ASC, [FormatType] ASC, [EventTime] ASC)CREATE INDEX IX_EventTime ON RecorderMetadata (EventTime)" />
     <InsertCommand value="INSERT INTO RecorderMetadata(SourceType, EventTime, FormatType, Channel, Metadata) VALUES(@SourceType,@EventTime,@FormatType,@Channel,@Metadata)" />
     <DeleteRowsCommand value="DELETE FROM RecorderMetadata WHERE EventTime in (SELECT TOP {0} EventTime FROM RecorderMetadata ORDER BY EventTime ASC)" />
     <AnprConnectionString value="Data Source=localhost\sqlexpress;Initial Catalog=Anpr;Integrated Security=True"  />
     <AnprMaxRows value="10000" />
  </Database>   
</Metadata>

DatabaseConfigurationFailover.xml
XML
<?xml version="1.0" encoding="utf-8"?>
<configuration connectionString="Data Source=localhost\SQLEXPRESS;Initial Catalog=RecorderFailover;Integrated Security=True;MultipleActiveResultSets=True" providerName="System.Data.SqlClient" />

Export Service DatabaseConfiguration.xml
XML
<?xml version="1.0" encoding="utf-8"?>
<configuration connectionString="Data Source=localhost\SQLEXPRESS;Initial Catalog=Export;Integrated Security=True;MultipleActiveResultSets=True" providerName="System.Data.SqlClient" />

Incident Reporting Service DatabaseConfiguration.xml
XML
<?xml version="1.0" encoding="utf-8"?>
<configuration connectionString="Data Source=localhost\SQLEXPRESS;Initial Catalog=IncidentReporting;Integrated Security=True;MultipleActiveResultSets=True" providerName="System.Data.SqlClient" />

Storage Locker Service DatabaseConfiguration.xml
XML
<?xml version="1.0" encoding="utf-8"?>
<configuration connectionString="Data Source=localhost\SQLEXPRESS;Initial Catalog=StorageLocker;Integrated Security=True;MultipleActiveResultSets=True" providerName="System.Data.SqlClient" />

Troubleshooting

If you are not sure if the connection is not working, you can use SQL Management Studio to test connection to Microsoft SQL Server.

Pagination
Previous page
ONVIF IP capture XML
Next page
How to change Alarm, Audit trail and Watchdog Event database retention times