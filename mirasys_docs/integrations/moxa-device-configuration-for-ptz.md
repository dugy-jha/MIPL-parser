# Moxa device configuration for PTZ | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/moxa-device-configuration-for-ptz

Moxa device configuration for PTZ
Configuration

In the section, you can find instructions on how to configure the Moxa NPort device and Moxa PTZ driver in System Manager to work with the analog PTZ camera.

Moxa NPort device configuration

To configure the Moxa NPort device user needs to login to the device web page using the name and password.

Then in device settings need to configure the ports:

In the “Serial Settings“ → “Port <number>“ need to configure serial settings - the most important is to set interface type (2-wire or 4-wire - depending on how the PTZ camera is connected to Moxa device). Other serial port settings can be set by default because the Moxa PTZ driver will write its own settings when it connects to the port:

Moxa device - Serial port settings

In the “Operating Settings“ → “Port <number>“ need to configure port operation mode - to work with the Moxa PTZ driver need to set “TCP Server“ mode for all ports. Other operating settings can be set by default:

Moxa device - Operating port settings

When the driver is connected to the Moxa device user can monitor the connection state on the “Monitor“ → “Line“ page:

Moxa device - Line Monitoring

The driver will apply its own serial port settings to the ports when it is connected. Users can check real serial port settings in the “Monitor“ → “Async-Settings“ page:

Moxa device - Port settings monitoring

When the Moxa device is configured and PTZ cameras are connected to its ports by wires, then the user can go to driver configuration in System Manager.

Please note

The 'AUTO/MANUAL' feature is incompatible with the Pelco D command set when used with this camera model. It functions only with HTTP commands

Pagination
Previous page
Magos Radar
Next page
Paxton Net2 Access Control System Proxy