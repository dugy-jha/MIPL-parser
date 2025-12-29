# Export logs | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/export-logs

Export logs

Export log files and send them to the system supplier should there be a problem with the system.

Log files are saved to a compressed (zipped) file that can be placed to a removable or non-removable device.

Export log files via System Manager

Open the System Manager application for export logs and choose the Export logs subitem in the Backup tree item on the System tab.

Select logs that can be exported in the

Select Logs window.

If there are problems with a server select logs on the System Server logs panel. In addition, select client program logs.

The client logs are from the machine where you are accessing the system manager application.

For fast selection, you can use the Select All and Clear Selections buttons placed under the System Server logs and VMS server logs panels. Select or clear all selections for specific service groups (e.g. License Plate Recognition service) that contain specific services by clicking on the services group checkbox.

3. Click OK. 

4. Select the storage device and the folder where you want to save the log files in the Destination Directory window.

To create a new folder, click the New folder button.

Type a name for the ZIP file in the Name fields and click OK

You can see the progress of exporting in the Export Progress window. Operations are executed in order from top to bottom.

It is seems like the operation is stuck it can be cancelled.

Cancel all export by clicking on the Cancel button at the bottom of the window.




5. Click OK to close the window once the export is completed.




6. The system exports the files to a ZIP file. Send the ZIP file to the system supplier. Services log files are stored in inner ZIP archives in the main ZIP file.

The typical content of logs ZIP archive is the following:

Some service sub-archives can be missed if there are no connections to services.




Export log files via System Monitor

It is possible to collect system logs via the System Monitor application.

Open System Monitor and click the

Log export button:

2. Choose the archive name and path for saving in the Save as dialog to save the export archive.

3. Click Ok to start collecting logs.

The System Monitor can collect SM server logs (also ones include Incident Reporting log, Storage Locker log, and Export services log), DVRs logs, clients' logs (Spotter, System Manager, etc.), and logs of all List management, Face Recognition, and License Plate Recognition services observed in the current system.

The typical content of logs ZIP archive is the same as for ZIP archive from System Manager. Some service sub-archives can be missed if there are no connections to services.

Pagination
Previous page
Backup
Next page
Back up settings