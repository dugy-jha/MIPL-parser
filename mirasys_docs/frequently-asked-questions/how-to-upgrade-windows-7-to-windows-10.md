# How to upgrade Windows 7 to Windows 10 | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-upgrade-windows-7-to-windows-10

How to upgrade Windows 7 to Windows 10
Checklist before upgrade

Mirasys VMS  v7 version must be newer than 7.6.4

If you need to upgrade VMS version, please use the latest version

Mirasys VMS  V8 version must be newer than 8.3.6

If you need to upgrade VMS version, please use the latest version

Capture cards are not officially supported in Windows 10

On Windows 10 you can use Windows 7 drivers

Mirasys VMS material is not lost if Windows 10 upgrade is not affecting material partitions

How to make Windows upgrade

Backup your Mirasys VMS settings using System Manager

Upgrade your VMS version if this is needed, depending on your installation version you can use a 32bit or 64bit installation package

Check that system works normally after the upgrade

When you have confirmed that everything is working, you can close VMS applications and proceed forward

Stop and disable VMS services; WDServer, DVRServer and SMServer

You can now start installing Windows 10 update on Windows 7, follow Microsoft installer instructions

Microsoft is providing Media Creation Tool which you can use to create Windows 10 installation images or installation media

You may need to buy Windows 10 license

When the upgrade is done, you can enable and change VMS services to Automatic startup; WDServer, DVRServer and SMServer

Check after this that VMS is working correctly and you can access stored material

Pagination
Previous page
Create memory dump using ProcDump
Next page
Default usernames and passwords for Windows