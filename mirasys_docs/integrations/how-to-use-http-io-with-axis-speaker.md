# How to use HTTP IO with Axis IP Speaker | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/how-to-use-http-io-with-axis-speaker

How to use HTTP IO with Axis IP Speaker

Axis Speakers has feature to generate HTTP link which allow you tricker wanted audio file from speaker. Mirasys VMS side this feature can be added part of system creating HTTP IO in System Manager application to wanted server.

On this example we use Axis C1004-E Speaker.

HTTP IO supports Application GUID integration via httpio.xml file. This file default location is C:\Program Files\DVMS\DVR\.

Requirements

Licensed VMS server

Access to System Manager

Access to Axis Speaker

How to add Axis IP Speaker to VMS

Axis Speaker use same Axis driver as normal IP-camera and take 1 channel license.

Open System Manager

Go to VMS Servers

Open Hardware

Add Axis Speaker using IP-address or using search tool

Now you have added Axis Speaker part of VMS system

Getting HTTP string

Open Axis Speaker web interface using wanted browser

Go to Audio and open Audio clips

This show stored audio clips

If you want you can add own clip to speaker

Hover mouse over wanted audio clip and click three dots

This open new menu where you need to click Create link

This open new window where you can fine tune attributes

Now on this window link Copy icon and save this HTTP string to example Notepad

Creating HTTP IO

On System Manager

Go to VMS Servers

Double click Digital I/O section on wanted server

This open new window, where you can create HTTP IO

Click Add I/O button

Select HTTPIO from dropdown menu

Now you can add HTTP string to wanted status of IO.

Opened or Closed

Here example where HTTP string is added to HTTP Method (Closed).

You can test this HTTP string using Test button

Fill also needed username and password of Axis Speaker

Last click OK button to save this HTTP IO and wait that system save settings.

Now you should see under Digital I/O Settings new HTTP IO device.

You can also rename this HTTP IO device using Outputs tab

If you see this new HTTP IO device under Digital I/O Settings, you can save these setting with OK button.

Now you have created new HTTP IO device which tricker when this is closed HTTP string to Axis Speaker.

You can now move this wanted HTTP IO to wanted profile using System Manager.

You can change action of this HTTP IO when you edit this device under profile

Pagination
Previous page
Watchdog Event Provider via TCP (WDEventProviderTCP.xml)
Next page
How to use HTTP IO with PTZ camera aux commands