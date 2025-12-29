# Object Recognition (OR) Settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/object-recognition-or-settings

Object Recognition (OR) Settings

System Administrator settings enabling Operators to use Object Recognition in Spotter Smart Search.

Object Recognition Settings

Object Recognition Settings can be found in System Manager under the VMS Server tab > Cameras.

In the Camera settings window, go to the OR Settings tab.

If the user license does not support the Object Recognition feature, the OR settings tab will be hidden. 

Select camera, stream, and enable OR

Select the Camera from the drop-down menu in OR

If there is more than one Stream, you can select the stream. If there is only one stream, there is a default stream like in the picture above, and the drop-down menu is disabled.

You can only choose a Service after you have enabled the service by clicking the box Enable OR for selected camera.

If the Enable OR for selected camera is not ticked, the Service drop-down menu is disabled.

The license text box shows number of used licenses and maximum number of licenses.

If the camera does not support OR or there is no Service active for it, then it is not possible to enable the service at all.

The yellow icon indicates that, and if the user hovers over it, there is a tooltip with the text There’s no active OR service for this camera.

Detection Area / Minimum Object Size

An image in the Detection Area is uploaded immediately after the current camera is selected in the Camera Combobox. The minimum object size can be adjusted in two ways:

Adjust the percentage in Min. object height (%)

Adjust it in the frame with the indicated square for Minimum object size. The square will have the same color as in the selector to the right of the frame.

The minimum size cannot be less than 10%.

Detection Parameters

Max objects – maximum number of objects to detect from the image. The value should be between 1 and 100.

Minimum confidence (%) – recognizer confidence level. If confidence for the detected object is below this threshold, then the object is ignored. Valid values are between 25% - 95%.

Detection interval (ms) - the number of milliseconds that describes how often object detection is done: if it is, for example, 250ms, then object detection is done 4 times in a second (even if the video stream frame rate is much higher, like 30 fps).

Device – is used for inference. Available devices depend on the hardware of the actual service.

Include thumbnail checkbox – include detection source image thumbnail or not in returned data.

Thumbnail height (px) – the height of the thumbnail image in pixels. ONLY enabled if the Include thumbnail box is checked. The value should be between 32 and 128 pixels.

Include object images checkbox – include object images or not in returned data.

Enable images HW decoding checkbox – enable to decode input images with the most suitable computing platform (CUDA, DXVA or DirectX).

Object Data Store Settings

To select the maximum amount of events to store in the database, and for how long to retain those events, go to System Settings > Object Data Store Settings in System Manager.




Pagination
Previous page
Face Recognition (FR) Settings
Next page
VCA settings