# Automatic Backup feature | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/automatic-backup-feature

Automatic Backup feature

Mirasys VMS has two automatic backup features

Automatic Backup to HDD

Automatic Backup to USB

Automatic Backup to HDD

V9 Enterprise product line include Automatic Backup to HDD feature. This feature make automatic backup to local HDD every night at 2 am if there has been any changes on system side.

Default location for this is

C:\Program Files\DVMS\SystemManagement\SMData\RecoveryStore\Backups


If you want to example change backup location or other options you can edit autobackup.xml file which is located in C:\Program Files\DVMS\SystemManagement -folder.

Example of autobackup.xml file

XML
<?xml version="1.0" encoding="utf-8"?>
<BackupConfiguration>
  <!-- Use automatic backup or not yes / no-->
  <Dobackup> yes </Dobackup>
  <!-- Start time for automatic backup, local time -->
  <Starttime> 2:00 </Starttime>
  <!-- Maximumm number of saved backup files -->
  <Maxfiles> 50 </Maxfiles>
  <!-- Backup path (if not defaults) -->
  <Path></Path>
</BackupConfiguration>


If you make changes on that file, you need restart SMServer to accept new changes.

Default VMS Services are using SYSTEM account. Please note that this user not example can’t detect mapped network drives or USB sticks.

Automatic Backup to USB

This feature is extra feature and this need to be add license before you can use this feature. If both features are added to license, then system use only Automatic Backup to USB feature.

Automatic Backup to USB feature detect if there is USB stick on system and that stick is named as VMS Restore. On that stick there need to be Backups folder on root. If that is not created VMS will not make any backups until that folder is created.

If you want to change when backup is made, you need to edit autobackup.xml file.

Automatic Backup testing

If you want to test automatic backup, you need to change start time and add Delay tag to autobackup.xml file.

Example of autobackup.xml file

XML
<?xml version="1.0" encoding="utf-8"?>
<BackupConfiguration>
  <!-- Use automatic backup or not yes / no-->
  <Dobackup> yes </Dobackup>
  <!-- Start time for automatic backup, local time -->
  <Starttime> 2:00 </Starttime>
  <!-- Maximumm number of saved backup files -->
  <Maxfiles> 50 </Maxfiles>
  <!-- Delay tag -->
  <Delay> 5 </Delay>
  <!-- Backup path (if not defaults) -->
  <Path></Path>
</BackupConfiguration>


Delay time defines after how many minutes backup is checked. Delay tag is not a default value.

When you want to use own settings, you need to remove Delay tag from XML file.

Pagination
Previous page
How to change programs DEBUG level
Next page
Audio channels found -popup window