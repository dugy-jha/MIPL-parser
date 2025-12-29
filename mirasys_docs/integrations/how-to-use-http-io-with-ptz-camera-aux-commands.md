# How to use HTTP IO with PTZ camera aux commands | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/how-to-use-http-io-with-ptz-camera-aux-commands

How to use HTTP IO with PTZ camera aux commands

HTTP IO is very powerful option to control example PTZ camera aux commands. This allow user example enable wiper directly on Spotter.

On this example we use Hanwha XNP-C6403RW PTZ camera.

HTTP IO supports Application GUID integration via httpio.xml file. This file default location is C:\Program Files\DVMS\DVR\.

Requirements

Licensed VMS server

Access to System Manager

Access to PTZ Camera

Creating IO

On System Manager

Go to VMS Servers

Double click Digital I/O section on wanted server

This open new window, where you can create HTTP IO

Click Add I/O button

Select HTTPIO from dropdown menu

Now you can add HTTP string to wanted status of IO.

Opened or Closed

Please remember fill username and password if that is needed for authentication

Example HTTP commands for Hanwha PTZ Camera

Run camera wiper once
http://CAMERAIP/stw-cgi/ptzcontrol.cgi?msubmenu=aux&action=control&Command=WiperOn

Run camera vibration once
http://CAMERAIP/stw-cgi/ptzcontrol.cgi?msubmenu=aux&action=control&Command=VibrationOn

Enable/Disable camera heater
http://CAMERAIP/stw-cgi/ptzcontrol.cgi?msubmenu=aux&action=control&Command=HeaterOn
http://CAMERAIP/stw-cgi/ptzcontrol.cgi?msubmenu=aux&action=control&Command=HeaterOff


When information is saved to HTTP IO Properties, this can be saved.

Now VMS store this information and show this as Digital Output in VMS environment.

Now you should see under Digital I/O Settings new HTTP IO device.

You can also rename this HTTP IO device using Outputs tab

If you see this new HTTP IO device under Digital I/O Settings, you can save these setting with OK button.

Now you have created new HTTP IO device which tricker action when this is closed or opened HTTP string to PTZ Camera.

You can now move this wanted HTTP IO to wanted profile using System Manager.

You can change action of this HTTP IO when you edit this device under profile




Pagination
Previous page
How to use HTTP IO with Axis IP Speaker
Next page
How to add Axis IP Speaker to Mirasys VMS