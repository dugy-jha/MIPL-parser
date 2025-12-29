# Mirasys VMS V9.5.1 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-5-1-release-notes

Mirasys VMS V9.5.1 release notes
Release date: 09.11.2022




Enhancements 
Nvidia decoding allows multiple display adapters 

The ability to decode using one display adapter has been extended to use all available display adapters for decoding in both the VMS server and in Spotter.   

 

Fixes 
VMS Server 

Fixed: Old camera drivers are working in the VMS server.  

Fixed: VCA service starting on the correct port on the first VMS server startup.  

Fixed: License counting in file system when multi-channel devices are used.  

Fixed: Malfunction on multi-channel device channels when some of the device channels are not used.  

Fixed: Disk mapping of automatic archiving to network disk 

 

Master server 

Fixed: User notification on settings change.  

Optimized: Alarm searching and alarm activity calculation for Spotter timeline 

Optimized: VMS server event sending to clients. 

Optimized: VMS server connection management.  

Optimized: Client application files downloading service. 

Optimized: System data loading when clients login.  

 

System Manager 

Fixed: Allows a user to uncheck the last unused channel whilst adding it.  

Fixed: Camera exports to CSV file shows correct information on cameras which configuration has changed.  

 

Spotter 

Fixed: Spotter crashing when the PTZ control is on, and the camera is opened with the automatic PTZ control opening enabled. 

Fixed: Spotter getting stuck on logging off on rare occasions. 

Fixed: Spotter crashing on rare occasions to alarm popup when connection to master is reestablished. 

Fixed: Backwards alarm search in case of lot of alarms occurring in the system. 

Fixed: Plugin elements scaling in camera grid. 

Fixed: In case of named layout is missing, Spotter will load last layout on login. 

Optimized: Alarm timeline activity calculation. 

 

Spotter Web 

Fixed: Spotter Web login being blocked when using 2-factor authentication is required in the user group settings.  

Fixed: Spotter Web number of streams limitations has been removed. 

Pagination
Previous page
Mirasys VMS V9.5.2 release notes
Next page
Mirasys VMS V9.5.0.5 release notes