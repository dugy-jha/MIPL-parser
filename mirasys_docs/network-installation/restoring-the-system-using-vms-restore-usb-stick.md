# Restoring the system using VMS Restore - USB stick | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/restoring-the-system-using-vms-restore-usb-stick

Restoring the system using VMS Restore - USB stick

If you encounter a problem with Windows or the system disk is broken, you can use the included USB stick to reinstall Windows.

Depending on the system configuration USB stick includes:

Mirasys VMS license under Licenses -folder

Mirasys VMS software under VMS Setup -folder

Prerequisites for System Restore

Internet connection to activate Windows license

USB stick with VMS Restore media

The Windows Server restores will ask for the license key, which can be found on the server chassis sticker.

VMS Restore wizard

Boot system from the USB stick

Workstations F12

Servers F11

Select the USB stick and press Enter to continue.
Please note that it will take some time for the files to load and the restore wizard starts.
When the wizard is ready to make a restore you should see this kind of window.

Change the keyboard layout if needed.

Continue by clicking Run the Deployment Wizard to install a new Operating System. The wizard now gathers data.

If needed, change the Time settings and Time zone. Please note that VMS Restore media is only available in English.

Click Next to continue.

The disk number where to install the operating system is requested in this step:

Select M.2/SSD disk and type the desired number.

The size can depend on system configuration, but it is normally 256GB or 480GB.

Click Enter to continue.

The needed partitions are now created, and the operating system with drivers is installed.

This can take up to 60 minutes depending on system configuration. At this time the system will make multiple reboots.

If you encounter problems, please click the Powershell window, type the number and press Enter to continue.

When the restore is done, you should return to the Windows login screen. You can now log in to the system using a Windows username and password.


Now you can proceed by installing the needed software and update drivers to the latest ones from the manufacturer page.





Pagination
Previous page
System Restoration
Next page
Networking White Paper