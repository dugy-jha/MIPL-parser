# Creating a customer-specific user | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/creating-a-customer-specific-user-1

Creating a customer-specific user

To add a new user to the system:

Open the Users tab. 

Click the name of the user group to which you want to add the user.

Note that you can only add users to the system’s native groups, not in domain-based groups.

Click Add User in the upper-left corner of the Users tab. The Add User dialogue box is shown.

Do the following:

Type a name for the account in the Username box.

To add a password to the account, click Change password and type the password two times.

Type an optional description about the user account.

Use the pull-down menu to select the user group into which you want to assign to the user.

Select the user interface language for the user.

Set protection settings for the programs:

Hide user interface on lock

Automatic lock

Automatic log-off

Wait time: if the user does not use the program for the specified time, the program is locked, or the user is logged off.

Note: Users can change their passwords and user interface language in the Spotter program.

Identify users through a user name separate from the user login ID

To improve platform security, users can be identified through a separate user name so as not to display and compromise the user login ID. 

The System Administrator can define a public name for users in the System Manager user settings. The public user name should be unique. This is not mandatory, and the field can also be left blank.

As before, the user will use the login user name to log into any application, but if a public user name has been entered for the user, this public user name will be displayed in the client UI.

Adding a public username in the System Manager

In the System Manager Desktop Application, go to User Settings and click edit.

In the Public name field, the system admin can choose to provide a public name for a user:

This name is displayed in the System Manager’s users list:

It is displayed in the profile settings user list:

And also as logged on user:

Displaying a public user name to the user in Spotter

If there is a public user name set for a user in System Manager, the public user name is displayed together with the user identity, in switch user:

The users can also view their public user name when changing their password:

Public user name in Spotter web client

The public user name is displayed in Spotter Web in the top right corner if it has been defined in the System Manager.

If the public name has not been defined, the user’s login name is shown.

If the user's public name is changed in the System Manager, the Spotter Web user is logged out, and the user needs to log in again. After the login, a new public name is shown on the main screen. If it has been removed in the System Manager, the same process applies, and after login the user’s login name is shown.




Pagination
Previous page
Active hours - User group access schedule
Next page
User account settings