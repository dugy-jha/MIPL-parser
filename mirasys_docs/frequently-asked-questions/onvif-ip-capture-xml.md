# ONVIF IP capture XML | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/onvif-ip-capture-xml

ONVIF IP capture XML
XML configuration for ONVIF IP Capture drive

The driver version 1.3.5.0 supports extended XML configuration to make the driver behavior more flexible and support more ONVIF-compliant devices.

The configuration file is in the installation package, and DVMS is set by default.

After installation, the file should be located in the %ProgramFiles%/DVMS/DVR folder.

File structure

The XML configuration file contains the following sections:

Default section.
This section contains the configuration which will be used for all driver instances.

Device sections.
These sections allow customizing driver configuration for each device.

Each specified section contains the following categories:

Capability detection option group. This group contains options that affect the device capabilities detection. So, they should be modified before adding an ONVIF-compliant device to the Mirasys VMS.

Dynamic option group. This group of options may be used without device re-subscribing. The specified options may be changed "on the fly" after applying settings.

A detailed description of all specified groups and sections can be found below.
Also, the file contains a global option for switching streaming mode between unicast and multicast, as for most other drivers with multicast support.

Streaming mode

The StreamingMode option affects all driver instances and all subscribed ONVIF-compliant devices as a result. The example of file content with this option is below:

XML
<?XML version="1.0" encoding="utf-8"?>
<Configuration>
  <!-- Switch streaming mode for all ONVIF-compliant IP device subscribed by ONVIF IP Capture driver -->
  <!-- Note: This option affects to all IP devices who answered that "RTP Multicast" capability is supported. The devices without this option support will work in Unicast mode only -->
  <!-- Possible values: Unicast, Multicast:Primary, Multicast:Listener -->
  <StreamingMode>Unicast</StreamingMode>
</Configuration>





The default mode is Unicast, and all added IP devices should support it.
The option will not affect the devices which do not support RTP Multicast capability. Such devices will always work in unicast mode.

Please note that the driver reads the StreamingMode option on the startup of each stream. So, to take the option, it will be required to restart all video and audio streams.
The easiest way to use the new option value is to restart the recorder service.

Also, the streams may be restarted by applying settings via the System manager. However, please keep in mind that:

The recorder does not update video settings if they are not changed. So, it is required to change at least one option (for example, quality) to restart the video stream

The recorder does not restart the audio stream while changing video settings. As a result, the audio will keep going in unicast if the user updates the XML file and then changes the resolution or quality setting via System Manager. Only changing the video codec guarantees the restart of all streams because the driver instance will be re-opened.

Please also refer to the Multicast section to specify the multicast address and port settings if problems with the multicast stream start.

Default section

This section contains the ONVIF driver configuration, which will be used for all ONVIF devices by default.
Please find the default configuration for this section below:

XML
<?xml version="1.0" encoding="utf-8"?>
<Configuration>

<!-- Default configuration for all subscribed IP devices -->

  <Default>

    <!-- This section contains options which affect to the device capabilities. The device should be re-added to DVMS to take changed options into use -->

    <CapabilityDetection>

      <!-- Detect device as multi-channel if feature is supported -->

      <!-- Note: Disable this option in case if single channel device is detected as multiple channel because of incorrect ONVIF reply -->

      <!-- Default value: "Yes" -->

      <DetectAsMultiChannel>Yes</DetectAsMultiChannel>

 

      <!-- Allow to detect device as multiple streaming if such feature is supported -->

      <!-- Note: Disable this option in case if device is not fully support multiple streaming feature and you'd like to have one stream only -->

      <!-- Default value: "Yes" -->

      <AllowMultipleStreaming>Yes</AllowMultipleStreaming>

 

      <!-- Version of ONVIF PTZ service -->

      <!-- Note: Set version to "1.0" value in case if driver is not able to detect PTZ capabilities of ONVIF v1.01/1.02 compliant device correctly -->

      <!-- Default value: "2.0" -->

      <PtzServiceVersion>2.0</PtzServiceVersion>

 

      <!-- Allow to use GetCompatibleVideoEncoderConfigurations request during video capabilities detection -->

      <!-- Note: Please disable this option in case if GetCompatibleVideoEncoderConfigurations request is not supported by the IP device or it returns video encoders which are not compatible with current profile -->

      <!-- Default value: "Yes" -->

      <AllowGetCompatibleVideoEncoderConfigurations>Yes</AllowGetCompatibleVideoEncoderConfigurations>

 

      <!-- Timeout of HTTP connection (in milliseconds) -->

      <!-- Note: The driver will treat ONVIF request as failed in case if camera replies longer that specified value. Please increase this value in case of timeout errors -->

      <!-- Possible values: 5000 - 60000 (i.e. 5 - 60 seconds) -->

      <!-- Default value: 7500 (i.e. 7.5 seconds) -->

      <HTTPConnectionTimeout>7500</HTTPConnectionTimeout>

 

      <!-- Ignore WSPullPointSupport flag during detection of digital I/O capabilities -->

      <!-- Note: The WSPullPointSupport may be set to "false" even if device is really supports pull-point subscriptions. Please enable this option in this case to add the device with Digital I/O support -->

      <!-- Default value: "No" (Use for debugging only!) -->

      <IgnoreWSPullPointSupport>No</IgnoreWSPullPointSupport>

 

      <!-- This option allows to limit Digital I/O contacts during capabilities detection -->

      <!-- Note: In some cases, it is required to debug the camera without using Pull-Point event subscriptions. Unfortunately, DVMS doesn't allow to exclude I/O from the configuration, so the easiest way does not add them to capabilities during device capabilities detection -->

      <!-- Possible values: "All" - add both digital inputs and outputs to capabilities (in case if they are available on the device); "Inputs only" - do not add digital outputs to the capabilities; "Outputs only" - do not add digital inputs to the capabilities; "None" - the Digital I/O will not be available for this device at all -->

      <!-- Default value: "All" (Use for debugging only!) -->

      <DigitalIOSupport>All</DigitalIOSupport>

    </CapabilityDetection>

 

    <!-- This section contains options which are used during normal driver usage. The camera settings should be re-saved in DVMS to take these options into use -->

    <DynamicOptions>

      <!-- Required size of RTP packets -->

      <!-- Note: Several cameras allow to specify size of RTP packet via Blocksize option in RTSP SETUP request -->

      <!-- Note: Please note that real size of packet may be greater than specified value because it also includes headers of TCP, IP and Ethernet II protocol layers -->

      <!-- Possible values: The packet size should be a positive decimal number measured in octets, greater than 100. Empty value means default size (1400 MTU) -->

      <RTPPacketSize></RTPPacketSize>

 

      <!-- address of network adapter through which the devices are connected to DVMS recorder. -->

      <!-- Important: The local address option is required if the server has more than one network interface available because the driver cannot automatically detect the correct interface. This option may be left empty in case of a single network interface available -->

      <!-- Possible values: Any IPv4 address. An empty value means default interface -->

      <NetworkInterface></NetworkInterface>

 

      <!-- Allow to use tptz::SetConfiguration request before PTZ functionality usage -->

      <!-- Note: Please disable this option in case if tptz::SetConfiguration request works incorrectly or not fully supported by the ONVIF-compliant device -->

      <!-- Default value: "Yes" -->

      <AllowPTZConfigurationUpdate>Yes</AllowPTZConfigurationUpdate>

 

      <!-- Disable checking and updating of non-important options like frame-rate of quality -->

      <!-- Note: The IP device may not allow to change such minor options or use limited range of values (for example: 1,3,5 instead of 1..5 range). The driver will not apply these options in case if encoding and resolution settings were not changed -->

      <!-- Default value: "No" (Use for debugging only!) -->

      <IgnoreFramerateDiscrepancy>No</IgnoreFramerateDiscrepancy>

 

      <!-- Check video encoder and video source configurations associated with media profile -->

      <!-- Note: This driver will use only video encoder associated with profile even if it differs from configuration media profile has during capabilities detection. Multiple streaming functionality may not work correctly if this option is disabled -->

      <!-- Default value: "Yes" -->

      <VerifyMediaProfile>Yes</VerifyMediaProfile>

 

      <!-- Bitrate range for quality configuring -->

      <!-- Note: The bitrate limitation will be used in case if camera will not return supported bitrate range. BitrateLimit value will not be changed in case if this section is not presented -->

      <!-- Values in Kbps units. No default values for this section -->

      <BitrateRange>

        <Min>64</Min>

        <Max>12000</Max>

      </BitrateRange>

 

      <!-- Size of GOV in frames (including intra) -->

      <!-- Note: The GOV length adjustment may be needed to set required value instead of standard 1 I-frame per second applied by the driver -->

      <!-- Possible values: "Auto" - use standard driver algorithm, "Off" - do not change value applied via Web-interface, non-zero numeric value - exact size of the GOV (maximal available value will be applied if specified value is out of range supported by the camera) -->

      <!-- Default value: "Auto" -->

      <GovLength>Auto</GovLength>

 

      <!-- Video streaming protocol -->

      <!-- Possible values: "RTP over UDP" - streaming via UDP protocol, ports in range 3556-4556 should be opened in Firewall; "RTP over RTSP" - streaming over RTSP port (554) -->

      <!-- Note: The "RTP over RTSP" mode may be enabled only for Unicast stream and in case if device supports it. Otherwise "RTP over UDP" will be used -->

      <!-- Default value: "RTP over UDP" -->

      <StreamingProtocol>RTP over RTSP</StreamingProtocol>

 

      <!-- Perform additional logging for RTSP session -->

      <!-- Note: In some cases it is required to log RTSP session state or time when it was started or stopped for analyze of RTSP problems -->

      <!-- Default value: "No" (Use for debugging only!) -->

      <RtspSessionLogging>Yes</RtspSessionLogging>

    </DynamicOptions>

 

</Configuration>


The default value (hard-coded in the driver) will be used if any option is missed from the configuration.
Please note that part of the options is used for debugging the driver only. They are not included in XML configuration by default and will not be available for end-users.

The Default section of the configuration contains Capability detection and Dynamic option groups.
Please find the group description below.

Capability detection options

The capability detection section contains options that affect the detection of device capabilities.
It is required to remove the camera from DVMS and add it again after the options change if you want to take any of the options for the specified camera.
The following options are available in this section:

DetectAsMultiChannel - allows detecting devices as multiple channels if this feature is supported.
This option should be "No" if the device has one video input but is detected as a multiple-channel device. 

Please refer to the Issue with Detection Onvif-compliant Device as a multiple-channel device section of the QA Notes page to learn more about this option.

AllowMultipleStreaming - allow detecting device as multiple streaming if such feature is supported.
This option should be set to "No" if the device does not fully support multiple streaming features. Also, the user may want to use one stream with different encodings/resolutions instead of several streams with limited capabilities.
Please refer to the Multiple Streaming implementation sections of the QA Notes page to learn more about this option.

PtzServiceVersion - specifies the version of ONVIF PTZ service (default value is "2.0")
Most ONVIF-compliant IP cameras return all available namespaces for all available services in each reply so that the driver can read the required version from such a reply.
However, a few cameras provide only namespaces used in returned replies. The driver will not read PTZ capabilities if these cameras support the 1.0 version of PTZ service (ONVIF Specifications v1.01), so this option should be set to a "1.0" value.

AllowGetCompatibleVideoEncoderConfigurations - allows the use of GetCompatibleVideoEncoderConfigurations request during video capabilities detection.
An ONVIF-compliant IP camera may return the whole list of video encoders as compatible so that the driver may select an encoder configuration unsupported for the selected profile or profile is fixed and cannot use anything except the currently applied configuration. In this case, we'll get a "No signal" problem after adding the camera. Would you please disable this option to add such an IP device correctly?

HTTPConnectionTimeout - timeout of HTTP connection (in milliseconds).
The driver uses a 7.5-second timeout for ONVIF requests. However, some ONVIF-compliant devices may process ONVIF requests (mainly apply/update requests) for a long time. As a result, the driver will not be able to detect the camera or cannot apply any configuration correctly.
Please increase the network timeout to resolve this issue. The possible range for this option is 5..60 seconds.

IgnoreWSPullPointSupport - ignore the WSPullPointSupport flag during detection of digital I/O capabilities.
Sometimes, an ONVIF-compliant device supports WS-PullPoint notifications, but the specified capability is set as unsupported. This option allows us to skip this check, but we cannot guarantee that WS-PullPoint is supported. So, please enable this option for debugging only.

DigitalIOSupport - this option allows excluding digital inputs, digital outputs or both of them.
This option was added because of several reasons:

First of all, several devices may support WS-PullPoint incorrectly, so digital inputs will always be in an "Unknown" state and will be useless

A couple of camera samples worked with PullMessage incorrectly and returned the response immediately (i.e. timeout option was skipped). This behavior overloads the camera's HTTP service, and the camera may become inaccessible

Also, it may be required to turn the inputs off for debug purposes (like reducing amount requests to the camera or preparing Wireshark to log without unnecessary requests)

This option should be used for debugging only and should not be provided in the customer package by default.

Dynamic options

The Dynamic Options section contains options that can be changed dynamically (on-fly) without re-subscribing the IP device or changing its capabilities.
This section is loaded during video channel or PTZ communication module creation, so it usually will be enough to save DVMS settings to take changed options into use.
The following options are available in this section:

AllowPTZConfigurationUpdate - allows the use of tptz::SetConfiguration request before PTZ functionality usage
The driver verifies that the correct PTZ configuration is selected before sending any PTZ command to the camera.
Sometimes, the ONVIF-compliant devices do not allow the change of any minor option that is unimportant for this functionality, so the driver should process it correctly.
However, in some cases, the tptz::SetConfiguration request does not work correctly. In this case, the option should be disabled, but the end-user should guarantee that the correct PTZ configuration is applied to have the possibility to control the device.

VerifyMediaProfile - check the video encoder and video source configurations associated with the media profile before profile usage.
The driver verifies video encoder and video source configurations associated with the media profile using selected values during capabilities detection. In case of any changes, it tries to restore the original configuration. In case of any problem with profile operations (add/remove configuration, etc.), this option should be disabled. In this case, the driver will use a simple model without this verification. Still, we cannot guarantee that stream capabilities correspond to detected values (stream will be used as is).
Please note that multiple streaming functionality may fail if this option is disabled.

IgnoreFramerateDiscrepancy - disable checking and updating of non-important options like frame-rate of quality during settings applying
We met a couple of times when the camera supports an enumeration of option values (1, 2, 3, 3, 5, 10, and 15) but cannot provide them using ONVIF capabilities and return a whole range of values (1-15). The camera allows the application of an unsupported value but writes the nearest suitable value to the configuration. As a result, the driver may apply this value continuously without success and will not start video streaming. This option should be used to avoid such behavior (at least for frame rate and quality options), but it also may cause skipping this option if no other options are changed. So, this option should be used for debugging only and not included in the installation package by default.

BitrateRange - bitrate range for quality configuring.
The bitrate limitation will be used if the camera will not return the supported bitrate range in trt: GetVideoEncoderConfigurationOptions response. The BitrateLimit value will not be changed if this section is not presented in the XML file.
Each camera has its bitrate limits, so this section has no default values.

GovLength - the size of GOV for H.264 and MPEG-4 encodings. The GOV length includes I-frame and all dependent P- and B-frames.
The GOV length adjustment may be needed to set the required value instead of the standard 1 I-frame per second applied by the driver. Possible values of this option:

Auto - the driver adjusts GOV length automatically to 1 I-frame per second. This is the default option value

OFF - the driver will not change the GOV length option so that the user may select the required value via Web-interface/

Non-zero numeric value - the exact size of the GOV. For example, if you'd like to send one intra per 10 seconds with 15 IPS settings, the GOV length should be equal to 150.

StreamingProtocol - video streaming mode/protocol. The "RTP over UDP" is the default streaming mode. The "RTP over RTSP" mode is also supported.

RTPPacketSize - this option represents the size of RTP data of the UDP packet. Empty option means default MTU size (1400 bytes). The headers of lower network layers will not be included in this value. Unfortunately, only several manufacturers (like Axis) support such an option, so it may not affect the UDP transport.

Network interface - Address of network adapter through which the devices are connected to DVMS recorder.
The Windows sockets listen-only default network interface for multicast traffic. There will be no multicast streaming problems if the correct network interface is selected as default (including cases with a single network interface), so this option may be left empty.
However, if another interface is selected by default, the WinSock API will receive no packets, even if Wireshark will see the correct stream. In this case, the correct IPv4 address of the network interface should be specified here.

RtspSessionLogging - this option is used for analyzing the amount of re-subscribing attempts during long-term test scenarios.
Enabling this option may produce many messages in the log, so it is recommended to use it for debugging only. This option is available since driver version 1.5.0.0

Device sections

This configuration section is used to customize XML configuration for specified devices only. It should be used in cases where the configuration for the required device differs from the default configuration.

Each device should have a separate Device section. Please specify an address and port attribute in the Device tag to assign the section to the required device.

The structure of this section is the same as that of the Default section. Please refer to its description for details.

The following rules are used for parameter reading:

Check the custom Device section. If an option is presented in this section - use it;

Check the Default section. If an option is presented here - take it into use;

Otherwise, use the default (hard-coded) value.

An example of customizing of PTZ version option and Verify media profile flag for device 10.10.10.100:8080 is shown below:

XML
<?xml version="1.0" encoding="utf-8"?>

<Configuration>

  <!-- Default configuration for all subscribed IP devices -->

  <Default>...<Default>

 

  <!-- Configuration of specific devices if it differs from the default configuration -->

  <!-- Note: The device will use options from the Default section except items specified below -->

  <Device address="10.10.10.100" port="8080">

    <CapabilityDetection>

      <PtzServiceVersion>1.0</PtzServiceVersion>

    </CapabilityDetection>

    <DynamicOptions>

      <VerifyMediaProfile>No</VerifyMediaProfile>

    </DynamicOptions>

  </Device>

</Configuration>

Multicast section

Most cameras map their network settings to the ONVIF configurations, so no additional option adjustment is required after switching the Recorder to Multicast mode using the Streaming mode option.
However, in several cases, it is required to change multicast address and port settings manually:

The camera doesn't map its multicast settings to the ONVIF structures (like Axis). In this case, the user is not able to apply settings correctly without using third-party software

The camera resets one of the values after the wrong operation, so it is required to apply the correct settings again

The adjustment of several dozens of cameras requires more time than editing a single file

In any other case, if the driver wrote ter: InvalidArgVal > ter: InvalidMulticastSettings error in the log after multicast enabling

That's why the Multicast section was added to the configuration.
The structure of this section is as follows:

The BaseAddress option.
This option is used to specify an IPv4 address for the multicast group for the whole device. This address may be overridden by the Address parameter in the Stream section.

The VideoSettingsMonitoringInterval option.
For example, several cameras (like Axis) don't restart the stream after the video settings change and keep it going while video settings apply. As a result, the camera will send two multicast streams after this: one stream for Multicast: Listener with previous settings, another stream for Multicast: Primary with updated settings.
The current option allows forcing video settings querying with the required frequency (from 10 seconds to an hour) and re-subscribing the stream if any video options are changed. This option doesn't affect Multicast: Primary recorders - it is for Multicast: Listener recorders only.

The several Stream sections. Each of these sections represents settings for a separate video or audio stream.
The following attributes are used to identify each stream:

channel attribute is a 1-based index of device channel (Please do not mix up this value with DVMS channels!).
In the case of a single-channel device, this value should be 1 for all instances. For multiple channel devices, the 1..n values may be used for audio (where n is the number of video/audio channels).

Type specified type of the stream. It may be one of the following values as specified in the XML comments:

recording,

live,

remote,

audio.

Both attributes should be presented in each section. If duplicate stream instances are presented, the driver will use the first instance (as default for MSXML implementation).
If the section for any stream is not presented, the default values will be used.

Each of the Stream entries may contain one of the following parameters or both of them:

The Address parameter specifies the exact multicast address for the specified stream. There are three possible scenarios for it:

If the address is specified, it will be applied to the media profile associated with the required stream

An empty value means that the device configuration will be used as-is. However, in case the multicast address is empty, the driver will try to generate it based on the current IP address by adjusting the first octet to 224..239 range (for example, 192.168.1.145 address will be converted to 239.168.1.145)

Missing attribute means that the BaseAddress option will be used. If an option is not available, the behavior will be the same as in the previous scenario

The Port parameter specifies the multicast port that should be used for video or audio streaming.
This option may be one of the following values:

Any even value from 1024..65534 range will specify the exact port

The "Auto" option will allow the selection of port automatically by the IP device itself.
Please note that this option may not be supported by the IP device (the error about the wrong multicast configuration will be written to the Recorder log in this case); if so, please select port according to the precious note.

The existing configuration will be used in case of an empty value or missed Port parameter

The example of the configuration of multiple channel device 10.10.1.110:80 is shown below:

XML
<?XML version="1.0" encoding="utf-8"?>

<Configuration>

  <!-- Default configuration for all subscribed IP devices -->

  <Default>...<Default>

 

  <!-- Configuration of specific devices if it differs from the default configuration -->

  <!-- Note: The device will use options from the Default section except items specified below -->

  <Device address="10.10.1.110" port="80">

    <DynamicOptions>

      <!-- List of multicast group addresses that should be used for video/audio streaming -->

      <!-- Note: The ONVIF-compliant devices will not start streaming without applying of correct multicast settings and return an "ter:InvalidArgVal > ter:InvalidMulticastSettings". It means that it is required to setup Multicast configuration manually or via this section -->

      <!-- Default value: This section has no default values because multicast for each device should be configured separately -->

      <Multicast>

        <!-- Address of multicast group that will be used for all streams for the device -->

        <!-- Note: This option has no default value. If option is not presented - the driver will use current multicast configuration for each media profile -->

        <!-- Note: The driver will generate the address based on current IP address by changing of first octet (example: 224.168.10.145 for 192.168.10.145 address) in case if no correct configuration specified here and on camera side -->

        <BaseAddress>239.205.94.107</BaseAddress>

 

        <!-- Time interval (in seconds) to monitor video settings by Listener recorder -->

        <!-- Note: A few cameras allow to keep the multicast stream active after changing video settings. As a result, the camera will send two different multicast streams after settings change - one stream for the Primary recorder with new video settings and one stream for the Listener recorder with previous video settings. The settings monitoring will help the driver to understand when video settings were changed, so it will be able to close the stream with older settings and subscribe to the stream used by the Primary recorder -->

        <!-- Note: This setting does not affect Primary recorder instances -->

        <!-- Possible values: "Off" - do not use monitoring, values from "10" to "3600" seconds to query video settings for query the video settings with specified frequency -->

        <!-- Default value: "Off" -->

        <VideoSettingsMonitoringInterval>Off</VideoSettingsMonitoringInterval>

 

        <!-- It is possible to specify configuration for each stream separately -->

        <!-- Possible stream types: recording, live, remote, audio -->

        <!-- Channel is 1-based value which represents number of video/audio channel on the ONVIF-compliant device -->

        <Stream channel="1" type="recording">

          <!-- Multicast port that should be used for Recording stream of video channel 1 -->

          <!-- Possible values: "Auto" - allows camera to select multicast port itself (please note that this feature may not be supported by the camera), any even value from 1024...65534 range to specify exact port, empty or missed option - use port specified in the media profile configuration (i.e. do not change it) -->

          <!-- Default value: Empty (use current device configuration) -->

          <Port>2346</Port>

        </Stream>

 

        <Stream channel="2" type="audio">

          <!-- Multicast address that should be used for audio channel 2 -->

          <!-- Note: This value overrides address specified in 'BaseAddress' option. It may be used if the device doesn't support sending of different streams to the same multicast group -->

          <!-- Default value: The driver uses 'BaseAddress' option if this option is not specified or empty -->

          <Address>239.213.171.11</Address>

 

          <!-- Multicast port that should be used for audio channel 2 -->

          <!-- Possible values: "Auto" - allows camera to select multicast port itself (please note that this feature may not be supported by the camera), any even value from 1024...65534 range to specify exact port, empty or missed option - use port specified in the media profile configuration (i.e. do not change it) -->

          <!-- Default value: Empty (use current device configuration) -->

          <Port>8642</Port>

        </Stream>

 

        <!-- Another examples of stream configurations -->

        <Stream channel="1" type="remote">

          <Address>239.232.192.255</Address>

          <Port>Auto</Port>

        </Stream>

      </Multicast>

    </DynamicOptions>

  </Device>

</Configuration>


Please also remember the following important notes during the configuring of the multicast streaming:

Using different multicast addresses and port settings for different devices is recommended. Using the same multicast group address and port combination may cause problems in stream-receiving

The Multicast section should be added to each device separately because of the recommendation above.

The Default section contains the Multicast section as an example. The driver will not process any changes made here




Pagination
Previous page
How to enable Dahua stream encryption
Next page
Configuring VMS to use an external Microsoft SQL Server