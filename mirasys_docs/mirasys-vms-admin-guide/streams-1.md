# Streams | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/streams-1

Streams

By default, Mirasys VMS receives recording quality stream from the camera.
Mirasys VMS server send recording stream by default to the Mirasys Spotter.

Codec

The codec is used for transmitting the video between the server and the client applications, and in the case of IP cameras, for transmitting the video between the IP camera and the server.
In the case of analogue cameras, the codec used by the system is JPEG.
In IP cameras, any codec supported by both the camera and the server software can be selected.
The codecs supported by the server software are JPEG, MPEG-4, H.264, H.265 and Mobotix MxPEG.

Bitrate mode. 

This setting controls if the Variable bit rate (VBRMax) or Constant bit rate (CBR) is used. 

Quality

Set this value between 0%-100%. A higher value means better image quality but also a large image data size.
To decrease the image data size, set the value lower. However, setting the value lower also decreases the quality of the images.
50% is usually sufficient. For wireless and low bandwidth connections, select 0%.

Resolution

For automatically configured IP cameras, the exact image resolutions supported by the camera model are displayed.

Record rate

The record rate defines how many frames the camera sends to the VMS and how many frames are recorded.
The maximum rate depends on the video standard and the camera type.
Multiple streaming (multi-streaming)

Pagination
Previous page
General settings
Next page
Multi-Streaming