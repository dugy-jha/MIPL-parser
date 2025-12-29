# Server Diagnostics | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/server-diagnostics

Server Diagnostics

VMS Server diagnostics shows information about the server and the CPU and network usage.

Diagnostics

The Diagnostics tab shows this information:

Information about the server:

Software version

Model

Number of cameras, audio channels, digital inputs, digital outputs, and video outputs

The name of the computer and the time zone

Operating system information

Processor information

Installed drivers, for example, capture drivers, video output drivers, digital output drivers, and PTZ drivers.

Log Files

The Log files tab shows a list of log files. 

To see the contents of a log file:

Select the file from the drop-down list. The contents are shown in the Contents of the selected log file.

Performance

On the Performance tab, you can monitor these:

CPU usage.

Usage of physical memory.

Usage of virtual memory.

Network traffic.

Used disk space.

Storage

On the Storage tab, you can monitor disk and file properties. For example, you can examine free disk space or monitor saved data by the camera and audio channel.

GeneralTotal recording capacity. Shows the total storage capacity that is reserved for the recordings.

Used space. The quantity of space that the recordings have used.
Free space. Free space is available for recordings.
% used. The percentage of the disk’s capacity that is used.
Average saving speed. Calculated by dividing the quantity of data saved since the server was last started by the uptime.
VMS Server uptime. Shows the time that the server has been operating since it was last started.
The counter shows the difference between the current time and the start time in days, hours and minutes.
DisksTotal recording capacity. Shows the storage capacity that is reserved for the recordings on the selected disk.
Used space. Used recording space on the selected disk.
Free space. Free space is available for recordings on the selected disk.
% used. The percentage of space used of the total capacity reserved for the recordings.
Total recording cache. Shows the total capacity of the cache that is used for the temporary storage of data before it is permanently written on a disk.
Because of the cache, video and audio can be recorded immediately when the server is started. The cache is also used for pre-event recording.
The system automatically calculates how much cache space it must have and allocates space accordingly.
Used recording cache. Temporary space that is currently in use.
Free recording cache. Temporary space that is currently free.
CamerasOldest time. The date and time of the oldest image in the store.
Newest time. The date and time of the newest image in the store.
Total no. of images. The total number of images in the store.
Average image size. The average image size.
Used space. This value shows how much space the images and metadata files from this camera use.
% used. This value shows what percentage of space this camera has used of the total capacity reserved for the recordings.
Audio channelsOldest time. The date and time of the oldest audio sample in store.
Newest time. The date and time of the newest sample in store.
A total number of samples. The total number of audio samples in store.
Average sample size. The average audio sample size.
Used space. This value shows how much space the audio samples and metadata files from the audio channel use.
% used. This value shows what percentage of space the audio channel has used of the total capacity reserved for the recordings.
Text channelsOldest time. The date and time of the oldest text data sample in store.
Newest time. The date and time of the newest sample in store.
A total number of samples. The total number of text data samples in store.
Average sample size. The average text data sample size.
Used space. This value shows how much space the text data samples and metadata files from the text channel use.
% used. This value shows what percentage of space the text channel has used of the total capacity reserved for the recordings.

Pagination
Previous page
SM Server Diagnostics
Next page
Licenses