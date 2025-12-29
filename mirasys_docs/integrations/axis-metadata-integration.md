# Axis metadata integration | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/axis-metadata-integration

Axis metadata integration

Axis metadata integration to Mirasys VMS can be done via Text Channel. License include this option already, there is only configuration needed to do.

Requirements

Latest Mirasys VMS

Axis camera where is configured data send to the desired IP address and port

Configuration

Copy Axis UDD file to DVR folder

Open System Manager and log in there using Administrator user rights

Go to the Serves tab and open Text Channels

Make their new Text Channel

Model: UniversalDataTcpModel

TCP Port number: 40000 or the next free one

Validation: Text, this depends type of data

Configuration file: UUD4Axis.xml

Custom validator: Empty

Send the “End” event after N: 0

Forward incoming message to: empty


Now you can save these settings and check via Spotter that Text Channel is working and you can see data from camera.

If you are using a different profile on the Spotter side, please add this Text Channel to the wanted profile; without this, you can’t see this Text Channel on Spotter.

When everything is working and you can see data on Text Channel you can use System Manager to do alarms based on camera metadata events.

Troubleshooting

No data in Text Channel

Check the configuration and test that the camera is working as normal on the VMS side.

Event missing

If there is event missing, you can add this to XML file and then restart services to reload this new file.

Example UUD4AxisASCII.xml file
XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
<logging>
  <level value="2"/> 
  <additionalDebug value="no"/>
</logging>
  <channelConfig>
    <linefeed value="0x0a"/>
    <ignored value="0x05,0x00"/>
    <clearscreen value="-----"/>
  </channelConfig>
  <validation>
    <regex value="[a-zA-Z0-9[:space:]\\:]*" />
  </validation>
  <uddXmlMapper version="2">
    <messageType value="text" parsing="regex">
      <message number="1" value="alarm">
		<param number="1" value="([a-zA-Z0-9[:space:]\\:]+)" group="1"/>
	  </message>
    </messageType>
	<constants>
		<array name="Events" params="Axis">
            <value>TEST</value>
            <value>Trigger</value>
        </array>
    </constants>	
    <rules>
		<message number="1" value="alarm" alwaysShowText="yes">
            <param number="1" reference="1" operator="eq" value="$Events" id="Axis">
				    <action number="1" type="event" value="$Events alarm" />
            </param>
		</message>
  </rules>
  </uddXmlMapper>
</root>

Example UDD4AxisMD.xml file
XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
<!--Axis Motion Detection 4 UDD file-->
<!--Configure camera sending data via TCP to VMS server IP and Port-->
<logging>
  <level value="2"/>
  <additionalDebug value="no"/>
</logging>
  <channelConfig>
    <linefeed value="0x0a"/>
    <ignored value="0x05,0x00"/>
    <clearscreen value="-----"/>
  </channelConfig>
  <validation>
    <regex value="[a-zA-Z0-9[:space:]\\:]*" />
  </validation>
  <uddXmlMapper version="2">
    <messageType value="text" parsing="regex">
      <message number="1" value="alarm">
		<param number="1" value="([a-zA-Z0-9[:space:]]+)" group="1"/>
	  </message>
    </messageType>
	<constants>
		<array name="Events" params="AxisMD">
		<value>Camera 1 Intrusion Zone 1</value>
		<value>Camera 1 Intrusion Zone 2</value>
		<value>Camera 2 Intrusion Zone 1</value>
		<value>Camera 2 Intrusion Zone 2</value>
		<value>Camera 3 Intrusion Zone 1</value>
		<value>Camera 3 Intrusion Zone 2</value>
		<value>Camera 4 Intrusion Zone 1</value>
		<value>Camera 4 Intrusion Zone 2</value>
        </array>
    </constants>	
    <rules>
		<message number="1" value="alarm" alwaysShowText="yes">
            <param number="1" reference="1" operator="eq" value="$Events" id="AxisMD">
				    <action number="1" type="event" value="$Events alarm" />
            </param>
		</message>
  </rules>
  </uddXmlMapper>
</root>

Pagination
Previous page
Asan UVP Gateway Connector
Next page
Axis Perimeter Defender application