# Watchdog Event Provider via TCP (WDEventProviderTCP.xml) | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/watchdog-event-provider-via-tcp-wdeventprovidertcp

Watchdog Event Provider via TCP (WDEventProviderTCP.xml)

With this please do not use System Manager own Watchdog alarm sending.

This feature can be used example to delay Camera No Signal events when camera is coming online shortly after this event.

Requirements

License feature TCP Watchdog health provider

On default latest VMS V9 and V8 VMS licenses includes this feature

How to modify WDEventProviderTCP.xml file

Go to folder default location C:\Program Files\DVMS\DVR\WDEventProviders

Make copy of WDEventProviderTCP.xml file to example Desktop

Open this file using example Notepad++

To enable this feature, you need to change line

<Enabled value="false" />


To

<Enabled value="true" />


This Watchdog Event Provider support IPv4 or hostname where messages will be sent.

To change these values you can find them on this xml file.

XML
  <!-- How many messages can be in sending queue before they will be lost -->
  <ThreadQueueLimit value="1000" />

  <!-- IPv4 address or hostname where messages will be sent -->
  <Address value="localhost" />

  <!-- TCP port number where messages will be sent -->
  <Port value="5151" />


If there is need to send data to other IPv4 address or hostname, there is option to uncomment that section and fill there wanted details.

XML
  <!-- Secondary address will be used if main address will fail -->

  <!-- Optional seconary IPv4 address or hostname where messages will be sent -->
  <!--<SecondaryAddress value="localhost" />-->

  <!-- Optional seconary TCP port number where messages will be sent -->
  <!--<SecondaryPort value="5152" />-->


On default events are resend 3 times but on xml file there is option to increase or decrease this resend count.

XML
  <!-- Events will be resend number of counts specified with this value -->
  <ResendCount value="3" />


DelaySendEvents section is section where you can make changes to delay Camera No Signal event sending.

This is helpful if there is IP camera which is working but not behind stable connection.

Default DelaySendEvents

<!-- text --> means comment in XML file

  <DelaySendEvents>
    <!-- Wait 60 seconds for video channel 2 for VideoChannelOK event after VideoChannelNotStarted has received 
    <DelaySendEvent seconds="60" channel="2" triggerEvent="15" cancelEvent="13" />
    -->
    <!-- Wait 30 seconds for video channel 2 for VideoChannelOK event after VideoChannelNoSignal has received 
    <DelaySendEvent seconds="30" channel="2" triggerEvent="14" cancelEvent="13" />
    -->
  </DelaySendEvents>


To change this section you need to add new lines under comments example

<DelaySendEvents>
    <!-- Wait 60 seconds for video channel 2 for VideoChannelOK event after VideoChannelNotStarted has received 
    <DelaySendEvent seconds="60" channel="2" triggerEvent="15" cancelEvent="13" />
    -->
    <!-- Wait 30 seconds for video channel 2 for VideoChannelOK event after VideoChannelNoSignal has received 
    <DelaySendEvent seconds="30" channel="2" triggerEvent="14" cancelEvent="13" />
    -->
    
    <DelaySendEvent seconds="60" channel="1" triggerEvent="15" cancelEvent="13" />
    <DelaySendEvent seconds="30" channel="1" triggerEvent="14" cancelEvent="13" />
  </DelaySendEvents>


Now there is add two lines

<DelaySendEvent seconds="60" channel="1" triggerEvent="15" cancelEvent="13" />
<DelaySendEvent seconds="30" channel="1" triggerEvent="14" cancelEvent="13" />


First line mean that we have delayed event “VideoChannelNotStarted” at 60 seconds and if system get in 60 seconds event “VideoChannelOK”, system not send email out but if that is more than 60s, then email is sent out.

Second line ean that we have delayed event “VideoChannelNoSignal” at 30 seconds and if system get in 30 seconds event “VideoChannelOK”, system not send email out but if that is more than 30s, then email is sent out.

Now save this WDEventProviderTCP.xml file and copy this to default location C:\Program Files\DVMS\DVR\WDEventProviders

When this is done, restart WDServer service in Windows Services.

Now when there is happening event where is made made changes, system send or not send email out based on these settings in XML file.

Filtering events

XML also provide option to filter events in Filters section.

  <Filters>
    <!-- if minutes is 0, event won't be sent at all -->
    <!-- sample filter: never send event 28
    <Filter event="28" minutes="0" /> -->
    <!-- sample filter: send event 4 once/hour maximum
    <Filter event="4" minutes="60" /> -->
  </Filters>


In this section you can example disable wanted event sending or send event once in hour.

Changing time format

In XML has two lines where you can change time format.

  <!-- The format used in UTC timestamp. See format description in http://msdn.microsoft.com/en-us/library/az4se3k1.aspx -->
  <UtcTimeFormat value="yyyy-MM-dd hh-mm-ss-fff" />

  <!-- The format used in local timestamp. See format description in http://msdn.microsoft.com/en-us/library/az4se3k1.aspx -->
  <LocalTimeFormat value="yyyy-MM-dd hh-mm-ss-fff zzz" />


Software use standard date and time format strings from Microsoft code.

Here links to supported strings.

https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings

https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings

Example you want to change Local time format to 27.7.2023 and time 16.39 you need edit line

<LocalTimeFormat value="yyyy-MM-dd hh-mm-ss-fff zzz" />


Change this line to this

<LocalTimeFormat value="dd-MM-yyyy HH-mm-ss-fff zzz" />

Changing Message format

If there is need to change message format, this can be found on XML file.

XML
  <!-- Message format used when sending messages. At least one macro shall be used, or any number or order of them. -->
  <MessageFormat value="$(MessageLength) $(RecorderMAC) $(EventNumber) $(EventName) $(ChannelNumber) $(ActionNumber) $(ActionName) $(UtcTime) $(LocalTime) $(Info)$(Cr)" />
  <!-- Message format macros: -->
  <!-- $(MessageLength) type = Uint32, not including MessageLength value -->
  <!-- $(EventNumber) type = Int32 -->
  <!-- $(EventName) type = string -->
  <!-- $(ChannelNumber) type = Int32, 0 = not channel specific event, 1-max channels -->
  <!-- $(ActionNumber) type = Int32 -->
  <!-- $(ActionName) type = string -->
  <!-- $(Info) type = string -->
  <!-- $(RecorderMAC) type = string -->
  <!-- $(UtcTime) type = UtcTimeFormat (see above) -->
  <!-- $(LocalTime) type = LocalTimeFormat (see above) -->
  <!-- $(Tab) -->
  <!-- $(Cr) -->


Then save these changes to WDEventProviderTCP.xml file and restart WDServer in Windows Services.

Supported WD Events

End of WDEventProviderTCP.xml file has all current supported WD Events codes.

  <!-- Current WD events
  // Service states
  SmServerDown = 0
  SmServerUp = 1
  DvrServerDown = 2
  DvrServerUp = 3

  // Network status
  NetworkDown = 4
  NetworkUp = 5

  // DVR core state
  DvrStatusOK = 6
  DvrRefreshing = 7
  DvrVideoCaptureLoadFailure = 8
  DvrAudioCaptureLoadFailure = 9
  DvrDataCaptureLoadFailure = 10
  DvrNoFileSystem = 11
  DvrDiskFailure = 12

  // Video channel status
  VideoChannelOK = 13
  VideoChannelNoSignal = 14
  VideoChannelNotStarted = 15
  VideoChannelNoCapture = 16

  // Audio channel status
  AudioChannelOK = 17
  AudioChannelNoSignal = 18
  AudioChannelNotStarted = 19
  AudioChannelNoCapture = 20

  // Data channel status
  DataChannelOK = 21
  DataChannelNoSignal = 22
  DataChannelNotStarted = 23
  DataChannelNoCapture = 24

  // Watchdog connection
  WDConnectionDown = 25
  WDConnectionUp = 26

  // Additional dvr core states
  DvrSecurityFailure = 27
  DvrOtherInitFailure = 28

  // Archiving failures
  DvrArchiveFailed = 29
  DvrMapNetworkDriveFailed = 30

  // Insuficient disk space
  DvrInsufficientDiskSpace = 31

  // NAS failures
  DvrNASDiskConnectionLostFailure = 32
  DvrNASDiskInitializationFailure = 33

  // Database events
  SMServerDBConnectionLost = 34
  SMServerDBConnectionRestored = 35
  SMServerAuditTrailCacheFull = 36

  // Temperature events
  DvrTemperatureLpcOk = 37
  DvrTemperatureLpcWarning = 38
  DvrTemperatureLpcFailure = 39
  DvrTemperatureCpuOk = 40
  DvrTemperatureCpuWarning = 41
  DvrTemperatureCpuFailure = 42
  DvrTemperatureHddOk = 43
  DvrTemperatureHddWarning = 44
  DvrTemperatureHddFailure = 45
  DvrTemperatureDisplayAdapterOk = 46
  DvrTemperatureDisplayAdapterWarning = 47
  DvrTemperatureDisplayAdapterFailure = 48
  DvrTemperaturePsuOk = 49
  DvrTemperaturePsuWarning = 50
  DvrTemperaturePsuFailure = 51
  DvrTemperatureAcpiOk = 52
  DvrTemperatureAcpiWarning = 53
  DvrTemperatureAcpiFailure = 54
  DvrTemperatureRamOk = 55
  DvrTemperatureRamWarning = 56
  DvrTemperatureRamFailure = 57

  DvrMetadataDatabaseConnectionError = 58

  GatewayUp = 59
  GatewayDown = 60

  DvrFatalRuntimeError = 61

  SMSServerUp = 62
  SMSServerDown = 63
  
  LicenseIsAboutToExpire = 64
  LicenseHasExpired = 65
  
  AutomaticBackupFailed = 66
  -->

Pagination
Previous page
Watchdog Event Provider via STMP (WDEventProviderSMTP.xml)
Next page
How to use HTTP IO with Axis IP Speaker