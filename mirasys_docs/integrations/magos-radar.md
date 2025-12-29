# Magos Radar | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/magos-radar

Magos Radar

Magos Radar System integration to Mirasys VMS can be done via Text Channel. License include this option already, there is only configuration needed to do.

Requirements

Latest Mirasys VMS

Magor Radar System where is configured data sending to wanted IP-address and port

Magos Radar System had own license feature for metadata sending

Configuration

Copy Magos Radar UDD file to DVR-folder

Open System Manager and logon there using Administrator user rights

Go to Serves tab and open Text Channels

Make there new Text Channel

Mode; UniversalDataTcpModel

TCP Port number; 40000 or next free one

Validation; Text, this depends type of data

Configuration file; UUD4Magos.xml

Custom validator; Empty

Send the “End” event after N; 0

Forward incoming message to; empty

Now you can save these settings and check via Spotter that Text Channel is working and you can see data from Magos Radar System.

If you are using different profile on Spotter side, please add this Text Channel to wanted profile, without this you can’t see this Text Channel on Spotter

When everything is working and you can see data on Text Channel you can use System Manager to do alarms based on Magos Radar System metadata events.

Troubleshooting

No data in Text Channel

Check configuration and test that Magos Radar system is working as normal.

Event missing

If there is event missing, you can add this to XML file and then restart services to reload this new file.

Example UDD4Magos.xml file
XML
<?xml version="1.0" encoding="utf-8"?>
<root>
    <channelConfig>
        <linefeed value="0x0A" /> <!-- this is CR+LF, change to 0x0A if only LF is used as message delimiter -->
        <ignored value="0x00" />
        <clearscreen value="" />
    </channelConfig>
    <logging>
        <level value="2"/>
        <additionalDebug value="no"/> <!-- set to "yes" to get debugging files, like incoming messages into Debug_UDD_Packets.bin file located in DVMS/DVR-folder-->
    </logging>
    <validation>
        <regex value="ZoneAlarm.*" /> <!-- all incoming messages starting ZoneAlarm will be processed -->
    </validation>
    <uddXmlMapper version="2">
        <messageType value="text" parsing="regex">
            <message number="1" value="AlarmMessage">
                <param number="1" value="(.+)" group="1" /> <!-- event -->
            </message>
        </messageType>
         <constants>
            <array name="sevent" params="Alarms">
                <value>ZoneAlarm_Alarm_test</value>
				<value>ZoneAlarm_Area1</value>
				<value>ZoneAlarm_Area2</value>
			</array>
        </constants>	
        <rules>
            <message number="1" value="AlarmMessage" alwaysShowText="yes"> <!-- change to "no", then only events will be shown -->
                <param number="1" reference="1" type="string" value="$sevent" operator="eq" id="Alarms" >
                    <action number="1" type="event" value="$sevent" />
                </param>
            </message>
        </rules>
    </uddXmlMapper>
</root>

Pagination
Previous page
Lenel OnGuard
Next page
Moxa device configuration for PTZ