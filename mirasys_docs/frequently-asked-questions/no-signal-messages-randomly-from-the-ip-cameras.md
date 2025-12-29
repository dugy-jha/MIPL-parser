# “No signal” messages appear randomly from the IP cameras | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/no-signal-messages-randomly-from-the-ip-cameras

“No signal” messages appear randomly from the IP cameras

In cases where “No signal” messages appear randomly from the IP cameras, please go through the following checklist:

Has the latest firmware been installed on the camera?

Has the latest camera driver been installed on the VMS?

Check that VMS network adapters have these settings:

Interrupt Moderation Rate: Extreme

Receive Buffers/Receive Descriptors: 2048

Transmit Buffers/Transmit Descriptors: 2048

Check that the VMS network adapter’s Link Speed is 1Gb/s. 

Check that the entire link speed from the cameras to the VMS is 1Gb/s.

VMS should NEVER be connected to 100 Mb/s Link Speed.

Pagination
Previous page
IP camera is found, but there is “No signal” from the camera
Next page
How to edit camera driver configuration file