# Flash Memory Backup / Restore | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/flash-memory-backup-restore

Flash Memory Backup / Restore

Mirasys VMS includes an automatic flash memory-based backup and restore functionality ("ABUR"). This feature is only available on servers delivered by Mirasys.

The flash memory backup and restore functionality is intended for situations in which the operating system and hard disk have failed the server hard disk needs to be re-formatted or replaced.

The automatic flash memory functionality can backup and restore the following:

Windows OS

Mirasys VMS software

Mirasys VMS license

Server configuration files

The automatic flash memory functionality does not include the following:

Windows OS updates made after server delivery

Any VMS software updates made after server delivery

Any driver updates made after server delivery

It is important to note that the automatic restore function restores the VMS software version that is delivered with the server. The same applies to IP camera drivers. If the server has been updated or new drivers installed, the software needs to be edited after restore, and the IP camera drivers will need to be reinstalled.

It should be noted that the first backup is done at midnight of each day (unless changes are made to the configuration during the hour before midnight, in which case backup is delayed until the next day).

Flash Memory Backup

The flash memory functionality automatically backs up the server configuration and license files at installation, and after that each time there are changes in them.

The server automatically handles all steps of the process, and there is no need for the users to do anything to enable the functionality.

Flash Memory Restore 

In case of a hard disk failure, the system administrator may need to restore the system from the automatic backup files. The process is mostly automatized, but the user needs to perform some steps.

Pagination
Previous page
Upgrading VMS version
Next page
System Restoration