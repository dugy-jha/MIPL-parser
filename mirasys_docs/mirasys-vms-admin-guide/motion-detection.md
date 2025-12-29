# Motion Detection | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/motion-detection

Motion Detection

Our motion detection feature allows you to define which recordings will be stored in our file system and can be used to trigger alarms.

To start using motion detection, you need to configure motion masks which will then be used to define if motion is detected on the camera or video stream.

By using the scheduler, you can decide which motion masks will be used when storing recordings in the file system.

The information received through motion detection can be used in alarm settings to trigger alarms. In the alarm trigger settings, you define which motion mask motion detection should be used as an alarm trigger.

To access motion detection configuration in the System Manager, go to VMS Server Settings > Camera Settings > Motion Detection.

Sensitivity and quantity

The system detects motion based on Sensitivy and Quantity:

Sensitivity: Pixels change more than the set limit

Quantity: The specified number of pixels change

When there is a lot of background noise in the image (for example changes in lighting conditions), you can decrease the sensitivity by dragging the slider to the left or increase the quantity limit by dragging the slider to the right.

Motion detection methods
Comparative detection 

Comparative detection compares an image to the image before it and can be used in most conditions.

If the differences exceed the set limits, the system detects motion.

When there is a lot of movement in the background, for example, rain, moving leaves, or changes in light levels, use adaptive motion detection.

Adaptive detection 

Adaptive detection compares each image to a background image.

The system automatically learns the background image and the movement does not interpret, for example, moving leaves as motion.

If more than half of the pixels in an image change, the system concludes that the lighting conditions have changed, and as a result, it resets the reference image and starts learning it again. 

Hermeneutic detection 

Hermeneutic detection is a sophisticated motion detection system for challenging weather conditions, such as heavy rain, “noisy” background images, and situations in which external video content analytics (VCA) tools are used.


Hermeneutic detection requires more processing resources than the other detection methods.

Motion detection frame rate

Motion detection frame rate detects the frame rate used in motion detection.

It is generally recommended to use the default frame rate.

For IP cameras, motion detection uses intra-frames and matches the intra-frame rate. Typically, this is one image per second.

Pagination
Previous page
RTSP Server Streaming
Next page
Motion Detection Configuration