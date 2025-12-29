# How to identify system overload and reduce load | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-identify-system-overload-and-reduce-load

How to identify system overload and reduce load

When Mirasys DVMS server seems to work slow and images are missing the system may be overloaded.

When system is overloaded there is often "Skipping frame" -prints in log files. This means that system is not able to store all the incoming data from cameras to disk.

Here is an example how it looks on log files: (C:\Program Files\DVMS\DVR\logs: xxxDVRLogxxx.x)

2016-12-28 09:32:12,753 WARN DVRServer.exe - Camera(59): Skipping frame (current time difference = 2001, limited time difference = 2000, total images skipped = 128, file Storage load 7 Mb/sec)
2016-12-28 09:32:12,893 WARN DVRServer.exe - Camera(82): Skipping frame (current time difference = 2320, limited time difference = 2000, total images skipped = 128, file Storage load 7 Mb/sec)

There might be also "Skipping images" print seen.  It indicates that server can not send all the images to client. This may happen due to bad network, server problems, client problems or some other reason.

Here is an example how it looks on log files: (C:\Program Files\DVMS\DVR\logs: xxxDVRLogxxx.x)

2016-12-28 10:40:31,503 INFO DVRServer.exe - Network send image queue to 10.91.102.10 full (1) for camera 61. Skipping images.
2016-12-28 10:40:31,534 INFO DVRServer.exe - Network send image queue to 10.91.102.10 full (1) for camera 64. Skipping images.

One symptom is also memory consumption. Memory reaches slowly 100% and the machine gets totally jammed.

When a notice such problems in Mirasys server think if there is any changes done recently. Adding cameras may cause performance issues. 

Step-by-step guide

This is how you can reduce the server load from System Manager → Camera settings 

Reduce Record rate: Try to reduce rate as low as it is acceptable (for example 8 or 6). Then see if system works better. 

Reduce Quality: Try to reduce rate as low as it is acceptable (lower default value 60% to 50% and so on..). Then see if system works better. 

Reduce Resolution: Try to reduce rate as low as it is acceptable. Then see if system works better.

Pagination
Previous page
How to configure Hikvision DS-6716HUHI-K
Next page
How to create a two-event alarm by using Logical IO