# Face Recognition (FR) Settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/face-recognition-fr-settings

Face Recognition (FR) Settings

System Administrator settings enabling Operators to use Face Recognition in Spotter Smart Search, and Spotter Smart Recognition.

The feature requires an RTSP Server Streaming license.

Face Recognition Settings

Face Recognition Settings can be found in System Manager under the VMS Server tab > Cameras.

In the Camera settings window, go to the FR Settings tab.

If your license does not support the Smart FR feature, the FR settings tab will be hidden. 

Select camera, stream, and enable FR

Select the Camera from the drop-down menu in FR

If there is more than one Stream, you can select the stream. If there is only one stream, there is a default stream like in the picture above, and the drop-down menu is disabled.

You can only choose a Service after you have enabled the service by clicking the box Enable FR for selected camera.

If the Enable OR for selected camera is not ticked, the Service drop-down menu is disabled.

The license text box shows number of used licenses and maximum number of licenses.

Face detection settings

After the camera, its stream, and the FR detection service are selected, face detection settings can be adjusted.

Detection Parameters

Face detection settings are used for configuring the face recognition detector.

Region of interest - define the area where the detections are made.

Max faces – maximum number of faces to detect from the image. The value should be between 1 and 5.

Minimum confidence – recognizer confidence level. If confidence for the detected face is below this threshold, then the face is ignored. Valid values are between 25% - 95%.

Minimum face height – minimum face height in %. Valid values are from 5 to 50%%. Default value 10%.

Minimum face similarity – If the similarity is greater than or equal to this value, then it is the same face. The value should be between 50% and 95%.

Same face event delay – the number of seconds that should elapse before arising an event with the same face.

Device – is used for inference. Available devices depend on the hardware of the actual service.

Thumbnail height – the height of the thumbnail image in pixels. The value should be between 32 and 128 pixels.

Include thumbnail – include detection source image thumbnail or not in returned data.

Include face images – include face images or not in returned data.

Enable images HW decoding – enable to decode input images with the most suitable computing platform (CUDA, DXVA or DirectX).

Save settings

Click the OK button with the green checkmark icon at the bottom of the Camera Settings window to save.

Click the Cancel button with the red cross icon to cancel saving FR settings and return to settings values loaded after opening the System Manager application.

When deleting stream settings for the selected camera and detection stream, the “None” value should be selected in the Service name Combobox for the selected camera and detection stream.

Influence on settings

The following actions affect the service settings regardless of the actions on the FR settings tab:

Deleting a recorder: in case of deleting a recorder, all streams are deleted in the settings of all FR services that worked with the remote recorder and saving the FR settings.

Deleting a camera: in case of deleting a camera, the stream is deleted in the settings of all FR services that worked with this camera and saving FR settings. There is a rule - one camera with one stream can only be used by one FR service, but one FR service can work with multiple cameras.

Changing the image size and compression type on the Streams subtab of the General tab: in case of changing the resolution or compression type for the camera and stream, which are present in the settings of any FR service, the FR service settings are changed, and saved when the Camera Settings window is closed.

Changing the RTSP streaming settings in the Streaming Settings group of the RTSP Server Streaming tab: in case of changing the "Password,” “User Name“, "RTSP Port", "Streaming Mode" (security type) for the selected camera and stream, which are present in the settings of any FR service, the FR service settings are changed and saved when the Camera Settings window is closed.

Changing the image size in the Device Settings group of the Video tab in the Hardware Settings window: in case of changing the resolution for the selected camera (here is possible to change the resolution for Recording stream only), which is present in the settings of any FR service, the FR service settings are changed and saved when the Hardware Settings window is closed.

Changing the camera by clicking on the Edit IP camera button on the Video tab in the Hardware Settings window: in case of changing the camera by clicking on the Edit IP camera button resolution and compression type for the new camera (for Recording stream only) will be rewritten in FR services settings, where camera ID is presented, the FR service settings are changed and saved when the Hardware Settings window is closed.

Pagination
Previous page
License Plate Recognition (LPR) settings
Next page
Object Recognition (OR) Settings