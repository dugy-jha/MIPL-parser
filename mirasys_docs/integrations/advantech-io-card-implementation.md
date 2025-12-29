# Advantech IO card implementation | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/advantech-io-card-implementation

Advantech IO card implementation

Mirasys VMS 9.6.1 forward we have support for Advantech IO card support. This implementation is tested with Advantech PCIE-1760 card and digital outputs and inputs.

Advantech is using this same SDK for multiple different models, so it is possible that this implementation supports other models. Mirasys is not responsible if those not tested models are not working correctly.

For older VMS version there is option to install separate driver from Extranet.

Requirements

Mirasys VMS 9.6.1 or newer

For older versions you can download separate driver from Extranet.

Advantech I/O NativeDriver feature

Card installation to PC

Check manufacturer guide how to install card to PC.

Driver installation

Before you can use IO card on Mirasys VMS, you need install Windows drivers for this card. Installation needs Administration user rights.

Download latest card drivers from Advantech support page.

XNavi, DAQ/COM/CAN series drivers/SDK/utilties installation and repack tool

When download is done, extract this zip file to wanted place; example C:\temp

Double click XNavi.exe package to start installation.

Select on first window that you want to install DAQ series components.

Click Next to continue.

After this you need to wait few seconds.

Now on this window you can select installation location and which components you want to install this PC.

Select wanted components

For this tested card needed components are

XNavi Public Tools

Select all, should be enabled as default

DAQ Series - Drivers - DAQ Demo Device

DAQ Series - Drivers - PCI/PCIE-series - PCIE-1730s/51s/52/53s/54/56s/60s/65 driver

DAQ Series - SDK - Runtime Library (Enabled on default)

DAQ Series - SDK - Device Manager

Then click Start to start installation.

Installation take few minutes.

Click Finish to close installation.

If there is need to uninstall this XNavi package etc. This is possible to do via Control Panel, Uninstall a program.

Uninstall Advantech Xnavi Products

Mirasys VMS driver installation

Download Advantech IO driver package from Extranet.

Open System Manager.

Go to System tab.

Double click Install driver under Add-ins.

Select Advantech IO driver zip package and select which server or servers you want to install this.

Wait that installation is done and close window.

IO card configuration to Mirasys VMS

Open Navigator application.

Installer has created icon to desktop and start menu.




Open DAQ series menu.

Open Installed Devices menu.

Open PCI Devices menu.

Open PCIE-1760 device/menu.

This name can be example PCIE-1760,BID#0.

This can change based on system configuration and devices.

Open Utilities.

This open new menu on right side.

On this window click Setting.

Go to DI Port section.

Enable Configure parameters of DI Filter to all wanted inputs.

Click Save.

Then Update to Device.

Go to DI Status Change Interrupt section.

Enable this to all wanted Input ports.

On default SDK allow status change only if there is coming second signal. With this change status change on VMS side real time when input is high and low.


Click Save.

Click then Update to Device, this update configuration to IO card.

After this click Save As to save this device profile.

This profile is used for Mirasys VMS side to detect how many Digital Inputs and Outputs are related to this IO card.

Save this XML file to wanted place.

Example location C:\temp

Example name AdvantechPCIE1760

Copy this file under DVR folder.

Default location C:\Program Files\DVMS\DVR

After this you can close Navigator.

Now open System Manager.

Go to second tab VMS Servers.

Open Digital I/O settings.

Click Add I/O driver down right corner.

This open new window where you can select wanted model. On this case advantechio.

Change Model to advantechio.

Select correct device for inputs.

Type input device profile path.

This need to be full path of this XML file.

Example C:\Program Files\DVMS\DVR\AdvantechPCIE1760.xml

Select correct device for outputs.

Type output device profile path.

This need to be full path of this XML file.

Example C:\Program Files\DVMS\DVR\AdvantechPCIE1760.xml

After these you can click OK to save this device to VMS Server.

When that is done, you can save Digital I/O settings.

Now you have added Advantech IO card VMS Server.

IO card Physical connections

These can be found on manufacturer user guide.

Before making wiring and connections please check manufacturer guide. Mirasys is not responsible if there is made wrong wiring etc. which cause that card got broken etc.

Digital Inputs

GND (1) is same for all inputs.

For Digital Input 8 connection point is IDI7- (2), for Digital Input 7 connection point is IDI6- (3) etc.

Digital Outputs

For output example RLY7_OUT (11) and RLY7_COM (14) are connectors for Digital Output 8 and RLY0_COM (37) and RLY0_NO (35) are connectors for Digital Output 1.

Troubleshooting

If you get error on Windows driver installation face that DVRServer.exe is running. Please stop this service and click Retry to continue driver installation. This same error may come too when you want to uninstall driver package.

Advantech SDK not allow to use IO card same time on Navigator and VMS side. If you example want to test card using Navigator.

Pagination
Previous page
Mirasys Reporting Troubleshooting
Next page
Asan UVP Gateway Connector