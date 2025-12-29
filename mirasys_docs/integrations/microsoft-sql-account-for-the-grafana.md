# Microsoft SQL Account for the Grafana | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/microsoft-sql-account-for-the-grafana

Microsoft SQL Account for the Grafana
Server Authentication

Start Microsoft SQL Server Management Studio

Click Connect

Select SQL Server and right-click

Select Properties

Select SQL Server and Windows Authentication mode

Click OK

Adding new user

Select Security → Logins

Right-click top of the Logins

Select New Login

This will open a new window where you can fill in information for this new user. 

Example 

Login name: GrafanaUser

SQL Server authentication

Password: GrafanaUser

Default database: master

Enter Login name

Set SQL Server Authentication

Enter Password

Remove Enforce password policy

Click OK

Giving access to the Mirasys VMS database

After this, you need to give rights for this user that they can access VMS databases. 

Go to the User Mapping page

Map

DvmsData

RecorderDB

WdContext

Give db_datareader role for each of these databases.

When you have done this you can click OK.

Pagination
Previous page
Microsoft SQL Server Management Studio
Next page
Install Mirasys Reporting Grafana