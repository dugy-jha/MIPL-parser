# License Plate Recognition (LPR) settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/license-plate-recognition-lpr-settings

License Plate Recognition (LPR) settings

System Administrator settings enabling Operators to use License Plate Recognition in Spotter Smart Search, and Spotter Smart Recognition.

The Smart LPR feature requires an RTSP Server Streaming license.

License Plate Recognition Settings

License Plate Recognition Settings can be found in System Manager under the VMS Server tab > Cameras.

In the Camera settings window, go to the LPR Settings tab.

If your license does not support the Smart LPR feature, the LPR settings tab will be hidden. 

Select camera, stream, and enable LPR

Select the Camera from the drop-down menu in LPR

If there is more than one Stream, you can select the stream. If there is only one stream, there is a default stream like in the picture above, and the drop-down menu is disabled.

You can only choose a Service after you have enabled the service by clicking the box Enable LPR for selected camera.

If the Enable LPR for selected camera is not ticked, the Service drop-down menu is disabled.

The license text box shows number of used licenses and maximum number of licenses.

Detection Parameters

After the camera, its stream and the LPR detection service are selected, license plate detection settings can be adjusted. Plate detection settings can be found in the Detection Parameters group box in the LPR settings tab in the Camera Settings window.

Plate detection settings are used for configuring the plate recognition detector.

Region of interest - define the area where the detections are made.

Same plate event delay - the number of seconds that should elapse before reading the same plate twice.

Max plates - maximum number of plates to detect. Detected plates are sorted by plate confidence number in descending order.

Minimum character confidence - plate characters recognizer confidence level. Valid values are between 25% - 95%.

Minimum plate confidence - recognizer confidence level. Valid values are in the range of 25% - 95%.

Minimum plate height - minimum plate height in %. Valid values are in the range 1% - 50%. The default value is 5%.

Detection interval - the number of milliseconds that describes how often plate detection is done: if it is, for example, 250ms, then plate detection is done 4 times in a second (even if the video stream frame rate is much higher, like 30 fps).

Device - is used for inference. Available devices depend on the hardware of the actual service.

Region - The detection model (Eurasia or Americas) to be used for detection.

Minimum country confidence - country recognizer confidence level. Valid values are between 25% - 95%.

Enable country recognition - enable or disable country detection. Enabling country detection can improve plate number detection in some cases.

Include plate images - include plate images or not in returned data.

Enable images HW decoding - enable to decode input images with the most suitable computing platform (CUDA, DXVA, or DirectX).

Save settings

Click the OK button with the green checkmark icon at the bottom of the Camera Settings window.

Click the Cancel button with the red cross icon to cancel saving LPR settings and return to the settings values loaded after opening the System Manager application.

LPR settings for the selected camera are temporarily saved after switching on other cameras, streams, or tabs.

If you need to delete stream settings for the selected camera and detection stream, then select “None” in the Service name Combobx for the selected camera and detection stream.

Influence on settings

The following actions affect the service settings regardless of the actions on the LPR settings tab:

Deleting a recorder: in case of deleting a recorder, all streams are deleted in the settings of all LPR services that worked with the remote recorder and saving the LPR settings.

Deleting a camera: in case of deleting a camera, the stream is deleted in the settings of all LPR services that worked with this camera and saving LPR settings. There is a rule - one camera with one stream can only be used by one LPR service, but one LPR service can work with multiple cameras.

Changing the image size and compression type on the Streams subtab of the General tab: in case of changing the resolution or compression type for the camera and stream, which are present in the settings of any LPR service, the LPR service settings are changed and saved when the Camera Settings window is closed.

Changing the RTSP streaming settings in the Streaming Settings group of the RTSP Server Streaming tab: in case of changing the "Password,” “User Name“, "RTSP Port", "Streaming Mode" (security type) for the selected camera and stream, which are present in the settings of any LPR service, the LPR service settings are changed and saved when the Camera Settings window is closed.

Changing the image size in the Device Settings group of the Video tab in the Hardware Settings window: in case of changing the resolution for the selected camera (here is possible to change the resolution for Recording stream only), which is present in the settings of any LPR service, the LPR service settings are changed and saved when the Hardware Settings window is closed.

Changing the camera by clicking on the Edit IP camera button on the Video tab in the Hardware Settings window: in case of changing the camera by clicking on the Edit IP camera button resolution and compression type for the new camera (for Recording stream only) will be rewritten in LPR services settings, where camera ID is presented, the LPR service settings are changed and saved when the Hardware Settings window is closed.




Pagination
Previous page
Object Blurring
Next page
Face Recognition (FR) Settings