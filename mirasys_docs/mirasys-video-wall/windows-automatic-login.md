# Windows automatic login | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-video-wall/Video-Wall-Guide/windows-automatic-login

Windows automatic login

Recommended to configure AVM DS PC’s for automatic start and automatic Windows login

Autologon tool

This tool needs to be used with the account that you want to log in automatically to Windows.

Download the tool from the Microsoft site.

Log in to the desired account on Windows.

Extract this file to the desired place, for example, C:\temp

Double-click Autologon64.exe.

Accept the agreement.

Fill details

Username

Password

The domain can be left empty or filled if needed.

Click Enable.

Now you can test this autologon by restarting the machine.

Windows User Accounts

Type in the search box the command netplwiz or open Run and type the command netplwiz.

This opens a new window, which is named User Accounts.

Select using the mouse the user whom you want to log in automatically.

Then untick Users must enter a user name and password to use this computer.

After this, you get a pop-up window, where you can fill this your username and password.

Click OK to save these settings.

Now you can test this autologon by restarting the machine.

Registry change

Open registry editor(Regedit)

Browse HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Winlogon

Set AutoadminLogon to 1

Set the DefaultUserName value to the correct username

Add new String Value --> DefaultPassword

Set value for DefaultPassword

Now you can test this autologon by restarting the machine.

Pagination
Previous page
Windows configuration
Next page
Windows performance options