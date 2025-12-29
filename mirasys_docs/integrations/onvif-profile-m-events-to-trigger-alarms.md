# ONVIF Profile M events to trigger alarms | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/onvif-profile-m-events-to-trigger-alarms

ONVIF Profile M events to trigger alarms

Mirasys first introduced ONVIF M support in VMS 9.7.0 version, after which the functionality has been improved to make it easier to use. The feature enables you to use camera analytics-generated events to trigger a VMS system alarm.

Before starting to configure the ONVIF M-based alarms, please ensure that you have the latest Mirasys VMS installed and that the latest ONVIF driver is being used.

Event Messages

The VMS service listens to the ONVIF Profile M event messages from the camera. Each camera that uses the ONVIF driver can be configured in the System Manager VMS Service alarm trigger setting to define which ONVIF Profile M event messages are used for alarm triggering.

Profile M event message includes details about the camera analytics events as topics. Usually, topics are named similarly, as the camera analytics function on the camera side.

Sample event data

The ONVIF Profile M event data varies depending on the camera manufacturer and camera model. Below are some examples of the event data from different manufacturers.

Avigilon
Topic: tns1:RuleEngine/tnsavg:ObjectCrosses
UTC Time: 2025-09-16T08:07:18.981Z
Source:
    VideoSourceConfigurationToken = "camCfg0"
    VideoAnalyticsConfigurationToken = "ana0"
    Rule = "Port Wrong"
Key:
    EventId = "12439"
Data:
    ChannelId = "0"
    ObjectType = "1"

Topic: tns1:RuleEngine/LineDetector/Crossed
UTC Time: 2025-09-16T08:07:18.981Z
Source:
    VideoSourceConfigurationToken = "camCfg0"
    AnalyticsConfiguration = "ana0"
    Rule = "Port Wrong"
Data:
    ObjectId = "2166734"
    ClassTypes = "Human"

Axis
Topic: tnsaxis:CameraApplicationPlatform/ObjectAnalytics/Device1Scenario1
Property Operation: Changed
UTC Time: 2025-09-25T06:19:36Z
Data:
    active = "1"
    objectId = ""
    classTypes = ""

Topic: tnsaxis:CameraApplicationPlatform/ObjectAnalytics/Device1Scenario1
Property Operation: Changed
UTC Time: 2025-09-25T06:19:43Z
Data:
    active = "0"
    objectId = ""
    classTypes = ""

Bosch
Topic: tns1:RuleEngine/LineDetector/Crossed
UTC Time: 2025-10-02T07:22:14.767Z
Source:
    VideoSource = "1"
    Rule = "Entering field 4"

Topic: tns1:RuleEngine/LineDetector/Crossed
UTC Time: 2025-10-02T07:22:15.026Z
Source:
    VideoSource = "1"
    Rule = "Crossing line 2"

Hanwha
Topic: tns1:OpenApp/WiseAI/LineCrossing
Property Operation: Changed
UTC Time: 2025-09-25T06:51:00.684+00:00
Source:
    Channel = "0"
    AppName = "WiseAI"
    AppID = "WiseAI"
    AppEvent = "LineCrossing"
    Type = "Event"
    RuleIndex = "1"
    VideoSourceToken = "vs-0"
    RuleName = "LineCross"
Data:
    State = "true"
    ObjectId = ""
    Action = ""

Topic: tns1:OpenApp/WiseAI/ObjectDetection
Property Operation: Changed
UTC Time: 2025-09-25T07:00:41.412+00:00
Source:
    Channel = "0"
    AppName = "WiseAI"
    AppID = "WiseAI"
    AppEvent = "ObjectDetection"
    Type = "Event"
    RuleIndex = "1"
    VideoSourceToken = "vs-0"
    RuleName = "ObjectDetectionRule-1"
Data:
    State = "true"
    ClassTypes = "Person"

Topic: tns1:OpenApp/WiseAI/ObjectDetection
Property Operation: Changed
UTC Time: 2025-09-25T07:00:42.512+00:00
Source:
    Channel = "0"
    AppName = "WiseAI"
    AppID = "WiseAI"
    AppEvent = "ObjectDetection"
    Type = "Event"
    RuleIndex = "1"
    VideoSourceToken = "vs-0"
    RuleName = "ObjectDetectionRule-1"
Data:
    State = "false"
    ClassTypes = ""

Configuring alarm triggers and alarms

Open the System Manager and select the VMS Servers tab.

Add a camera in the Hardware settings by using the ONVIF driver.

Some cameras require enabling the ONVIF protocol in the camera settings and creating a username and password for it.

Open the Alarm Triggers settings.

Click the “Add new alarm trigger” icon.

Select the ONVIF type.

Give a name for the trigger.

Select the desired Device.

The device is showing up with that name, which is defined for it.

Choose the desired topic.

Please check the example metadata section to select the correct topic.

To make the trigger work properly, it is recommended to add additional filters. This can be done by clicking the Select additional filters.

Depending on the camera model, multiple event messages can use the same topic, and to filter the correct one, there is an option to add source, parameter types to filters, or both.

Example for Avigilon: Source is RuleName, and type for Value is the rule name, which is defined on the camera side.

Example for Axis: Parameter Name is Active, type for Value is True, and Operation is Equal.

Example for Bosch: Source Name is RuleName, type for Value is Crossing line 2, and Operation is Equal.

Example for Hanwha: Source Name can be used as RuleName, the type for Value is LineCross, and Operation is Equal.

Click “OK” to save the filters.

Click “OK” to save the alarm trigger.

Click “OK” to close the Alarm Triggers section.

Open Alarms settings to configure alarms that use the configured alarm triggers.

To find this Alarm Trigger, select the type of metadata and select the source camera.

The shows a list of created triggers, where you can choose the desired one.

Configure the rest of the alarm settings and click the Ok button to approve the alarm configuration.

Once all alarms are configured, click the Ok button to save the alarm settings.

Additional configuration

In case the event data sent by the camera does not include source/channel information, the event messages are received by the camera channel 1. This applies to all one-lens and some multi-lens cameras.

When configuring analytics on the camera side, some camera capabilities need to be updated until all the latest topics are visible from the camera. The camera capabilities update can be done in the following way.

Open Hardware settings from the System Manager VMS Servers section.

Select the camera whose capabilities need to be updated and click the “Edit IP Camera” button.

Click the “OK” button to request the latest capabilities from the camera.

If multiple driver options are offered, select the ONVIF driver.

Click the “OK” button to accept to add audio and I/O channels if needed.

Click the “OK” button to save the changes.

Avigilon specific configuration

If the camera is not sending the ONVIF Profile M events to the VMS service, please check that Extended Settings are enabled on the Avigilon camera side. On the Avigilon camera Extended Settings page, you can configure the ONVIF Settings in the following way.

Select the Enable Multi-Packet XML Documents checkbox to enable multi-packet XML documents to reduce metadata size. Only for Video Management systems that support multi-packet XML documents.

Select the Enable Analytics Options Requests checkbox to enable the GetAnalyticsModuleOptions and GetRuleOptions Requests.

Select the Enable Analytics XML Metadata checkbox to send analytics metadata in the XML metadata stream.

Select the Enable Run-Length Encoding of Motion Mask checkbox to enable run-length encoding of the motion mask. Only for Video Management Systems that do not require an unencoded mask.

Select the Enable Supplemental Events checkbox to send supplemental events not defined by ONVIF that may be useful to some Video Management Systems.

Select the Enable Singleton Analytics Events checkbox to send singleton Analytics events instead of property events.

Click Apply to save your changes.

Pagination
Previous page
ONVIF devices
Next page
HTTPS encryption