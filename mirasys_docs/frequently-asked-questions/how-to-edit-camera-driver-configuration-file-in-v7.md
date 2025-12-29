# How to edit camera driver configuration file | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-edit-camera-driver-configuration-file-in-v7

How to edit camera driver configuration file
Mirasys VMS V9 offers many possibilities to configure camera drivers via System Manager. But sometimes, you may need to edit the camera driver configuration file.

These configuration files tell the VMS what settings can change on the camera or VMS side. Different camera drivers have different options stored on this configuration file.

In a situation in which you need to change, for example, the camera streaming type from default RTPoverUDP to RTPoverRTSP, this can be done with the following steps in the VMS server:

Open System Manager, go to the Recorder section, and open Cameras settings.

On this window, you can check what driver is used on this camera where you want to make a change.

In this example, the driver used for the Axis P5534 camera is NewAxisIPCapture.

You can go to the VMS installation folder now that you know the driver details.
Default installation paths are
For x86 C:\Program Files (x86)\DVMS\
For x64 C:\Program Files\DVMS\

Go to the DVR folder; under this folder, you can find the camera driver configuration files.
In this example, we know that the camera is using the NewAxisIPCapture driver.
For this configuration, the file name is NewAxisIPCapture.xml.

Copy this file on your desktop and open it with Notepad.
Depending on the camera driver configuration file, Configuration sections affect all of the same cameras using the same camera driver.
Some camera driver configurations have end-of-file camera-specific settings.

We are interested in this part of the camera driver configuration file in this example.
<RTPMode>RTP over UDP</RTPMode>

That tells us that camera streaming is using RTP over UDP mode. To change this using different streaming, you must replace this value with this.
<RTPMode>RTP over RTSP</RTPMode>

In the configuration file, it is specified before values, which are accepted per section.

Now, when this change is done, you can save this file.
Before replacing the old configuration file, stop VMS services on Windows Services.

Stop first WDServer, then DVRServer, and last SMServer.
When services are stopped, you can copy/replace the old camera configuration file with this new one.

When this is done, you can start VMS services on Windows Services.

Start first WDServer, then DVRServer, and last SMServer.

The system detects this change from the camera configuration file when services are up and running. It starts using other streaming types for this specific camera or all cameras using the same camera driver.

In this example, we have changed this mode to affect all cameras using the same camera driver.

Pagination
Previous page
“No signal” messages appear randomly from the IP cameras
Next page
How to enable Dahua stream encryption