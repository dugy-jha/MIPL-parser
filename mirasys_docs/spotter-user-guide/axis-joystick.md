# AXIS joystick | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/axis-joystick

AXIS joystick

AXIS joystick setup for Axis T8311, AXIS 8312, and AXIS 8313.

In Mirasys 8.33, default setups were added to the AXIS 295 Video surveillance joystick. Please read more here.

​​Refactor​ing in Mirasys 8.3.3

​The input device driver level was removed since Spotter only supports DirectX devices at the moment

Input device settings buttons tooltips were added to give more information to the user about what buttons do

The title was added to devise settings and setup settings

Scrolling of the input device operations list was fixed to operate more smoothly

​Default setup support

Two buttons were added to input device settings UI

Clear

To clear the setup

Default

To set the default setup

This only works if there are default setup defined for the detected device.

Default setups were added to devices

DCZ

CH Products IP Desktop Controller

AXIS 295 Video surveillance joystick

Default input device setups are disassembled to folder C:\Users\<WindowsUser>\AppData\Roaming\DVMS\DVR Application\DefaultPTZConfig. When the "Default" button is clicked, the default setup from the folder is read, and its config is loaded to UI. The format of the default setup is the same as when importing and exporting device setup.

Axis T8311 default setup

Default setup buttons:

X-axis: move left/right

Y axis: move up / down

Z axis: PTZ near / far

J1: Ptz open/close​

J2: Select the camera

J3: Quick select camera

​J4: Select the PTZ preposition

L: Play backward

R: Play forwards

Axis T8312 keypad default setup

Default setup buttons:

Button 0 - Button 9: 0 - 9​

Button 10 (Tab): Navigate to select tab content

Button 11 (Alt): Enter

Button 12: Quick select window

Button 13: Quick select camera

Button 14: Ptz select preposition

Axis T8313 jogdial default setup

Jog wheel: Play forward / backward

Shuttle wheel: Step forward / backward

Button 1: Quick bookmark

​​Button 2: 

Button 3: Playback pause

Button 4: 

Button 5 (L): Camera export image

Button 6 (R)​: Quick storyboard

Changes in V9: Setup name added in selected device layout

To improve selected setup findings between different clients, the selected setup name is added to user layouts. If the setup instance id search does not match, then the search by setup name is tried.

Related links

https://www.axis.com/dam/public/57/bf/60/axis-t8310t8311t8312t8313--user-manual-en-US-38652.pdf

Pagination
Previous page
DirectX devices
Next page
VM Desktop default setup (DirectX and AXIS)