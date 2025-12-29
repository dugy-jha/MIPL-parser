# Device Compatibility Tool | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/device-compatibility-tool

Device Compatibility Tool

You can find this tool in our Extranet. This tool offer easy way to test if device or devices (example IP-camera, encoder etc.) are working with Mirasys VMS and our camera driver or drivers. This tool provide different levels of testing and give results based on tests.

Test requirements

Device Compability Tool from Extranet

Device is not connected to any VMS

Camera motion test

To test this, you need configure motion mask on camera side

Camera edge test

To test this, you need install SD-card to camera and check that camera is recording material to SD-card

Camera audio test

To test this, you need loopback audio channels on camera physically

How to use
Initial configuration and driver update

The DCT doesn’t have installer, so user can just unpack ZIP archive with the application and run it. In the application folder you can find the “Drivers“ folder which contains driver archives. The tool automatically unpack the drivers to application folder after launching, so if you need to use another version of the driver or add/remove some driver, then you need to close application, add/remove driver package to the “Drivers“ folder and start application again.

Only 64 bit drivers are supported.

Main Window

After launching the main application window is displayed.

Device compatibility tool - Main window

It has 3 areas:

The device tree

Working area with test scenarios and manual test controls

Status bar with log messages and the “Full log“ button

Add/remove devices

To add new devices user needs to click to the “Add device“ button in device tree and the following dialog will be displayed.

Device compatibility tool - Add device manually

User can add device manually with selecting the driver, specify device network address, port, user name and password. Or user can add all devices from local recorder.

Device compatibility tool - Add recorder devices

After selection and pressing the “OK” button selected devices will be added one by one to the tree. During the adding process device capabilities will be quired.

To remove device need to select it in the tree and click to the “Remove“ button.

Device capabilities

All added devices have capabilities. To display them user needs to select device and go to the “Device Capabilities“ tab.

Device compatibility tool - Capabilities
Testing process

To run tests for devices user needs to select them with check-boxes in device tree (he can select particular devices or all of them with clicking to the “Devices“ check-box). Then in the “Compatibility testing“ tab user needs to configure tests: select which tests will be active and configure test iteration duration in seconds.

Device compatibility tool - Test scenarios

The test scenarios view has 2 areas: general tests which are active by default and additional tests which can be activated by user if required.

When devices and tests are selected and configured user needs to click to the “Start compatibility testing“ button to run testing process. Test scenarios will be running one by one and results are displayed in the following view.

When test scenario is done user will see the test status (OK or Failed) and button with the “Folder“ icon - if user will click to this button the test results folder will be opened for the particular test.

Device compatibility tool - Test result folder

It contains detailed log for the test (the “TestReport.txt“ file) and additional files depends on test type. For example, for video tests there will be recorded video files.

In addition for video tests user can click to the thumbnail image and video player will be opened with result video.

Device compatibility tool - Test result video

User can start/pause playback and rewind to the beginning of the video file.

If some features are not supported by device the test scenarios will be completed with “Unsupported“ result.

Application logging

In the tool user can see the application log in 2 areas:

Latest log message in the status bar

Full log starts from application running when click to the “Open full application log“ button

Device compatibility tool - Full log

In addition the log is writing to the “logs“ folder in the application folder.

Supported IP Camera List

If test is done by Mirasys personel in Mirasys office with direct access to device, then this device is added to Supported IP Camera list.

If manufacturer, distributor or integrator wants to get camera to our Supported IP Camera list or get report of this camera, please contact Sales to discuss more.

Pagination
Previous page
How to debug VCA Metadata
Next page
VMS Performance Counters