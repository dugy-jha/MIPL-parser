# Ohjelmistovahti eventit | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/watchdog-event-list-finnish-documentation

Ohjelmistovahti eventit
Use table header to sort columns

Id


	

Event


	

Description




0

	

SmServerDown

	

WDServer detected that  SMServer process stopped




1

	

SmServerUp

	

WDServer detected that  SMServer process started




2

	

DvrServerDown

	

WDServer detected that DVRService process stopped




3

	

DvrServerUp

	

WDServer detected that  DVRServer process started




4

	

NetworkDown

	

WDServer detected that network is down




5

	

NetworkUp

	

WDServer detected that network is up




6

	

DvrStatusOK

	

WDServer got ok status from recorder




7

	

DvrRefreshing

	

WDServer got settings refreshing status from recorder




8

	

DvrVideoCaptureLoadFailure

	

WDServer got video capture driver load error status from recorder




9

	

DvrAudioCaptureLoadFailure

	

WDServer got audio capture driver load error status from recorder




10

	

DvrDataCaptureLoadFailure

	

WDServer got text data driver load error status from recorder




11

	

DvrNoFileSystem

	

WDServer got no file system status from recorder




12

	

DvrDiskFailure

	

WDServer got disk failure status from recorder




13

	

VideoChannelOK

	

WDServer got video channel ok status from recorder




14

	

VideoChannelNoSignal

	

WDServer got video channel no signal status from recorder




15

	

VideoChannelNotStarted

	

WDServer got video channel not started status from recorder




16

	

VideoChannelNoCapture

	

WDServer got video channel no capture status from recorder




17

	

AudioChannelOK

	

WDServer got audio channel ok status from recorder




18

	

AudioChannelNoSignal

	

WDServer got audio channel not started status from recorder




19

	

AudioChannelNotStarted

	

WDServer got audio channel no capture status from recorder




20

	

AudioChannelNoCapture

	

WDServer got audio channel not started status from recorder




21

	

DataChannelOK

	

WDServer got text data channel ok status from recorder




22

	

DataChannelNoSignal

	

WDServer got text data channel not started status from recorder




23

	

DataChannelNotStarted

	

WDServer got text data channel no capture status from recorder




24

	

DataChannelNoCapture

	

WDServer got text data channel not started status from recorder




25

	

WDConnectionDown

	

Connection between WDServer and SMServer is down




26

	

WDConnectionUp

	

Connection between WDServer and SMServer is up




27

	

DvrSecurityFailure

	

WDServer got security failure status from recorder




28

	

DvrOtherInitFailure

	

WDServer got other initialization status from recorder




29

	

DvrArchiveFailed

	

WDServer got archive failed status from recorder




30

	

DvrMapNetworkDriveFailed

	

WDServer got map network drive failed status from recorder




31

	

DvrInsufficientDiskSpace

	

WDServer got insufficient disk space status from recorder




32

	

DvrNASDiskConnectionLostFailure

	

WDServer got NAS disk connection lost status from recorder




33

	

DvrNASDiskInitializationFailure

	

WDServer got NAS disk initialization failed status from recorder




34

	

SMServerDBConnectionLost

	

SMServer has detected that database connection lost




35

	

SMServerDBConnectionRestored

	

SMServer has detected that database connection is restored




36

	

SMServerAuditTrailCacheFull

	

SMServer has detected that audit trail cache is full




37

	

DvrTemperatureLpcOk

	

NOT IN USE




38

	

DvrTemperatureLpcWarning

	

NOT IN USE




39

	

DvrTemperatureLpcFailure

	

NOT IN USE




40

	

DvrTemperatureCpuOk

	

NOT IN USE




41

	

DvrTemperatureCpuWarning

	

NOT IN USE




42

	

DvrTemperatureCpuFailure

	

NOT IN USE




43

	

DvrTemperatureHddOk

	

WDServer has detected that HDD temperature is ok




44

	

DvrTemperatureHddWarning

	

WDServer has detected that HDD temperature is in warning level




45

	

DvrTemperatureHddFailure

	

WDServer has detected that HDD temperature is in failed level




46

	

DvrTemperatureDisplayAdapterOk

	

NOT IN USE




47

	

DvrTemperatureDisplayAdapterWarning

	

NOT IN USE




48

	

DvrTemperatureDisplayAdapterFailure

	

NOT IN USE




49

	

DvrTemperaturePsuOk

	

NOT IN USE




50

	

DvrTemperaturePsuWarning

	

NOT IN USE




51

	

DvrTemperaturePsuFailure

	

NOT IN USE




52

	

DvrTemperatureAcpiOk

	

NOT IN USE




53

	

DvrTemperatureAcpiWarning

	

NOT IN USE




54

	

DvrTemperatureAcpiFailure

	

NOT IN USE




55

	

DvrTemperatureRamOk

	

NOT IN USE




56

	

DvrTemperatureRamWarning

	

NOT IN USE




57

	

DvrTemperatureRamFailure

	

NOT IN USE




58

	

DvrMetadataDatabaseConnectionError

	

WDServer got metadata database connection error status from recorder




59

	

GatewayUp

	

WDServer has detected that Gateway service is started




60

	

GatewayDown

	

WDServer has detected that Gateway service is stopped




61

	

DvrFatalRuntimeError

	

WDServer got fatal runtime error status from recorder




62

	

SMSServerUp

	

WDServer has detected that SMSServer service is started




63

	

SMSServerDown

	

WDServer has detected that SMSServer service is stopped




64

	

LicenseIsAboutToExpire

	

SMServer has detected that license is about to expire




65

	

LicenseHasExpired

	

SMServer has detected that license is expired




66

	

AutomaticBackupFailed

	

Automatic backup generation has failed in SMServer




67

	

DvrBrokenAtMaintenance

	

Recorder failure has been detected on maintenance mode and failover is ignored




68

	

DvrBrokenAndChangedWithFailoverDvr

	

Recorder failover has occurred




69

	

DvrBrokenWithoutPossibilityToChangeWithFailoverDvr

	

Recorder failure has been detected but there is no free failover servers




70

	

RPMServerUp

	

NOT IN USE




71

	

RPMServerDown

	

NOT IN USE




72

	

PublicWebApiServerUp

	

NOT IN USE




73

	

PublicWebApiServerDown

	

NOT IN USE




74

	

ExportServerUp

	

WDServer has detected that Export service has started




75

	

ExportServerDown

	

WDServer has detected that Export service has shutdown




76

	

StorageLockerServerUp

	

WDServer has detected that Storage Locker service has started




77

	

StorageLockerServerDown

	

WDServer has detected that Storage Locker service has shutdown




78

	

IncidentReportingServerUp

	

WDServer has detected that Incident Reporting service has started




79

	

IncidentReportingServerDown

	

WDServer has detected that Incident Reporting service has shutdown




80

	

DvrFailbackDone

	

Recorder failback operation has been performed successfully on SMServer




81

	

DvrFailbackFailed

	

Recorder failback operation has failed on SMServer




82

	

DvrFailbackOnMaintenance

	

Recorder failback operation has been ignored because recorder is in maintenance mode

Pagination
Previous page
Ohjelmistovahtiloki
Next page
Ohjelmalisäkkeet