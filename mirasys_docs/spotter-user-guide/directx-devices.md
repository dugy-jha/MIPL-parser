# DirectX devices | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/directx-devices

DirectX devices

Spotter supports DirectX input devices that can be used mainly to control camera PTZ.

DirectX control devices

Spotter supports DirectX input devices (joysticks). They can control different Spotter functionalities, normally PTZ cameras.

The control devices have various axes and buttons. The driver detects these by using DirectX interfaces.

Operations (changes in device button states and Axis positions) are detected through the DirectX interface.

Control device settings

From the Spotter main menu, choose Spotter Device settings and then Control Device settings. In the device settings, you get a list of detected input devices.

Each input device can have common settings. Common device settings are:

Use absolute axises

Dead zone setting

Each device can have a number of different setups, but only one can be selected at a time. Input device setup maps input device button and axis changes to Spotter operation.

​​Shared device setups​

In Adder, a shared folder is added under user device configuration to split own ad shared setups.

In Carp, a new boolean property of IsShared is added.

Spo​​tter

In Input device settings, own and shared joystick settings are shown with different icons:

​When shared settings are selected, only SaveAndClose and Close buttons are enabled. The content of the settings can not change.




​​​Default setup support

Clear

To clear the setup

Default

To set the default setup

This only works if there are default setup defined for the detected device.

Default setups were added to devices

DCZ

CH Products IP Desktop Controller

AXIS 295 Video surveillance joystick

Default input device setups are disassembled to folder C:\Users\<WindowsUser>\AppData\Roaming\DVMS\DVR Application\DefaultPTZConfig. When the "Default" button is clicked, the default setup from the folder is read, and its config is loaded to UI. The default setup format is the same as when importing and exporting device setups.

Virtual joystick default setup

​​Default setup buttons:

​​C1: The last camera remembers the last camera selection, so it goes​ to the last camera and calls up in the “active Selected Camera” position

C2: Previous camera, UP, or PREVIOUS button will change “Active Selected Camera” to ​the PREVIOUS in the selected profile folder in the tree.​

C3: Next camera, DOWN button, will change “Active Selected Camera” to the next in the selected profile folder in the tree

C4: Snapshot of active Camera Selected Saves a picture with date and time as name to the default location

C5: Focus near

C6: Focus far

C7: Iris Open

C8: Iris Closed

C9: Window selected grid to full screen / back to normal

C10: Ptz open / close

C11: Quick Bookmark​​

C12: Set selected window to Live

C13: Quick Storyboard

*: PTZ Home

​#: ​​Navigate and select the camera

Right Buttons by jog shuttle Grid selection advance move to NEXT camera a.  Right button when selected will go to the next camera in the grid as the “Active Selection”  IE if they have 6 PTZs’ up. They hit the right button, which moves PTZ control to the NEXT camera, and the joystick can now control that camera.

Left Button by jog shuttle Grid selection advance move to PREVIOUS camera a.  Left button when selected will go to the PREVIOUS camera in the grid as the “Active Selection”  IE if they have 6 PTZs’ up. They hit the Left button, and it moves PTZ control to the PREVIOUS camera, and the joystick will now be able to control that camera.

Pagination
Previous page
Input devices
Next page
AXIS joystick