# Troubleshooting Guide | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/troubleshooting-guide

Troubleshooting Guide
Prologue

On this guide you can find tips how to start troubleshooting VMS System.

Hardware

When you encounter problem with VMS System it's recommend to start checking that hardware is working properly.

Many manufacturer are providing own diagnostic tools which can help to solve if there is problem with hardware side

HP/HPE is shipping integrated diagnostics toolsWhen you reboot HP/HPE hardware you can access diagnostics tools when hardware is rebootingYou can access there pressing ESC or F2 keys on boot but always these are not working and key can be something elseHP/HPE is providing very good guide how to access on integrated diagnostics toolshttps://support.hp.com/us-en/document/c03467259Usually hardware problems are related to memory and hard drive, so it's good to run tests for these firstSometime fast check give answer but sometimes it's necessary run extensive test, that can take more that 1 hourIf Windows is working fine you can also install diagnostics tools there and try find problem using thosehttp://hp.com/go/techcenter/pcdiags

Dell is shipping with integrated diagnostics toolsWhen you reboot Dell hardware you can access diagnostics tools when hardware is rebootingYou can access there pressing F12 key on boot but always these are not working and key can be something elseDell servers also provide iDrac which allow you to connect over network that server hardware and run diagnosticsIf Windows is working fine you can also install diagnostics tools there and try find problem using thosehttps://www.dell.com/support/home/us/en/04/quicktest

To fix hardware issues you may need change component like hard drive, processor etc.

Sometimes fix can be found in BIOS/UEFI update or hardware example hard drive need firmware update

Network

If there is problem with network first what you need to do is check that network is working correctly

This means that check that cables are connected fine, you can use example ping command to check that connection is working and no package drops happens

It's recommend to read Network White Paper, that include critical information how system works and what are requirements

Windows

It's also very important check that Windows is working correctly

For that you need run SFC /scannow command, this command check that Windows files are fine

https://www.dell.com/support/article/us/en/04/sln32294/how-do-i-run-the-system-file-checker-in-microsoft-windows

If you are using Windows 10, you need to use DISM command to check Windows files

https://support.microsoft.com/en-us/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system

If that founds something problems with Windows files, it's recommend to check that hardware is working fine

Both these commands try to fix corrupted files but sometimes this will not work and you need reinstall whole Windows

VMS Software
SQL Server

First thing is check that system is running normallyCheck that SQL Server is working and connection is made there; VMS is shipped with SQL Server 2014 Express (needs Net Framework 3.5) and later SQL Server 2016 ExpressYou can open SQL Server and look that there is these databases created; DvmsData, RecorderDb and WdContextIf those databases are created, you can Select Top 1000 Rows and check is there any data stored

On default VMS Services are using SYSTEM account and that mean's that SYSTEM account need to have rights to write/read data to SQL Server

If SQL Server is not working check that if that is installed on system, you can check this from Control Panel or Windows Services, which shows SQLEXPRESS service
If SQL Server is not installed you can use Full installer package to do this or install it manually

If SQL Server is not running you can may find reason for that in Windows Event Viewer (https://www.howtogeek.com/school/using-windows-admin-tools-like-a-pro/) or in SQL Server logs

VMS Server

If there is any problems with VMS Software best think is start to check VMS logs

You can check logs using System Manager or check them manually

Default logs locations

32bit System 

C:\Program Files (x86)\DVMS\DVR\logs

C:\Program Files (x86)\DVMS\SystemManagement\logs

C:\Program Files (x86)\DVMS\Gateway\logs

C:\Users\%username%\AppData\Roaming\DVMS\DVR Application\Logs

64bit System

C:\Program Files\DVMS\DVR\logs

C:\Program Files\DVMS\SystemManagement\logs

C:\Program Files\DVMS\Gateway\logs

C:\Users\%username%\AppData\Roaming\DVMS\DVR Application\Logs

We can provide DvmsLogs tool to check up VMS logs. That tool provide easier view to look log files and also use colors to show error related messages. More information here.

VMS Client

If there is problem on client side log default location is

C:\Users\%username%\AppData\Roaming\DVMS\DVR Application\Logs

Those logs can tell so much what is maybe causing problems

If client can't connect to VMS Server, it's recommend first start checking that connection can made to VMS Server example use ping command to look if server can answer

If VMS Server answers ping that means that it's up and running but sometimes ping maybe is blocked so it's better to check that ports are openVMS Ports can be found hereTelnet is one way to check if port is open; telnet <IPADDRESS> <PORT>Or PowerShell command; Test-NetConnection -Port <PORTNUMBER> -ComputerName <IPADDRESS OR COMPUTERNAME>

Cameras

If system has problems to recognize camera, start checking that communication between server and camera is working

Then update camera driver to VMS Server and also camera firmware

When you have updated camera firmware, you need "refresh" camera information, that system can understand there is new firmware installed on camera which may provide new features

"Refresh" means that you open System Manager, go to Hardware section, open updated camera and search it again. When this is done you can save system settings.

If system is not showing camera stream, try change streaming protocolDefault is RTPoverUDP

Pagination
Previous page
Default usernames and passwords for Windows
Next page
How to create "dump" virtual disk for VMS Master