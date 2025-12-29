# Audit trail log | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/audit-trail-log

Audit trail log

The Audit trail log can be used to search VMS system user activity information. It can be accessed in System Manager at the System tab tree under Monitoring.

Audit trail log

In the audit trail log dialog admin can search for audit trail events using several search parameters. Results are listed in the result list ordered by time. Found audit trail events can be sorted by other audit trail event information by clicking the list headers.

Search parameters

Following search parameters can be used for audit trail event searching.

Date - Select the date for the search to start. Buttons on the left and right decrease or increase the day of the date.

Time - Select the time of the date for the search to start. Buttons on the left and right decrease or increase the hour of the time. Buttons up and down increase or decreases minutes of the time by ten.

User - User whose audit trail events will be searched. All = search without filtering users.

Application - Application to search. All = search without filtering applications.

Max result count - Maximum number for how many audit trail events will be searched starting from start time.

VMS Server - The VMS Server drop-down shows all possible values for VMS Servers that can be selected.

End time check box - If checked, it enables search end date and time selection similar way as for start time. If not checked, end time is not used as a search filter (= search until now)

Audit trail events - Operation to search: none, one, many, or all operations can select. If none or all is selected, then search without filtering operations. The following buttons can be used with operations:

Enlarge operation list view

Select all

Unselect all

Results list

Found audit trail events are listed in the search result list. The list contains information about each audit trail event.

Time - Time of the user action.

User - Username who did the user action.

Application - Application where the user action was taken.

Event - Name of the user action. When the even is related to camera audit, and the operator needs to add a comment before accessing playback material, the event contains the comment.

Event status - If the operation was successful or not.

Object - The object depends on the operation itself. For example, if you open a camera, the name of that camera is shown.

VMS Server - Displays on which VMS server the operation occurred.

Audit log export

Listed audit trail events can be exported to a PDF file as an audit trail report by clicking the button under the audit trail events results list. The location and the name of the exported file and the comment for the report can be given on the save report dialog. The audit trail log report title is created of the export time and the user who exported the report. The report contains all the audit log entries with the same information that is listed in the audit trail event result list.




Pagination
Previous page
Monitoring
Next page
SM Server Diagnostics