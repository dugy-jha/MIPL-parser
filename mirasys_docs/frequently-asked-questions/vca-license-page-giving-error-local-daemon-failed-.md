# VCA license page giving error "Local daemon failed to start" | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/vca-license-page-giving-error-local-daemon-failed-

VCA license page giving error "Local daemon failed to start"

Some cases it’s possible that VCA license daemon start configuration is corrupted.

Then this is giving error in VCA license side “Local daemon failed to start: <unspecified file>(1): expected <

To fix this error go to C:\ProgramData\VCA-Core -location and delete wiz.bit file. After this restart DVRServer Service via Windows Services.




Pagination
Previous page
Cannot add VMS server to system (Duplicate identifier)
Next page
How to debug VCA Metadata