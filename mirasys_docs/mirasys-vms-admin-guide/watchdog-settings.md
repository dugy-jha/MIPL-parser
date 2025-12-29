# Watchdog settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/watchdog-settings

Watchdog settings

In watchdog settings, you can select what events trigger a report to be sent to e-mail addresses specified in E-Mail Settings
You can select different events for each server.
Alternatively, you can select the same events for all servers by selecting All VMS Servers from the drop-down list.
In addition to e-mail notifications, notifications can be performed through digital outputs.
All event types are written to the watchdog logs, regardless of the e-mail settings.

To add or remove events on the notification list:

On the System tab, select Watchdog settings.

Mark the Send mail checkbox for each event type for which a notification e-mail should be sent.

Click OK.

Automatic restart

Tick the box Allow automatic computer restart if a critical error occurs to allow your computer to restart automatically in case of high hardware temperatures, if there is a reboot action received (alarm or text channel), in case of a recorder process restart failure or multiple reconnection failures to the recorder. The computer will not be restarted more than once a day.

You can also allow hardware monitoring if needed.

Digital output notifications

In addition to e-mail notifications, notifications can be performed through digital outputs.
Notifications through digital output are created as server-specific; you need to select a specific server from the VMS Server drop-down list.

To set a digital output notification:

On the System tab, select Watchdog settings.

Select a server from the VMS Server drop-down list. As digital output signals are server-specific, you cannot select All VMS Servers.

Click on an event.

Select the digital output channel you want to use from the In Use drop-down menu.

If you want to send a pulse signal to the output channel, mark the Pulse checkbox and select the pulse length with the slider.

Click OK.

Pagination
Previous page
Watchdog
Next page
Watchdog log