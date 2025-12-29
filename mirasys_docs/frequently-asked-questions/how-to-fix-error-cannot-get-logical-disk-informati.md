# How to fix error "Cannot get logical disk information" | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-fix-error-cannot-get-logical-disk-informati

How to fix error "Cannot get logical disk information"

If System Manager can't recognize server disks then problem can be Windows WMI polling method.

In DVRlog you should see this kind of error

ERROR DVRServer.exe - Cannot get logical disk informationSystem.Management.ManagementException: Invalid class
at System.Management.ManagementException.ThrowWithExtendedInfo(ManagementStatus errorCode)
at System.Management.ManagementObjectCollection.ManagementObjectEnumerator.MoveNext()
at Mirasys.Servers.Recorder.DVRServices.Monitoring.MonitoringService.GetDriveInformation()

Step-by-step guide

Create a system restore point (Steps: https://support.microsoft.com/en-us/help/17127/windows-back-up-restore)

From the command prompt with administrative rights or elevated privileges change directory to C:\Windows\System32\Wbem and run the following command: mofcomp.exe CimWin32.mo

For re-registering associated .dll if one exists use following command: regsvr32 CIMWin32.dll

Restart the Windows Management Instrumentation Service

Start System Manager and check if you can see disks

If this is not helping do also these steps

Go to start-run and type in wmimgmt.msc

Right click on Local Wmi Control (Local)and select properties

Click on the Security tab and expand Root folder. You can now see cimv2.

Create a system restore point (Steps: https://support.microsoft.com/en-us/help/17127/windows-back-up-restore)

Execute the console application if there is no error, exit.

From the command prompt with administrative rights or elevated privileges, execute the following steps and execute the following this: net stop winmgmt

Open a Windows Explorer and locate the path to C:\windows\system32\WBEM\ folder and rename the Repository folder to something else like RepositoryOLD (right click and choose 'Rename Folder').

Restart the computer

From the command prompt with administrative rights or elevated privileges, execute the following steps and execute the following this: net stop winmgmt

From the command prompt with administrative rights or elevated privileges, execute the following steps and execute the following this: winmgmt /resetRepository

Restart the computer

Pagination
Previous page
How to run HP Diagnostics
Next page
How to enable Windows Services recovery