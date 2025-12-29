# Storage Locker Settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/storage-locker-settings

Storage Locker Settings

Storage Locker Settings contains the following values:

File path:

Defines the location of the Storage Locker file storage that can be either local or network disk. As the default location, Storage Locker file storage is located in the master server's local disk.

Changing the file path

Please note that old storage locker data is not copied to the new location

Select if a local drive or network drive is used.




2. If the local drive is selected, click Set file path for data storage. Select a new location and click OK.

3. If a network drive is selected, click Set network file path for data storage. Specify network path, username, and password and click OK.

When a network drive is used for Storage Locker data storage, it is possible to allow Spotter applications directly to access saved data from the network disk by checking the option Allow applications to access directly to stored data.

Import file path:

If someone has exports that are needed to be added to the Storage locker, those exports should be placed in a folder that is defined in Storage locker settings as "Import file path". How to use:

Each import data need to be in its own folder, files that will be placed into the import folder directly will be ignored

Each import folder can have several subfolders

Images and clips can be placed in one folder, Storage locker will import them one by one

SEF archives should be in their own folder and not mixed with other data (like images, clips, etc.)

Import data should be copied all at once if something should be added - it should be copied with its own folder, files added to existing folders are not supported (those files will not be processed)




The retention time for data

The retention time for data sets defines how long Storage Locker retains data, which are not used in any Incident Report

The retention  time for data used in the incident reports

The retention time for data used in incident reports defines how long Storage Locker retains data, which are used in any Incident Report

Pagination
Previous page
Changing the order of the values
Next page
List Management settings