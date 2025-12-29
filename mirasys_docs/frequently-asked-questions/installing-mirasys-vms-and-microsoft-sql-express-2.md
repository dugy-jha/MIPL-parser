# Installing Mirasys VMS and Microsoft SQL Express 2019 separately | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/installing-mirasys-vms-and-microsoft-sql-express-2

Installing Mirasys VMS and Microsoft SQL Express 2019 separately

In some cases, there is a need to install Mirasys VMS and Microsoft SQL Express 2019 separately.

First, download the latest Microsoft SQL Server Express 2019 installer from the Microsoft site.





Open the Microsoft download tool and click the Download Media button.





Select the Express Advanced installation package in the next window and download the location.





When the download is ready, you can proceed to the installation:

Double-click the installation media and wait for the installer to extract files.

When this is done, you should see a new window where the option is to “New SQL Server stand-alone installation or add features to an existing installation”.





This opens a new window for you to accept the license agreement.

Accept and click Next.





Wait for the installation wizard to go to the next window.

At this installation time, check if there is a need to reboot the machine, install updates, etc.

A warning related to the Windows firewall can appear. This indicates that if you want to allow incoming connections from outside, you need to open ports.
In normal cases, this is not needed.

Click Next to proceed.





On the next window, disable Machine Learning Services and Language Extensions.

Now, you can also change installation locations if this is needed.

Click Next to proceed.





By default, Mirasys VMS is looking for SQLEXPRESS from the local server.

If there is no need to change it, keep it default and click Next to proceed.

If you need to use an external or different name, then use this guide to configure Mirasys VMS connection strings.





You can keep your default settings and click Next to proceed.





On this window, you must add the current user and the NT AUTHORITY\SYSTEM user. If there is a need to add other users who can access the SQL Express server, they can be added now or later on using Microsoft SQL Management Studio.

Mirasys VMS uses SYSTEM users to create databases. If this is not added, then the VMS cannot make the needed databases.

Enable Mixed mode as well. This allows you to log in with sa-user with a password and also with Windows authentication.

Click Next to proceed.





After this installation, start installing the Microsoft SQL Express server. Please wait, this can take a few minutes.

When the installation is done, you can close the window by clicking the Close button.





If any other windows are open, you can close them now.

To manage the SQL Server, you must install Microsoft SQL Management Studio separately. 

To install Mirasys VMS, you need to use the update package. This does not include Microsoft SQL Express Server installation. Future updates are also done with the Mirasys VMS Update package. 

If you use the Mirasys VMS Complete package, this forces the installation of the Microsoft SQL Express Server version, which is included in the installation package.

Pagination
Previous page
Mirasys VMS Tips and Tricks
Next page
Upgrade Microsoft SQL Server Express 2014 to 2019