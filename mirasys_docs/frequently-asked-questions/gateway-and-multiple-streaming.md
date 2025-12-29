# Gateway and Multiple Streaming | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/gateway-and-multiple-streaming

Gateway and Multiple Streaming

System Manager allows configuring cameras to use multiple streaming. This means that VMS can send multiple streams to different clients.
In VMS settings there are totally 3 streams that you can use in different scenarios. 1. is Recording, 2. is Live and 3. is Remote. When Gateway is installed on a server in default configuration this use Live stream.
This means that when multiple streaming is in use Gateway use the second stream for live view and when the user search recorded material, Gateway starts using the first stream.

Scenario example

The first stream is recording and this is the highest stream; 1080p 25fps
The second stream is live and this is the middle stream; 720p 15fps
The third stream is remote and this is the lowest stream; VGA 5fps
When Gateway is installed to the server and multiple streaming is in use, Gateway will use the second stream for live and when users searches recorded material, Gateway starts using the first stream.
If you want to change this live stream to the third stream which is the lowest you need to edit the Gateway configuration file.

Step-by-step guide

Default installation location for Gateway configuration file is C:\Program Files\DVMS\Gateway and file name is ServiceLauncher.exe.config

First, stop DVMSGatewayService

Then edit ServiceLauncher.exe.config using Notepad

In there is attribute VideoStreamType, which you can change

VideoStreamType

<!-- Video stream type parameter, Possible values: Rec, Live, Remote -->

<add key="VideoStreamType" value="Live" />

If you want to use a third stream for Gateway streaming you need to edit this VideoStreamType value to Remote

VideoStreamType

<!-- Video stream type parameter, Possible values: Rec, Live, Remote -->

<add key="VideoStreamType" value="Remote" />

When change is made, you need to start DVMSGatewayService

Pagination
Previous page
Lost Recorder Password?
Next page
Cannot add VMS server to system (Duplicate identifier)