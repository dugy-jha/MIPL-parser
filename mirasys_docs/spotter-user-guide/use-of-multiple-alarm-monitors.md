# Use of Multiple Alarm Monitors | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/use-of-multiple-alarm-monitors

Use of Multiple Alarm Monitors

With the same Alarm popup settings as above, it is possible to configure the system to use multiple alarm monitors so that only a single alarm (or multiple if desired) is shown on each monitor. The system can be configured, for example, to have four separate alarm monitors. Then alarm monitor number 1 will show the oldest alarm, monitor 2 will show the second oldest alarm, and 3 will show the third oldest alarm. Monitor 4 can, for example, be configured to show the rest of the alarms.

The configuration is done by defining which alarm the Alarm popup should show. For configuring alarm monitor 1, the first active alarm should be selected in the filtering.

For the second and third, a new alarm popup should be opened and then the filtering adjusted accordingly. For the 4th and additional alarms, the setting should be changed like this:

With these four-alarm popup windows open and configured, the layout should now be saved. When there are no active alarms, the alarm monitors display a clarification number to know which monitor. When there is only one alarm active, it is displayed on the first monitor.

If two alarms are active, the oldest is displayed on the first monitor, and the newer alarm opens on the second monitor.

The third alarm is on the third monitor.

When the oldest alarm ends, it will be closed from the first monitor (1).The monitors will automatically refresh so that the alarm previously in monitor 2 is now in monitor 1, and so on.

If the alarm settings have been defined so that alarm components are kept open longer than the alarm duration, the move of alarms will happen only when the alarm components are closed.

In this case, the alarm colour in monitor one will change from the active alarm colour to the ended alarm colour.The alarm popup filter setting is saved to layouts and saved tabs.When using AVM, it is recommended to create a camera tab, open the alarm popup to the camera tab, configure the filter, and then save it with the appropriate name.The tab can then be opened to AVM using the AVM Operator Console.

It is also possible to configure the multiple alarm monitors to show the Alarm popup and Profile map side by side by configuring the Profile map to use similar filtering settings as the alarm popup.




Pagination
Previous page
Showing the Alarm Name in Alarm Popup View
Next page
Daylight Savings Time (DST)