# How to fix SQL login error | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-fix-sql-login-error

How to fix SQL login error

In some cases, SQL may lose login information. This can see on VMS services logs and here example of that error.

ERROR Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.Edge.EdgeHandler - Select records from database error! System.Data.SqlClient.SqlException (0x80131904): Cannot open database "RecorderDB" requested by the login. The login failed. Login failed for user 'NT AUTHORITY\SYSTEM'.


On default VMS services are using SYSTEM-user for login to SQL databases.

How to fix SQL login error

Open Microsoft SQL Server Management Studio.

When VMS installation is done at first time, this is user with admin rights.

Use that user to login to Microsoft SQL Server Management Studio.

On Connect to Server window, check that you are making connection to correct server with Windows Authentication and click Connect.

Open Security and then Logins

If there is only 1 user and sa-user, this means this user which has been used for login, not have admin rights to this SQL Server. Please use other user.

If you can see more than one user, this indicate that user has correct user rights to system.

If you can’t see NT AUTHORITY\SYSTEM user, this need to be then add to under Logins.

Right click Logins and select New Login.

This open new window where you can fill needed details.

Click Search and type on this new window in the Enter the object name to select name system and click Check Names and last OK. This add SYSTEM user details to New Login window.

After this go to Server Roles and enable this user sysadmin right.

Now you can click OK.

This save user details under Logins.

Now you can restart VMS services and services will now create needed databases if there is any missing or make logins to current databases.

After this is recommend to fine tune user rights correctly.

Here examples for normal SYSTEM user rights

When all of these steps are done, you can check that logs are clean for this error and use VMS normally.

Pagination
Previous page
List Management Service update from 9.6.1 to 9.6.2 fails
Next page
Media Exporter Command Line Tool