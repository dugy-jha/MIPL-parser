# Multistreaming and TruCast for Network Optimization and Storage | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/multistreaming-and-trucast-for-network-optimizat-1

Multistreaming and TruCast for Network Optimization and Storage

Since it is also possible to use a different stream for TruCast than the recording stream, this should be considered when planning the network capacity.

For example, users can choose to view live images with TruCast at a higher framerate (for example, 25 fps) and always record at a lower framerate (for example, eight fps).

This reduces the storage and network requirements considerably.

Impact of TruCast on Image Delay

Since the TruCast stream does not travel to the VMS Server and back, the delay from the camera to the client is slightly smaller, but the difference to the stream received from the server is not large, only some milliseconds. 

The difference in the two-stream modes is complicated to observe in real life.

Features Not Supported in TruCast Streaming

TruCast does not support PTZ control or Audio

Also, currently, TruCast supports only live images. Playback (recorded images) is currently always received from the server.

Licenses

TruCast requires the VMS license to have the TruCast feature and the TruCast client driver identifiers used.

These TruCast driver licenses, and the TruCast feature, are always enabled in the Mirasys V9 product version.

Multiple Viewers

Since each TruCast-viewer opens an individual new stream from the camera to the client, users should trial how many streams can reliably be opened from the cameras they are using. In practice, 3-5 streams typically work ok.

Installing Client Drivers

Before using TruCast, the necessary client drivers need to be installed with the System Manager application if they have not been installed with the original system installation.

The client driver packages are available in the whole setup package from Mirasys. They are named with the “.sdi” filename extension.

These drivers are installed on the System Manager application’s first page, “Install client driver.”

The new drivers can be added by pressing the “Install new client driver” button and choosing the SDI packages.

After this, click the “OK” button.

After installing the drivers, they still need to be downloaded to the viewing Spotter clients. This is done when Spotter is restarted from the desktop.

After Spotter has downloaded the new drivers, the system is ready for TruCast use.

Please note that only those cameras which’ client driver was installed will appear as TruCast enabled.

Configuring multi-streaming

TruCast can use any stream from the camera, the Recording, Live viewing or Remote streams.

The multi-streaming is enabled and configured typically in System Manager – cameras.

In the Spotter client settings – streaming – multi-streaming, the user can choose which one of the streams is used for viewing. The same setting is used for standard and TruCast viewing.

TruCast Default Setting

The default setting for all cameras that have not been used for TruCast before can be defined in Spotter settings – streaming – TruCast default value.

The possible values are

Always stream from the VMS Server

Stream from the VMS Server normally, but switch to TruCast if the connection to the server is lost

Always stream using TruCast

Pagination
Previous page
Network Optimization
Next page
Using TruCast