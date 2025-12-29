# Pacom Unison | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/pacom-unison

Pacom Unison

This integration allows for automatic video retrieval in case of an alarm or event for rapid visual alarm verification. Video can be recorded and played/paused which facilitates analysis of any alarm or event that has occurred in Unison. Two way audio can also be streamed between the video device and Unison (listen-in/microphone). Operators are able to manage the cameras in order to view the desired position and angle using the PTZ (Pan/Tilt/Zoom) function and select preset positions.

Requirements

Unison Gateway Connector feature

This allows Unison and Mirasys VMS “talk” together to fetch devices etc.

Web App Spotter Rest API feature

This allows Unison control Mirasys Spotter layouts

Configuration

First you need configure Mirasys Gateway and Spotter softwares until you can use Unison integration.

When these are done you can add Mirasys VMS to Unison system.

Configuring Mirasys Gateway

Stop DVMSGatewayService under Windows Services

Go to Gateway installation folder

Open file ServiceLauncher.exe.config using example Notepad++

Find line

<add key=”GatewayServerPort” value=”9000” />


Change this port value to example 9010

Port need to change because Unison use port 9000 for own system

Before changing port check that this port is free to use

Save file

Start DVMSGatewayService under Windows Services

Configuring Mirasys Spotter

Run Spotter Run As Administrator

Go to File → Settings → Advanced tab

Enable Public Web Api

Use default port

Other information

Unison server can send messages via XML or ASCII format. Mirasys VMS can get these via Text Channel.

There is then option to build UDD file which generate these messages as trigger events on VMS side and these can be used to trigger alarm event and record material.

Troubleshooting
Communication error in Unison system

Check that you are using correct GUID for Gateway and Spotter

Check that ports are opened that Unison can make connection to VMS server and Spotter

Pagination
Previous page
Paxton Net2 Access Control System Proxy
Next page
Qognify Gateway Connector (Situator)