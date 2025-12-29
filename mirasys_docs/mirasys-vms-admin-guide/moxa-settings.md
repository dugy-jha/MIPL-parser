# Moxa settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/moxa-settings

Moxa settings
Enable Moxa PTZ editing

In System Manager role properties / VMS Servers settings, Moxa PTZ settings editing for user group can be selected. If Enable Moxa PTZ control is not selected, Moxa PTZ settings under camera settings can be seen but those cannot be changed.

Moxa PTZ settings

In Camera settings, an additional Moxa settings tab is available for those cameras that have configured Moxa Ptz driver settings or if Moxa editing is enabled for users user group.

Device

Enable Moxa PTZ settings for the camera

If the camera does not have PTZ settings, open the device and PTZ control tab pages with default values.

If the camera has Moxa PTZ settings and Enable is not selected, the settings saving removes Moxa PTZ settings from the camera

Address enter IP or DNS address of MOXA device.

Port index is the index of the serial port (1 - 255) in the MOXA device where the PTZ camera is connected.

Timeout/ms is the timeout in milliseconds for communications with MOXA device (5000 ms as default)

Protocol is the communication protocol with the PTZ camera from the following enumeration:

{ “PelcoD”, “BoschOSRD” }

Default value is “PelcoD“

PTZ control

Camera index - address of PTZ analog camera which is set in camera (usually it is hardware jumpers) (0 - 255)

Baud rate - serial port baud rate in bits per second. MOXA supports following set of baud rates:

{ 50, 75, 110, 134, 150, 300, 600, 1200, 2400, 4800, 6400, 7200, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600 }.

Default value is 38400 bps.

Data bits - (byte) - value from the following set:

{5, 6, 7, 8 }

Default value is 8.

Stop bit - (byte) - value from the following set:

{ 1, 2 }

Default value is 1.

Parity - value from the following enumeration:

{ “None” = 0, “Even” = 1, “Odd” = 2, “Mark” = 3, “Space” = 4 }

Default value is “None“

Flow control - value from the following enumeration:

{ “None” = 0, “RTS / CTS” = 1, “XON / XOFF” = 2, “Both” = 3 }

Default value is “None“

Pagination
Previous page
Advanced
Next page
RTSP Server Streaming