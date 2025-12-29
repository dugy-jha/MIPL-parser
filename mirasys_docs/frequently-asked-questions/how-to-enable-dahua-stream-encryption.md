# How to enable Dahua stream encryption | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-enable-dahua-stream-encryption

How to enable Dahua stream encryption

To enable Dahua stream encryption, and before adding a camera to DVMS, stream encryption should be enabled in the camera web UI:

Go to device settings

Select "System." 

Go to the "Security" or "Safety" subgroup (the name may differ for different devices).

In the settings dialogue, select the System Service tab

Enable the Audio and Video Transmission Encryption checkbox.

Then, when you add a camera with supported and enabled encryption to DVMS, the driver automatically detects this stream and will add "AES-256 Encrypted" transport to System Manager -> Camera Settings -> Transport Options. An encrypted stream will be used by default transport.

Pagination
Previous page
How to edit camera driver configuration file
Next page
ONVIF IP capture XML