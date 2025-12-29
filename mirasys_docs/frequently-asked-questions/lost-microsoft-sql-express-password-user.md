# Lost Microsoft SQL Express password/user | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/lost-microsoft-sql-express-password-user

Lost Microsoft SQL Express password/user

On default, Mirasys VMS Complete package installs VMS with Microsoft SQL Express.
The installer adds this Windows user who is installing VMS to SQL SuperAdmin user.
If you have lost this user or password, here are some tips on restoring access to SQL Express.

Enable Mixed Mode Authentication for SQL Server

There are different ways to enable Mixed Mode Authentication

Way 1

Enable SQL Server Mixed Mode Authentication by changing instance properties

Open Microsoft SQL Server Management Studio

Click Properties on SQL Server

Go to Security

Change Server authentication mode to SQL Server and Windows Authentication mode

After this, you get a notification that you need to restart SQL Server to change these settings active

This can be done on Windows Services

Way 2
Enable Mixed Mode Authentication in Registry Editor

Open Registry Editor

Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL12.SQLEXPRESS\MSSQLServer

MSSQL12.SQLEXPRESS depends on what is your installed version

Change the value of LoginMode from 1 to 2

Close Registry Editor

Restart SQL Server to change these settings active

This can be done on Windows Services

Recover a lost SuperAdmin (SA) password

To start recovering SuperAdmin (SA) password, there is need to change how SQL Server authenticate users

Stop all Mirasys VMS servicers

WDServer

DVRServer

SMServer

Open SQL Server Configurator Manager

Select SQL Server Services

Open with right-click SQL Server Properties

Add under Startup Parameters parameter -m

Apply settings and click the OK button for the warning message window

Restart SQL Server service

Open Command Prompt as Administrator mode

Type there command SQLCMD -S localhost

This open console to SQL Server

First, you need to enable a user with the command

ALTER LOGIN sa enable
GO


Then you need to create a new user with sysadmin user rights

CREATE LOGIN NewSA WITH PASSWORD = 'Password@1234';
ALTER SERVER ROLE sysadmin ADD MEMBER NewSA
GO


If you want to use a Windows account to log in, you can add this using these commands

CREATE LOGIN [ComputerName\username] FROM WINDOWS
GO
ALTER SERVER ROLE sysadmin ADD MEMBER [ComputerName\username]
GO


When changes are done, remove SQL Server startup parameter and restart SQL Server

After these changes, you can log in to SQL Server using SQL Server Management Studio with NewSA user or Windows user to SQL Server and change the SuperAdmin (SA) user password and remove unnecessary users from SQL Server.

Sources
4 Ways to Enable Mixed Mode Authentication for SQL Server (isunshare.com)
Recover a lost SA password (sqlshack.com)

Pagination
Previous page
How to change VMS Service to Automatic (Delayed Start)
Next page
How to run Command Prompt as SYSTEM user