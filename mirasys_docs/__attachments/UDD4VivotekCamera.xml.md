# 

Source: https://documentation.mirasys.com/__attachments/a_2522e3f924abdf6847562da6339fbd2ec46691b6e18ec3c6e3f6b2ba2bd74665/UDD4VivotekCamera.xml?cb=f06a84d287a2e4f51bbe69ae149a7557

This XML file does not appear to have any style information associated with it. The document tree is shown below.

<root>
<channelConfig>
<linefeed value=""/>
<ignored value="0x00"/>
</channelConfig>
<validation>
<regex value=".*"/>
</validation>
<uddXmlMapper version="2">
<messageType value="text" parsing="regex">
<message number="1" value="VivotekEvent">
<param number="1" value="EVENT_TYPE=(.+)" group="1"/>
</message>
</messageType>
<constants>
<array name="EventName" params="VivotekEventNames">
<value>Video motion detection</value>
<value>Camera tampering detection</value>
<value>Periodic</value>
</array>
</constants>
<rules>
<message number="1" value="VivotekEvent" alwaysShowText="yes">
<param number="1" reference="1" operator="eq" value="$EventName" id="VivotekEventNames">
<action number="1" type="event" value="$EventName"/>
</param>
</message>
</rules>
</uddXmlMapper>
</root>