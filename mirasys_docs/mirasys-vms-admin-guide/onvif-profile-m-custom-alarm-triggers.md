# ONVIF Profile M Custom Alarm Triggers | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/onvif-profile-m-custom-alarm-triggers

ONVIF Profile M Custom Alarm Triggers

When using ONVIF Profile M conformant devices, System Administrators can create alarm triggers in our VMS based on the metadata available on the camera side.

Go to System Manager > VMS Servers > Alarm Triggers

Create an alarm trigger

Open Alarm Triggers. A table of your custom alarm triggers will be displayed.

Click the + sign in the bottom-left corner to add an alarm trigger.
This will open the Add new alarm trigger dialog.

Select the trigger Type ONVIF.

Write the Trigger Name you have chosen for the trigger.

Select a camera in the drop-down Device menu.

Select a Topic for the trigger in the drop-down menu, such as Motion Detection.


Selection additional filters by clicking the + sign.

Filter by source and parameter
:light_bulb_on:

We highly recommend selecting optional filters by source and parameter for specifying which alarms to receive.

In the Filter by source and parameter System Administrators can add as many filters as they would like.

To Add Source, click the + sign. Select the source from the available sources in the
drop-down menu Names. Define the Value. Define the Operation.

To Add Parameter, click the + sign. Select the parameter from the available parameters in the drop-down menu Names. Define the Value. Define the Operation. Select Greater or equal or Less or equal under operation to define a value range.

To remove sources and parameters, there is a red - sign to the right of each row. Click to remove.

Click ✓ to Save. You will return to the Add new alarm trigger dialog.

If you have not entered the value, the save ✓ functionality is disabled.

Click ✓ to Save.

Edit an alarm trigger

To modify an alarm trigger, go to VMS Servers, select recorder, and under alarms, open Alarm Triggers.

Select the trigger you want to modify from the list.

Click the Modify button at the bottom left (wrench symbol).

See Create an Alarm Trigger above for instructions on how to make modifications.

Click ✓ to Save changes.

Delete an alarm trigger

To delete an alarm trigger, go to VMS Servers, and select recorder.

Open Alarm Triggers.

Select an alarm from the trigger list.

Click the red X button at the bottom left to Delete.

Confirm the deletion in the confirmation modal.

Pagination
Previous page
Web API Custom Alarm Triggers
Next page
Storage