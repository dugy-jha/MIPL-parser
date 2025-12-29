# Logs messages and what those means | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/logs-messages-and-what-those-means

Logs messages and what those means
Message types

INFO

This is a normal info-type message that tells how the system is running.

WARN

This message type indicates that there have been some issues, but those are not critical.

ERROR

This message type indicates that there are some problems related to this error, and those should be fixed.

A useful tool for logs is the DvmsLogs tool.

VMS Server
DVRLog (Digital Video Recorder)

Default logs path
C:\Program Files\DVMS\DVR\logs

Log messages
INFO  DVRServer.exe - Network send image queue to xxx.xxx.xxx.xxx full (1) for camera 8. Skipping images.


This info message indicates that the Spotter client is requesting more images than the network card can send out and skipping some images. The problem can be related to network card settings on the recorder and Spotter client side.

Check that you are using an Intel network card with at least 1GB of connection, and these settings are configured on the network card.

The interruption mode is Extreme

Send and Receive buffers are 2048




INFO  DVRServer.exe - Sending playback image to  failed.


This info message indicates that DVRServer can’t send live images to the Spotter client.




WARN  DVRServer.exe - mirasys::CBaseAudioRTSPChannel::SdpInfoReceived: The audio stream is not available via RTSP for Dahua DH-IPC-HDBW2441R-ZAS (xxx.xxx.xxx.xxx:80). Probably it should be enabled manually via Web-interface


This warning message indicates that the recorder can’t get an audio stream from the camera, and it should be enabled manually via the web interface.




WARN  Mirasys.FileStorage.MaterialFile - Read index for path\dvrfile000XXXXX.dat failed! ChunksCount 32, SavedChunksCount 32
System.IO.InvalidDataException: The 'MaterialFileIndexRecordEnd' deserialization failed!
   at Mirasys.FileStorage.MaterialFileIndexRecord.Deserialize(Stream aStream)
   at Mirasys.FileStorage.MaterialFileIndexChunk.Deserialize(Stream aStream)
   at Mirasys.FileStorage.MaterialFileIndex.Deserialize(Stream aStream, Int32 aChunkCount, Int32 aSectorSize)
   at Mirasys.FileStorage.MaterialFile.ReadIndex(FileIndexSegment aSegment)


This warning message indicates that the file wasn’t closed correctly during writing. This causes deserializing to fail. This warning is possibly coming when the recorder has crashed or the connection has been lost in the middle of writing. The filesystem will automatically “repair” this file when there is new data that overwrites old data.




WARN  DVRServer.exe - Camera(116): Skipping frame (current time difference = 3989, limited time difference = 2000, total images skipped = 3, file Storage load 14 MB/sec)


This warning message indicates that storage can’t handle all frames that are coming into the VMS system. On the default system, skip all frames older than 2 seconds.




WARN DVRServer.exe - mirasys::CBaseThread::JoinThread: Thread (id=1234, name="HikvisionEventMonitoring") for device 192.168.1.234:80 was not stopped during 5000 milliseconds


This warning message indicates the HikvisionEventMonitoring thread stop takes more than 5 seconds (usually, if the network camera connection is poor or broken).

This thread is trying to receive HTTP messages from the "AlertStream" URI (it receives IO states, video-loss events, LPR events, and motion detection events). It starts when the driver is opened and stops when the driver is closed.




ERROR DVRServer.exe - mirasys::CBaseAudioRTSPChannel::SetDeviceState: Audio signal was lost for camera xxx.xxx.xxx.xxx


This error message indicates that the recorder has lost connection to the camera audio signal stream. If audio is not necessary to use, please remove these via the System Manager → Hardware → Audio tab.




ERROR DVRServer.exe - mirasys::CBaseCameraChannel::SetCameraState: Signal was lost for Dahua IPC-PDBW5831-B360-E4-2712 (xxx.xxx.xxx.xxx:80 / channel 2) (Rec)


This error message indicates that the recorder has lost connection to the camera recording stream. This can be a result of a poor connection or problems on the camera side.




ERROR DVRServer.exe - mirasys::CDahuaVideoSettingsManager::GetBitrateRangeBySettings: Unable to receive bitrate range from  Dahua IPC-HFW2541T-ZAS-27135 (xxx.xxx.xxx.xxx:80)


This error message indicates that the recorder can’t get details from the camera. This can be a result of a poor connection or problems on the camera side.




ERROR Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.Metadata.MetadataDatabase - Create metadata database failed, error message: CREATE DATABASE permission denied in database 'master'.
ERROR Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.Metadata.MetadataDatabase - Create metadata tables failed
System.Data.SqlClient.SqlException (0x80131904): Database 'RecorderDB' does not exist. Make sure that the name is entered correctly.


This error message indicates that DVRServer can’t make a connection to SQL Server to create the desired databases or SQL Server is not running on this machine.




ERROR Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.FileSystemV1.Channels.ChannelV1 - ReadNext: search next frame failed - client='ed2f9097-f14a-4046-a9dc-0165ffe37d0f', ch='type=Video ch=40', params='DateTime: 01.01.0001 12:00:00.000 SearchDirection: Forward Intra: True'


This error message indicates that the Filesystem can’t read data. Probably because this data writing was interrupted in the middle of writing (e.g., during a recorder crash). This is not a critical error; the Filesystem will erase this on the next file retention.




ERROR Mirasys.FileStorage.LoadBalancer - Unable to open journal 'path\dvrfile000XXXXX.jrn'!
System.IO.IOException: The process cannot access the file 'path\dvrfile000XXXXX.jrn' because it is being used by another process.
   at System.IO.__Error.WinIOError(Int32 errorCode, String maybeFullPath)
   at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32 rights, Boolean useRights, FileShare share, Int32 bufferSize, FileOptions options, SECURITY_ATTRIBUTES secAttrs, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access, FileShare share, Int32 bufferSize, FileOptions options)
   at Mirasys.FileStorage.Journal.Open()


This error message indicates that the journal file is reserved third party, and DVRServer can’t access this file. Please check possible third-party programs that may access the same files.




ERROR Mirasys.FileStorage.LoadBalancer - Unable to save journal record 'path\dvrfile000XXXXX.jrn'!
System.NullReferenceException: Object reference not set to an instance of an object.
   at Mirasys.FileStorage.Journal.Save(Byte[] aMaterialFilePath, Int64 aMaterialFileOffset, Byte[] aData, Int32 aDataOffset, Int32 aDataLength)


This error message indicates that DVRServer can’t open/save journal information to the file. Please check that DVRServer has access to this storage location and check if any third-party programs do not reserve these files.




ERROR DVRServer.exe - FS writing queue for ch=25 (type -1231031248) error: Frame time less then queue time!


This error message indicates that there is a time difference between DVRServer and storage. Filestorage tries to write a frame with the current time, but that has already been written earlier. In this case, Filestorage only skips the frame.




ERROR DVRServer.exe - mirasys::COnvifEdgeStorageTask: Signal was lost during processing of recorded interval (RecordingToken='23434253453453453', TrackToken='v2342-12', DataFrom='2024/01/10 10:44:45.754') for Camera manufacturer (Camera IP)


This error message indicates that the DVRServer lost connection to the camera when that was fetching data from the camera's SD card.




ERROR Mirasys.FileStorage.ArchivingTask - Read frame error, status: Failed. File: MaterialPath\dvrfile00032435.dat


This error message indicates that DVRServer recording has stopped suddenly for this dat file. That has caused there to be corrupted frames inside that dat-file. File storage will repair this dat file when the data inside dat file is overwritten with new material.




ERROR Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.Edge.EdgeHandler - Select records from database error! System.Data.SqlClient.SqlException (0x80131904): Cannot open database "RecorderDB" requested by the login. The login failed. Login failed for user 'NT AUTHORITY\SYSTEM'.


This error message indicates that the DVRServer can’t log in to the SQL database. That can happen if there has been happened error on the Windows side, and that is dropped out login details or if there has been happened hardware side crash has occurred. To fix this, you need to use Microsoft SQL Server Management Studio and fix the login details.




ERROR Mirasys.FileStorage.PrerecCopyTask - Prerec copy error, read frame error! Channel type=Video ch=4


This error message indicates that DVRServer can't read frames from a prerecording channel, which points out that at least one frame is not written correctly.




ERROR DVRServer.exe - ArchivalFileSystem: Write data error! Error: The network path was not found.


This error message indicates that DVRServer can’t find the network path to store archive data. In this case, check that network storage is working normally and there are no issues on the network side.




INFO  DVRServer.exe - Starting manual archival run.
ERROR DVRServer.exe - Could not create archive directory (\\192.168.1.100\ArchiveStorage\Archive_20240101080000\).
INFO  Mirasys.Servers.Recorder.DVRServices.DvrCoreManager.FileSystemV1.FileSystemWrapper - Export failed, error 6


This error message indicates that DVRServer can’t create a directory in the network path. In this case, check that network storage is working normally, there are no issues on the network side, and the account has write/read permissions.

SMLog (System Management Server)

Default logs path
C:\Program Files\DVMS\SystemManagement\logs

Log messages
WARN  SMServer.exe - SMRemotingHost: Remoting channel HostResourcesReleased received from HOST (URL: gtcp://127.0.0.1:5009 URI: <none> LocalNo: 92 RemoteNo: -1), Exception Genuine channels operation exception: The connection has been forcibly closed.


This warning message indicates that the SMServer has lost connection to the recorder. This can be the result of a poor network connection, or the DVRServer is not running.




WARN  SMServer.exe - Forcing a client ( xxx.xxx.xxx.xxx:62185 ) disconnected.
WARN  SMServer.exe - Failed to send event Mirasys.Common.Daos.DVREvent.SMEvents.ClientDroppedEvent


This warning message indicates that the SMServer can’t communicate with the client and timeout connection, which causes the Spotter client to be disconnected and dropped out from the system.




WARN  LicenseContainer.ValidateLicense [SMServer] - License protection not ok. Protection code(s) doesn't match: New license has codes MAC:ABCDEFG  and system doesn't have any MAC addresses


This warning message indicates that the SMServer can’t find the license MAC address from the system. Check that all network cards are operational.




ERROR SMServer.exe - Unexpected connection exception for (127.0.0.1:5009 638260581766102255) occured: 
Genuine channels operation exception: Can not connect to the remote host "gtcp://127.0.0.1:5009". System error message: The connection cannot be established because the target machine does not allow it 127.0.0.1:5009.


This error message indicates that the SMServer has lost connection to the recorder. This can be the result of a poor network connection, or the DVRServer is not running.

WDLog (WatchDog)

Default logs path
C:\Program Files\DVMS\DVR\logs

Log messages
WARN  WDServer.exe - Capture: dahuaipcapture (audio input), Audio: Channel_14, status: NO SIGNAL, action: No action needed


This warning message indicates that there is no audio stream from the audio channel.




WARN  WDServer.exe - Capture: dahuaipcapture, Video: Channel_2, status: NO SIGNAL, action: No action needed


This warning message indicates that there is no video stream from the camera.




ERROR WDServer.exe - WD: GetDvrStatus failed: No connection


This error message indicates that WDServer can’t make a connection to DVRServer to check this service. This can be the result of a poor network connection, or the DVRserver is not running. If WDServer can’t make a connection to DVRServer, WDServer tries to start this service or restart it.

Spotter (Client application)

Default logs path
C:\Users\%username%\AppData\Roaming\DVMS\DVR Application\Logs

Log messages
INFO  CameraActivitySearch.SearchGraphicalPreviousHandler [Recorder 127.0.0.1] - Graphical search previous failed


This warning message indicates that Spotter can’t make a connection to the recorder and can’t fetch material to the timeline.




WARN  ViewContainer.IsFrontBufferAvailableChanged [WindowMain] - Direct3D front buffer lost, video rendering will be slower than usual


This warning message indicates that internal or external GPU memory is full and image drawing is slower.




WARN  ViewContainer.GetImageParameters [WindowMain] - GetImageParameters, camera is not valid (not included in current profile?). Camera name: Camera 7


This warning message indicates that there is a camera open in Spotter, which is not part of the current selected profile.




WARN  LayoutLocationHelper.Parse [149] - Screen settings have changed, layout settings: 0,-1080,3840,2160, current settings: -1920,0,3840,1194
WARN  LayoutLocationHelper.Parse [149] - Monitor count has changed, cannot set window positions. Monitor count in layout: 3, current monitor count: 2


This warning message indicates that Spotter has opened the layout, which is stored for 3 monitors, but the current setup has only 2 monitors.




WARN  RealtimeStreamVideoContext.ProcessImage [TaskPoolThread11] - No image data from ConvertImage(). Camera: Camera 20, image format: 1129727305


This warning message indicates that Spotter has not received enough data to draw the image.




ERROR ControlDeviceDriverHandler.LoadInstalledDriver [SMServer] - Exception in reading parameter information from installed control device driver: ControlDeviceAxis


This error message indicates that Spotter can’t register the Axis Control Device driver. To fix this, you need to run Spotter using Administrator rights.




ERROR CameraRealtime.OpenNormalStream [Recorder 127.0.0.1] - Open failed: No connection
ERROR RealtimeStreamVideoContext.OnRealtimeStream_StreamOpen [Recorder 127.0.0.1] - Stream open exception, camera: Camera 8, message: Stream open failed: No connection


This error message indicates that Spotter can’t open the camera real-time stream from the VMS Server.




ERROR PluginInstanceCameraPrivacy.RefreshLastImage [WindowMain] - RefreshLastImage: camera not found for stream id: f5cf561b-3cc1-4b51-9b08-3e8150b86c80_070777e2-f271-421d-b3ae-7f1a6c01eae3


This error message indicates that there is a camera open in Spotter, but that is removed from the system or profile.




ERROR ApplicationLogger.ErrorSuppress [WindowMain] - Resize
SlimDX.Direct3D9.Direct3D9Exception: DXGI_ERROR_DEVICE_REMOVED: Hardware device removed. (-2005270523)
ERROR ApplicationLogger.ErrorSuppress [WindowMain] - DrawAllVideo no back surface


This error message indicates that the monitor has been removed from the PC, or Spotter can’t find the display device on Windows.




ERROR ThruCastHandler.UnpackDrivers [UserSession thread] - Failed to unpack plug-in XXXXXXCaptureDriver.sdi
System.IO.IOException: Access to the path 'C:\Users\%username%\AppData\Roaming\DVMS\spotter\9.6.1\systemfolder_5008\DriverStore\_temp_\' was denied.
   em System.IO.Directory.InternalMove(String sourceDirName, String destDirName, Boolean checkHost)
   em Mirasys.Clients.SharedCode.CommunicationLayer.Recorder.Component.ThruCastHandler.UnpackDrivers(String aStorePath)


This error message indicates that the Spotter client can’t unpack the Spotter plugin to the desired location. This indicates that folder user rights are not set correctly.




ERROR ApplicationLogger.ErrorSuppress [TaskPoolThread11] - Realtime camera 112 (server name or ip-address) ImageConvert failed to convert from format HEVC to YUY2, image utc time: 18:24:22 25/10/2023, image size: 134298
System.InvalidOperationException: Decompression failed: Opening compression driver failed. Driver error description: NvidiaDecoder::InitializeContext: cuCtxCreate() failed, error code: 2 = CUDA_ERROR_OUT_OF_MEMORY
   em Mirasys.Clients.SharedCode.PluginsLayer.ImageConversion.HandleError(Int32 aErrorCode, Int32 aHandle, Int32 aSourceSize)
   em Mirasys.Clients.SharedCode.PluginsLayer.ImageConversion.ImageConvertWithExtraData(Int32 aHandle, Int32 aSourceX, Int32 aSourceY, Int32 aSourceSize, UInt32 aSourceFormat, ArraySegment`1 aSourceImage, Int32 aDestinationX, Int32 aDestinationY, UInt32 aDestinationFormat, ArraySegment`1 aDestinationImage, Int32 doImageFunctions, Int32 aIs4CIF, Byte[] aExtraData, Int64 aTicks)
   em Mirasys.Clients.SharedCode.ApplicationServicesAPI.Streams.ImageHandler.DoConvertImage(Int32 aHandle, IBufferVideo aBuffer, Int32 aDestinationWidth, Int32 aDestinationHeight, ImageFormat aDestinationFormat, Boolean aImageFunctionsOn)


This error message indicates that the GPU memory is full and can’t process images from the camera.




ERROR RTSPClient.SendCommand [RTSP Client Thread (xxx.xxx.xxx.xxx:554)] - Unable to send RTSP TEARDOWN command to xxx.xxx.xxx.xxx:554 device): Unable to read transport connection data: A connection was forced to be canceled existing by the remote host.


This error message indicates that the Spotter client can’t send a stream closing command to the IP camera.




ERROR CameraRealtime.OpenNormalStream [Recorder server name or IP-address] - Open failed: No connection
ERROR RealtimeStreamVideoContext.OnRealtimeStream_StreamOpen [Recorder server name or IP-address] - Stream open exception, camera: Camera 85, message: Stream open failed: No connection


This error message indicates that the Spotter client can’t open the camera stream from the server.




ERROR CameraRealtime.ResetStateHandler [Recorder server name or IP-address] - Reset failed, message: DVR is performing critical task and services are temporarily out of service.


This error message indicates that DVRServer is running tasks and the Spotter client can’t request until DVRServer is free again.




ERROR RegistrationOperations.LoginHandler [SMServer] - Login failed Session id: 0
Mirasys.Common.Exceptions.UnauthorizedUserException: Given user not found for Name: Mirasys Spotter Enterprise, Version: 9.6.1, Log in time: 10/25/2023 5:48:11 PM, Type: , Network address: xxx.xxx.xxx.xxx, Session ID: 1837364178, GUID: , Policy: UserManagement = False UserQuery = False AutoUpdate = False DVRControl = False DVRMonitoring = False DVRSettings = False ---> System.ArgumentException: No such user: mirasys


This error message indicates that someone has tried logging Spotter client using an account that is not on the system.

Other services
AdvLmService (List Management Service)

Default logs path
C:\Program Files\DVMS\AdvLmService\logs

ERROR Mirasys.Lms.Services.EventService - Connect to EQ 127.0.0.1:5672 error!
RabbitMQ.Client.Exceptions.BrokerUnreachableException: None of the specified endpoints were reachable
 ---> System.AggregateException: One or more errors occurred. (Connection failed)
 ---> RabbitMQ.Client.Exceptions.ConnectFailureException: Connection failed
 ---> System.Net.Sockets.SocketException (10061): No connection could be made because the target machine actively refused it.


This error message indicates that the List Management Service can’t make a connection to Rabbit. This can be fixed by uninstalling List Management Service and RabbitMQ from the server and reinstalling List Management Service.

Export Service

Default logs path
C:\Program Files\DVMS\Export\logs

ADVExportService.exe - Failed to get public key!
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:8082
   at System.Net.Sockets.Socket.InternalEndConnect(IAsyncResult asyncResult)
   at System.Net.Sockets.Socket.EndConnect(IAsyncResult asyncResult)
   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)
   --- End of inner exception stack trace ---
   at System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)
   at System.Net.Http.HttpClientHandler.GetResponseCallback(IAsyncResult ar)
   --- End of inner exception stack trace ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   at Mirasys.SharedCode.HttpAccessBase.ServiceBase.<GetData>d__24`1.MoveNext()


This warning message indicates that the SMServer is not yet running, and the service can’t register there. This can be fixed by waiting for the SMServer to be running or checking that the SMServer is not crashed and allowing connections.

Incident Reporting

Default logs path
C:\Program Files\DVMS\IncidentReporting\logs

WARN  ADVIncidentReporting.exe - Failed to get public key!
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:8082
   at System.Net.Sockets.Socket.InternalEndConnect(IAsyncResult asyncResult)
   at System.Net.Sockets.Socket.EndConnect(IAsyncResult asyncResult)
   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)
   --- End of inner exception stack trace ---
   at System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)
   at System.Net.Http.HttpClientHandler.GetResponseCallback(IAsyncResult ar)
   --- End of inner exception stack trace ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   at Mirasys.SharedCode.HttpAccessBase.ServiceBase.<GetData>d__24`1.MoveNext()


This warning message indicates that the SMServer is not yet running, and the service can’t register there. This can be fixed by waiting for the SMServer to be running, or checking that the SMServer is not crashed and allowing connections.

Storage Locker

Default logs path
C:\Program Files\DVMS\StorageLocker\logs

WARN  ADVStorageLocker.exe - Failed to get public key!
System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:8082
   at System.Net.Sockets.Socket.InternalEndConnect(IAsyncResult asyncResult)
   at System.Net.Sockets.Socket.EndConnect(IAsyncResult asyncResult)
   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)
   --- End of inner exception stack trace ---
   at System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)
   at System.Net.Http.HttpClientHandler.GetResponseCallback(IAsyncResult ar)
   --- End of inner exception stack trace ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   at Mirasys.SharedCode.HttpAccessBase.ServiceBase.<GetData>d__24`1.MoveNext()


This warning message indicates that the SMServer is not yet running, and the service can’t register there. This can be fixed by waiting for the SMServer to be running, or checking that the SMServer is not crashed, and allowing connections.

Pagination
Previous page
DvmsLogs tool
Next page
Default username and password for System Manager and Spotter