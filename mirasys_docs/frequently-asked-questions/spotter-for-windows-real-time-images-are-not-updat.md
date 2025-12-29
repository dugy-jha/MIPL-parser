# Spotter For Windows real-time images are not updated smoothly | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/spotter-for-windows-real-time-images-are-not-updat

Spotter For Windows real-time images are not updated smoothly

Check that VMS network adapters have these settings (VMS servers and clients):

Interrupt Moderation Rate is Extreme

Receive Buffers/Receive Descriptors is 2048

Transmit Buffers/Transmit Descriptors is 2048

Check that the VMS network adapter’s Link Speed is 1Gb/s.

Check that the entire link speed from the VMS server to the Spotter for Windows is 1Gb/s.

VMS remote client should NEVER be connected to 100 Mb/s Link Speed.




Pagination
Previous page
Check HDD/SSD/M.2 health
Next page
How to install CA certificate to Windows 10 store