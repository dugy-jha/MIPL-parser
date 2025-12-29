# Failover Logs | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/failover-logs

Failover Logs
Failover log in Spotter

To see failover events in Spotter, the user role for that must be enabled in System Manager Spotter user role settings. By default, failover events are not shown in Spotter.

When failover events are received in Spotter, the log is shown in the Notifications drop-down menu. The notifications icon blinks a few seconds every time a new notification is added.

Failover event is sent only once in cases:

Recorder failure detected, but the recorder is already in the failover process.

Recorder failure detected, but no failover recorders are free in the system.

The situation cleared when the failover for the recorder was done.

Failover events

Failover events are categorized with severity. The severity of the information is shown with different icons.

Information - white info icon

Failover in progress

Failback in progress

Material copy in progress

Failover ready

Failback ready

Material copy ready

Warning - yellow warning icon

Failover failed, reason: Skipped, failover already running

Error - red error icon

Failover failed

Failback failed

Material copy failed

Errors are shown with detailed info part

Failover server in the wrong state

Incompatible

Internal error

Invalid log state

No failover serve

No failover server connection

No license

No recorder

No recorder settings

Operation canceled

The server is in the wrong state

Settings saving failed

Pagination
Previous page
Watchdog Event Search
Next page
Plugins