# Quick start guide for VCA | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/quick-start-guide-for-vca

Quick start guide for VCA

To help you get started quickly, we have listed essential topics below. Please execute the following steps for each server:

Decide what VCA functionality meets your requirements. For guidance or consult your Mirasys representative.

Acquire and install a Mirasys VMS system and the related software license key with other required features enabled.

Add and configure the video cameras you intend to use for VCA and enable the VCA capability in the camera settings.

Enable hermeneutic motion-detection mode for each camera used for VCA.

Export the VCA core HW GUID and obtain the VCA activation license code from Mirasys, and activate Mirasys VCA with these licenses.

Calibrate each camera in VCA settings if object classification is required.

Configure the detection zone and rules for each camera.

Configure alarms based on the VCA events if required. 

Verify VCA functionality visualisation using the Spotter for Windows application.

To get the HWGUID for the VCA license, one camera has to be enabled in the System Manager camera settings to get the VCA engine running. After the VCA is running, the VCA HWGUID can be retrieved from the VMS server license dialog in the System Manager.

The VCA engine is started in the VMS server when at least one camera is configured to use the VCA in the System Manager camera settings. The very first VCA engine start will compile the NVIDIA libraries if Deep Learning is in use. This can take a lot of time, and it depends on the hardware used. During the compilation time, the VCA is not functioning.

It is highly recommended to wait until the NVIDIA libraries are compiled after the VCA is enabled, before doing any other operations on the VMS server.

Pagination
Previous page
About Mirasys VCA
Next page
Prerequisites for Mirasys VCA