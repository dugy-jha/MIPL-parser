# Installing External Driver Packages | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/installing-external-driver-packages-1

Installing External Driver Packages

To use IP cameras, digital I/O devices or text data in the VMS system, the driver for each device must be installed on the server. The software includes all drivers and plugins that have been included in the previous versions of the software.

Install a new Driver

New Drivers and Plugins can be installed manually.

Driver installation packages

To install a new driver, you need a device-specific driver installation package. The package is a compressed (zipped) folder containing the driver files.

When installing a driver installation package, the system compares the files in the installation package to the existing files on the servers. It installs the files only if they do not exist on the servers or if the files in the installation package are newer than those on the servers.

You can also force the system to install any driver version if necessary.

If you want to update an already existing camera driver:

Remove the camera from the system before updating the driver.

After removing the camera, install the driver file.

Then reinstall the camera.

After installing a new driver, you need to configure the devices that use the driver. 

How to install a Driver package

On the System tab, under Add-ins, open Install driver. 

Select the drive where the driver package is located, find and select the driver package (.zip file). The Install Driver dialogue box is shown.




3. Select the servers on which you want to install the driver.

4. If you want to force the system to install the driver package version, select Install the driver even if the same or a newer version exists.

5. Click Install. The Status column shows the text Installed if the driver is successfully installed. If the driver is not installed, the column shows an error message.

6. Click Close to exit the dialogue box.

If you need to update drivers for hardware other than IP cameras, please contact the system supplier.

A 32-bit system requires a 32-bit driver package, and a 64-bit system required a 64-bit driver package.







Pagination
Previous page
Mirasys Camera Drivers
Next page
Driver Istallation and Usage