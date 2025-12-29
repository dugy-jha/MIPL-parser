# How to use Mirasys VMS Text Channel | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-use-mirasys-vms-text-channel

How to use Mirasys VMS Text Channel

The following instructions guide how to configure a text data channel by using an example configuration file and TCP connection.

Copy the UDD4Demo.xml configuration file to the DVR subfolder under the VMS installation folder. The default VMS installation folder is “C:\Program Files\DVMS\DVR“.

Example UDD4Demo.xml configuration file content can be found at the end of this guide.

Configure the text data channel in the System Manager.

Open the System Manager application.

Open the second tab, where the VMS server settings can be found.

Open Text channel settings.

Click the first reconfigured text data channel from the list.

Click to add channels using the button below the list.

In the “Add New Text Channel” dialog, select the UniversalDataTcpModel as a model.

Configure the settings using the following configuration.

Click ok from the dialog to confirm the text data channel configuration.

Name the text data channel and define the description if needed.

Click ok from the text data settings to save the settings.

Make sure that the port that was defined in the text data channel settings is open in the firewall.

After the VMS server configuration is done, an external application can be used to send text data to the TCP port. You can use, for example, the Putty application to send these ASCII commands to the Mirasys VMS port.

Download the putty.exe and run it

Use the following configuration in the Session

Hostname or the IP address of the VMS server

Port = 40000

Connection type = Other/Raw

Click Open to create a TCP connection from Putty to the VMS service

In the Putty console, the following commands can be written to send events to the VMS service
start low
start normal
start high

stop low
stop normal
stop high

In the System Manager application, the text data events can be used to configure alarms.

UUD4Demo.xml configuration file content

The following text data configuration file defines text data alarm triggers that are parsed from the incoming text data.

XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
<logging>
  <level value="2"/> 
  <additionalDebug value="no"/>
</logging>
  <channelConfig>
    <linefeed value="0x0d0a"/>
    <ignored value="0x00,0x0B"/>
    <clearscreen value="-----"/>
  </channelConfig>
  <validation>
    <regex value=".*"/>
  </validation>
  <uddXmlMapper version="2">
    <messageType value="text" parsing="regex">
      <message number="1" value="alarm">
		<param number="1" value="([a-zA-Z]+) (.+)" group="1"/>
		<param number="2" value="([a-zA-Z]+) (.+)" group="2"/>
	  </message>
    </messageType>
	<constants>
		<array name="Rules" params="AT">
            <value>start</value>
            <value>stop</value>
        </array>
		<array name="AlarmType" params="AT">
            <value>temp</value>
			<value>normal</value>
            <value>low</value>
        </array>
    </constants>
    <rules>
		<message number="1" value="alarm" alwaysShowText="yes">
            <param number="1" reference="1" value="$Rules" operator="eq" id="AT">
				<and number="1" reference="2" value="$AlarmType" operator="eq"/>
				    <action number="1" type="event" value="$Rules $AlarmType alarm" />
            </param>
		</message>
  </rules>
  </uddXmlMapper>
</root>

Pagination
Previous page
Crash Dump Generation
Next page
How to reset usernames and password to default