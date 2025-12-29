# User Roles | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/user-roles

User Roles

The system supports the following types of user roles (defined through user groups)

System Manager role: Administrators are allowed to log in to System Manager and change all settings, such as changing camera settings or adding new profiles or user accounts.

Monitoring role: Users with monitoring rights are allowed to log in to System Manager and monitor the system on the System tab, but they are not allowed to change the settings.

Gateway role: if this role is active, the user group can access the DVMS gateway 

Mirasys Spotter Enterprise role: End users can log in to Spotter but not to System Manager.

Spotter Web role: End users can log in to the Spotter Web

User group level automatic lock / log off
Possibility to force other user log off when starting System Manager

Enabled only if System Manager Enterprise Plus role is enabled

Possible values for Wait time: 0s, 10s, 20s, 30s, 45s, 1 min

When creating new group, default value is 10 seconds

Functionality at log on

There is changes from previous versions only if other user log off is enabled and there is other user logged in System Manager with administrator rights.

When trying to log on, following choices will appear:


Kick off current user: start sequence to kick off current user with administrator rights in System Manager

Login with limited system monitoring rights: continue login with monitoring rights, no effect to current System Manager users

Cancel login: go back to start login page (cancel button has this same effect)

Kick off current user

Current user is selected, new processing window is opened:

This processing window is open until:

Other user is logged off

Other user has cancelled force log off

Cancel button is pressed

Other user is logged off

User is automatically logged in with administrator rights.

Other user has cancelled force log off

Other user has cancelled force log off

After OK button, go back to login page, other user with administrator rights continue logged in.

Cancel button is pressed

Go back to login page, other user with administrator rights continue logged in.

Other (already logged with Administrator rights) side

If there is timeout in forced log off settings, warning of coming forced log off appears:

Remaining seconds before forced log off is updated. During this timeout, user can cancel forced log off by cancel button.

If timeout is past or Ok button is pressed, current user session is logged off.




Pagination
Previous page
User group
Next page
System Manager Enterprise role