# ArchiveCapture installation and usage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/archivecapture-installation-and-usage

ArchiveCapture installation and usage

The path for the archive is set to the address field (auto search window).

The Driver configuration is done through ArchiveCapture.xml:

Loop functionality

Original (captured) frames time

Frame rate (configurable or default)

Time limits for capture from the saved archive

Enable/disable video channels

The "channels" and "limit" sections can be disabled at all (attribute enabled="0")

Without ArchiveCapture.xml default values will be used.

XML file settings are applied only during the archive search process.

PAUSE, CONTINUE and NEXT_FRAME are implemented over CIPVideoCapture::SetExtendedProperty(const char* const aProperty, void* aValue, unsigned long aChannelId) where:
aProperty- command, can be "PAUSE", "CONTINUE" and "NEXT_FRAME"
aValue- for future needs, should be NULL
aChannelId- channel id

Pagination
Previous page
Driver Istallation and Usage
Next page
CanonIPCapture installation and usage