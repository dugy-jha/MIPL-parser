# Digital I/O Settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/digital-i-o-settings-1

Digital I/O Settings

In Digital I/O settings, you can add digital input and output devices and configure the input and output settings.
These sections describe how to set up digital I/O devices.

Drivers

In addition to the default digital I/O drivers included in the system, new drivers can be added to the system by installing them as plugins.
Once an I/O device driver has been added to the system, the device can be configured and taken into use through the Drivers tab.

To take an I/O device driver into use:

If necessary, install the device driver package.

Open the VMS Servers tab.

Select the correct server and open the Digital I/O page from the menu. 

Click Add I/O driver in the lower right corner of the screen. 

Select the driver from the Model drop-down menu. 

Configure the device settings in the Properties list.

To save the settings, click OK.

Note: After configuring a digital I/O device driver, you may need to configure the inputs and/or outputs. 

 

To edit I/O device driver settings:

Open the VMS Servers tab.

Select the correct server and open the Digital I/O page from the menu. 

Double click on the device driver you want to edit.

Edit the device settings in the Properties list.

To save the settings, click OK.

To delete an I/O device driver:

Open the VMS Servers tab.

Select the correct server and open the Digital I/O page from the menu. 

Click on the I/O device driver you want to delete.

Click Delete I/O driver in the lower right corner of the screen.

Click Ok to confirm the deletion.

Digital Inputs

You can use digital inputs to activate alarms.
In digital input settings, set the polarity of the inputs. Set the alarm actions in alarm settings.

Name. To rename an input, select the input and then type a new name for the input in Name.Active state polarity. Select the input and then select if the input is activated when the circuit is opened or closed.
Current physical state.Shows the state of a relay in real-time (Open or Closed).
Description.Here you can type a description of the selected input shown to all users in the Spotter program.
Administrative Description. Here you can type a description of the selected input shown in the Spotter program to only system administrators.

Digital Outputs

In digital outputs, select if a relay is opened or closed (polarity) when the output is triggered.

Name. To rename an output, select the output and then type a new name for the output in Name.
Active state polarity. Select the output and then select if the output is closed or opened when it is activated.
Current physical state.Shows the state of a relay in real-time (Open or Closed).
Description.Here you can type a description of the selected output shown to all users in the Spotter program.
Administrative Description. Here you can type a description of the selected output shown in the Spotter program to only system administrators.

To test a digital output, click the Change State (Toggle) button.

Pagination
Previous page
Digital I/O
Next page
LoopBack I/O