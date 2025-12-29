# ThruCast | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/thrucast

ThruCast

ThruCast is a proprietary direct video streaming feature found in Mirasys VMS 7.3 that streams camera video directly to a Spotter client in case of a recording VMS server disconnect or for the purpose of network optimization.
If ThruCast is to be used, the VMS network needs to be planned with this in mind.
Normally it is recommended to isolate the camera network physically or logically, routing traffic from IP cameras directly to DVRServer.

With ThruCast, the cameras need to be able to be routed to Spotter clients in the event of connection difficulties with DVRServer.

Normally the camera’s video feed is routed to the server’s camera network card, while it is accessed by a Spotter client through the server’s client/server network card.

In the event of a network disconnect or other failure relating to the server, the spotter takes direct streaming from the camera.
Direct streaming can also be accessed by changing connection settings. This option can be considered when optimizing the network.

Supported Cameras

ThruCast requires a separate camera capture driver for the client.

Currently, drivers exist for the following camera manufacturers:

ACTi

Axis

Bosch

Hikvision

Samsung

Sony

Stanley

LILIN

An ONVIF ThruCast driver is also available for cameras that are not on the supported list.
The use of the ONVIF driver requires that the camera is added to the VMS system with the ONVIF driver, not the camera’s native driver.

Network Optimization

ThruCast is useful in reducing network load in certain instances.
Usually, this is performed when the recording server is on another site and the Spotter client is on the same site as the cameras.

Example 1

Site 1 contains the recording VMS server and Site 2 contains the other elements of the system, including the cameras and a Spotter for Windows client.
In the initial state, camera feeds are sent to the server and from there to the Spotter. Traffic between the sites is increased because of this, with the server streaming the feed to the Spotter.

With ThruCast, the camera sends a direct feed to the Spotter and a recording stream to the VMS server.
Traffic from the camera is increased, but the inter-site traffic load is lessened.
A user operating the Spotter can determine the framerate of the ThruCast stream coming directly to the Spotter client.
The frame rates between the ThruCast stream and the recording stream can be different. A user can determine whether or not they want to directly stream any specific camera through the Spotter client.

Example 2

The two sites both have cameras as well as Spotter viewing clients. Site 2 user uses ThruCast with on-site cameras. This service can be chosen for all cameras in the system or only on-site cameras.

For the Site 1 user, ThruCast only reduces traffic between the server and the network connection.

ThruCast allows users to have control over which cameras are using the service. The setting is saved for each user and camera, and Spotter layouts remember these settings.

Impact Of Multistreaming And ThruCast On Network Optimization And Storage

Network planning is required when ThruCast is expected to be used.
The service creates two streams from a camera using the service: a recording stream to the recording server and a live stream to a viewing Spotter client.
ThruCast streams can be set for different frame rates, as well. A live viewer might set the recording stream to a lower frame rate (e.g. 8FPS) and have the live stream at a higher frame rate (e.g. 25FPS).
This reduces storage and network requirements to the recording server significantly.

Other Considerations
Impact Of ThruCast To Image Delay

The delay of the video stream might be less than in a case where the stream is relayed through a recording server.
But this difference is not significant enough for a human to notice, as it’s only some milliseconds.

Features Not Supported In ThruCast Streaming

ThruCast does not support PTZ (Pan, Tilt, Zoom) camera control or two-way audio transmissions.
The ThruCast only supports one-way streams from the camera.
Currently, the service doesn’t support replaying recorded images either, as these are always received from the recording server.

Licenses

ThruCast requires the VMS license to have the “ThruCast” feature and the ThruCast client driver identifiers that are being used.
These ThruCast driver licenses, and the ThruCast feature, are always enabled in the Mirasys Enterprise product version.

Multiple Viewers

Each individual viewer on ThruCast constitutes an individual video stream from the camera, so users seeking to adopt the service should conduct trials to establish the maximum number of reliable streams from the cameras used.
Cameras can usually support three to five streams.

Pagination
Previous page
Solution Examples
Next page
Troubleshooting Network Issues