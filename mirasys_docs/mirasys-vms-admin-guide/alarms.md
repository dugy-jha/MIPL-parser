# Alarms | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/alarms

Alarms
Alarm Settings

The alarm management tools enable the creation of server-specific alarms based on various triggers based on motion, sound level or specific text data triggers.

In addition, the triggers can include custom-made third-party triggers.

Alarms can be created, edited and deleted through the Alarms screen in the VMS Servers tab.

Adding a New Alarm
General

Click New Alarm at the lower-left corner of the Alarms screen.

Type the name of the new alarm in the Name field.

Type the description and administrative description of the new alarm to the respective fields below the Name field.

Select whether the alarm is of high, average or low priority. The priority is used to define the order in which alarms are executed in case of multiple simultaneous alarms.

Select The Alarm is active until it is acknowledged to create the alarm as continuous; if the option is selected, the alarm will continue until a user acknowledges it through the Spotter application.

Alarm highlight colour allows administrators to define a custom colour for each alarm separately. 

In the View Alarms in Profiles menu, select the profiles in which the alarm will be used. Note: Alarms can also be added to profiles through the Profiles tab.

Trigger

8. Open the Trigger tab. The Trigger tab is used to define the triggers that start the alarm event.

9. Select the trigger type from the Type drop-down menu.

Camera

Audio

Metadata

Text data

Digital input

10. Select the device that will trigger the alarm from the device list below the Type drop-down menu.

11. Select the triggering condition from the condition list on the right side of the screen. 

For camera-based triggers, you can select the mask used in motion detection to trigger the alarm. 

For audio-based triggers, you can set the alarm to trigger based on a high or low audio level. 

For text data based (e.g., VCA, metadata, etc.) triggers, you can set the alarm to trigger based on a text data string.
In addition, you can set an optional alarm ending trigger by marking Define ending input and selecting a string for ending the alarm. 

For digital input-based triggers, the alarm is triggered based on the change of the input’s polarity.

Actions

12. Open the Actions tab. The Actions tab is used to define the actions performed by the alarm when it is triggered.

13. Select the action type from the Type drop-down menu. The action type defines the basic functionality of the alarm.

Action Types and Settings

The list below contains the default action types and their parameters. Some of the action types listed above may not be available on all systems.

Note: In addition to the default actions, the system may include alarm actions installed through third-party modules.

Camera Recording

Camera recording is the default action for cameras. When an alarm that contains this action type is triggered, the recording settings defined by the alarm type will be used instead of the camera’s default settings.

In Spotter, if alarm pop-up windows are enabled for the user profile, devices used with the Camera recording action are displayed in the alarm pop-up view when the alarm is triggered.

The action includes the following fields and parameters:

A) Reference picture. This static field contains the reference picture (image) of the camera. 

B) Use camera settings. The alarm recording will be performed using the camera-specific resolution and record rate setting by marking this checkbox. 

C) Resolution. Use the slider to change an IP camera’s resolution during alarm recording. The slider is active only for IP cameras.

D) Record rate. Use the slider to change the camera’s IPS rate during alarm recording. The slider is inactive if the Use camera settings checkbox is marked.

E) Pre-event recording. Mark this checkbox to set the pre-event recording on. The duration of the pre-event recording can be set through the Pre-event recording time slider.

F) Post-event recording. Mark this checkbox to set post-event recording on. The duration of the pre-event recording can be set through the Post-event recording time slider.

G) Pre- & post-event recording duration. These sliders can be used to set the pre-and post-event recording durations for the action. The sliders are active only if pre-event and/or post-event recording has been activated.

Note All devices (cameras and microphones) are connected to the alarm and have their pre-and post-event recording activated to share the same pre-and post-event recording durations.

Audio Recording

Audio recording is the default action for microphones. When an alarm that contains this action type is triggered, the recording settings defined by the alarm type will be used instead of the microphone’s default settings.

In Spotter, if alarm pop-up windows are enabled for the user profile, devices used with the Audio recording action are displayed in the alarm pop-up view when the alarm is triggered. 

The action includes the following fields and parameters:

A) Pre-event recording. Mark this checkbox to set the pre-event recording on. The duration of the pre-event recording can be set through the Pre-event recording time slider.

B) Post-event recording. Mark this checkbox to set post-event recording on. The duration of the pre-event recording can be set through the Post-event recording time slider.

C) Pre- & Post Recording duration. These sliders can be used to set the pre-and post-event recording durations for the action. The sliders are active only if pre-event and/or post-event recording has been activated.

Note: All devices (cameras and microphones) connected to the alarm and have their pre-and post-event recording activated to share the same pre-and post-event recording durations.

Digital output

The digital output is the default action for digital I/O devices. When an alarm that contains this action type is triggered, the I/O device is activated. 

Note: Even though the Pre- & Post Recording duration sliders are displayed for the action type, they do not affect the functionality of the action.

PTZ (Dome) Preset Position

The PTZ preset position action can be used to set a PTZ camera to a specified preset position. When an alarm that contains this action type is triggered, the PTZ camera will automatically move to the selected preset position. Please see Mirasys VMS Spotter User’s Guide for information on setting PTZ camera preset positions.

It should be noted that this action moves the PTZ camera to a preset position but does not result in the video feed from the PTZ camera being displayed in the alarm view in the client application unless other alarm actions, such as Camera recording, has been selected for the PTZ camera. 

The action includes the following fields and parameters:

Position. Use the drop-down menu to select the preset position to which the PTZ camera will move during the alarm.

Note: Even though the Pre- & Post Recording duration sliders are displayed for the action type, they do not affect the functionality of the action.

PTZ (Dome) Camera Tour

The PTZ camera tour action can be used to set a PTZ camera to start a pre-programmed PTZ camera tour. When an alarm that contains this action type is triggered, the selected PTZ camera tour is started. Please see Mirasys VMS Spotter User’s Guide for information on setting PTZ camera tours.

It should be noted that this action starts the PTZ camera tour but does not result in the video feed from the PTZ camera being displayed in the alarm view in the client application unless other alarm actions, such as Camera recording, has been selected for the PTZ camera. 

The action includes the following fields and parameters:

Program. Use the drop-down menu to select the PTZ camera tour, starting when the alarm is triggered. 

Note: Even though the Pre- & Post Recording duration sliders are displayed for the action type, they do not affect the functionality of the action.

Set Motion Detection Mask

The Set motion detection mask action can change the motion detection mask used by a specific camera during the alarm. When the alarm occurs, the motion detection mask used for the designated camera is changed to the alarm specific mask. After the alarm ends, the system restores the default mask. 

The action includes the following fields and parameters:

Mask. Use the drop-down menu to select the motion detection mask that will be used during the alarm.

Note: Even though the Pre- & Post Recording duration sliders are displayed for the action type, they do not affect the functionality of the action.

Send E-Mail

The Send e-mail action can be used to send e-mail to any email address or group configured in the E-mail settings in the System tab. 

You can choose which recipient or group should receive the alarm.

You can also include one or more unscaled or scaled-down images in the alarm email. To do this, uncheck the Send in a short format -option and check the Attach images –option

After this, you can choose a camera, size for the image scaling, desired number of images, and the time span from which the images are fetched.

Note: 

The number of images in this configuration is the maximum amount delivered. Fewer images might arrive 

Attaching images to alarm emails might lead to high data traffic, so it is recommended to test the configuration settings to find the optimum setting.

If you experience issues that no images are arriving with the default settings, it is recommended to select more than one image to the “maximum images” setting and adjust the sliders slightly to have a longer duration of time where the images are being fetched.

The action includes the following fields and parameters:

Format – Defines the message format as short or usual. 

A short message will contain only up to 160 characters and cannot contain additional message text or image attachments (see below).

Message – This field contains the message that will be sent to the recipients if the alarm occurs. The message field is active only if the e-mail format has been set as long. 

Note: 

Unlike other alarm actions, the Send e-mail action can be selected only once for each alarm. Once selected, the action will disappear from the list of available actions.

The message will have the alarm name in the title.

Disable Alarms

The Disable alarms action can be used to send disable alarms based on one alarm. The configuration can be done so that all alarms are disabled, low and medium priority alarms, or low alarms. 

This option allows specific alarms to remain active while others are suppressed. 

The alarms are disabled only while the alarm that disables them is active.

ONVIF Profile M

ONVIF profile M support enables our system to respond to the triggering of an alarm generated by camera analytics.

ONVIF alarm

When you have added a device that supports ONVIF Profile M, you do not need to take any special steps to enable or disable these triggers. They are automatically added to the camera's metadata triggers.

In the Alarm Configuration in System Manager, this will be displayed in the Trigger tab and listed as ONVIF. You can use these to create new alarms.

Creating an ONVIF alarm trigger

Note that device alarms/triggers itself should be configured using device web interface, not in the System Manager.

This configuration should be done before you add device to VMS. Otherwise device capabilities should be refreshed in System Manager for it to include the changes in device.

Start the System Manager desktop application.

Add a device with ONVIF Profile M support.

Go to the VMS Servers tab.

Select Alarms.

Select a New Alarm.

The General tab opens. Name the alarm in the general tab, and select which profiles will use the alarm.

Go to the Trigger tab.

Select Metadata as the type.

Select the type of ONVIF metadata you want to use to trigger the alarm.

Go to the Actions tab and select the desired action for the alarm.

Go to the Calendar tab and select which days/hours are enabled for the alarm. By default, the alarm is active 24 hours each day.

Click the OK checkmark ☑️ at the bottom of the page

Calendar

Define that when the alarm is active

Click OK

Holiday Schedules

Alarm specific holiday schedules can create schedules for specific dates or set a specific date to use an alarm schedule designed for another weekday. The Holidays sub-tab can be accessed through the alarm’s Schedule tab.

To set a specific date to function with another weekday’s schedule:

Select the weekday from the schedule list on the left side of the screen.

Select the desired year and month from the drop-down menus above the calendar.

Click on a date in the calendar to add the schedule.

To create a custom schedule:

Click Add at the upper left side of the screen.

Type the name of the holiday schedule in the Schedule name field.

To create the schedule, select Off from the On/Off list on the left side of the screen and mark the hours the alarm is switched off for the day.

Click OK to save the schedule.

Select the desired year and month from the drop-down menus above the calendar.

Click on a date in the calendar to add the schedule.

To edit a custom schedule:

Select the custom schedule from the schedule list on the left side of the screen.

Click Edit at the upper left side of the screen.

Edit the schedule.

Click OK to save the changes.

To delete a custom schedule:

Select the custom schedule from the schedule list on the left side of the screen.

Click Remove at the upper left side of the screen.

To restore the original schedule:

Click Restore in the schedule list on the left side of the screen.

On the calendar, click the day that you want to restore.

Deleting an Alarm
To delete an alarm:

On the VMS Servers tab, select the server.

Double-click on Alarms.

Select the alarm you want to delete by clicking on its name.

Click Remove Alarm at the lower-left corner of the Alarms screen.

The alarm is deleted from the system.

Pagination
Previous page
UniversalOutputDriver
Next page
Storage