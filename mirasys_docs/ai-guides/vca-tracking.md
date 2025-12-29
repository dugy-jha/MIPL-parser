# VCA Tracking | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/vca-tracking

VCA Tracking
Initialization

When a tracker is selected by the user, an initialization phase will be required. This will vary based on the selected tracker.

Object Tracker: when selected the tracker will need to 'learn the scene' to determine background from moving foreground objects.

Whilst learning the scene the following message will be displayed in the live view, and no objects will be tracked during this time.

DL People Tracker & DL Object Tracker: when first selected, the DL engine will run a model generation process. This optimizes the DL models to run on the available GPU hardware.

Irrespective of which tracker is selected, the DL People tracker model, DL Object Tracker model and the DL Filter model will all be optimized in one go.

This process can take up to 10 minutes per model and may increase with different GPU configurations. Once complete the optimized models are stored in the configuration folder.

The process will not need to be run again unless the GPU hardware is changed. Whilst optimization is performed a message will be displayed in the live view, and no objects will be tracked during this time.

Please note: The DL Filter requires the same initialization process but does not display a message.

Once initialized, VCAserver will begin analyzing the video stream with the selected tracker. Settings specific to that tracker will also be displayed below the tracker engine selection option.

Regardless of the tracker selected, any tracked object can be passed through the available rules. However, in some cases, certain rules or algorithms will only be available with a specific tracker.
For example, Deep Learning Filter and the abandoned and removed object rules are only available with the Object Tracker.

Object Tracker

The Object Tracker is a motion based detection engine. Based on changes detected in the image, the algorithm separates the image into foreground and background, tracking any foreground object that is moving above a set threshold. The Object Tracker has the following settings:

Stationary Object Hold-on Time

The Stationary Object Hold-on Time defines the amount of time an object will be tracked by the engine once it becomes stationary.
Since objects which become stationary must be "merged" into the scene after some finite time, the tracking engine will forget about objects that have become stationary after the Stationary Object Hold-on Time.

The default setting is 60 seconds.

Abandoned / Removed Object Threshold

This threshold amount of time an object must be classed as abandoned or removed before an Abandoned / Removed rule will trigger.

The default setting is 5 seconds.

Minimum Tracked Object Size

The Minimum Tracked Object Size defines the size of the smallest object that will be considered for tracking.

For most applications, the default setting of 10 is recommended. In some situations, where extra sensitivity is required, the value can be manually specified.
While lower values allow the engine to track smaller objects, it may increase the susceptibility to false detections.

Object Tracker Sensitivity

The Object Tracker Sensitivity value allows the object tracker to be tuned to ignore movement below a certain threshold.
Combined with the Blob Map burnt in annotation, which visualizes the area of the scene the object tracker is detecting movement, this value can be adjusted to filter out environmental noise.

The default setting is 4.

Scene Change Detection (Object Tracker)

Learn more about Scene Change Detection.

Detection Point of Tracked Objects

For every tracked object, a point is used to determine the object's position, and evaluate whether it intersects a zone and triggers a rule. This point is called the detection point.
There are 3 modes that define the detection point relative to the object:

Automatic

In automatic mode, the detection point is automatically set based on how the channel is configured.
It selects 'Centroid' if the camera is calibrated overhead, or 'Mid-bottom' if the camera is calibrated side-on or not calibrated.

Centroid

In this mode, the detection point is forced to be the centroid of the object.

Mid-bottom

In this mode, the detection point is forced to be the middle of the bottom edge of the tracked object.
Normally this is the ground contact point of the object (where the object intersects the ground plane).

Tamper Detection (Object Tracker)

Learn more about Tamper Detection.

Loss Of Signal Emit Interval

See Loss Of Signal Emit Interval

Deep Learning People Tracker

The Deep Learning People tracker is designed to track people in situations where the camera field of view is relatively close.
The Deep Learning People Tracker is based on Pose Estimation technology, providing the location of a person in the field of view as well as additional key point metadata on the parts of the body.
See Deep Learning Requirements for hardware requirements for this algorithm.

The Deep Learning People Tracker has the following settings:

Tamper Detection (DLPT)

Learn more about Tamper Detection.

Loss Of Signal Emit Interval

See Loss Of Signal Emit Interval

Enabling DL People Tracker

Open View Channels

Select the camera

Open Tracking

Open Tracking Engine dropdown box and select DL People Tracker

Deep Learning Object Tracker

The Deep Learning Object Tracker is designed for accurate detection and tracking of people, vehicles and key objects in challenging environments where motion based tracking methods would struggle.
The list of objects detected by the Deep Learning Object Tracker is given below:

Use table header to sort columns

Class Name

	

Description




person

	

A person, or tracked object with a person present (e.g bicycle)




motorcycle

	

A motorcycle




bicycle

	

A bicycle




cyclist

	

Person riding a bicycle, can be reported as two separate objects




bus

	

A bus




car

	

A car




van

	

A van, including mini-vans and mini-buses




truck

	

A truck, including lorries and commercial work vehicles,




forklift

	

A forklift truck




bag

	

A backpack or holdall (sports bag)







	




The Deep Learning Object Tracker is based on a classification and detection model, providing the location of an object in the field of view. See Deep Learning Requirements for hardware requirements for this algorithm.

The Deep Learning Object Tracker has the following settings:

Stationary Object Filtering

See Stationary Hold On Time

In addition to the Stationary Hold On Time, an additional setting Require Initial Movement, is available which will prevent objects which have not moved from being tracked.

Detection Point of Tracked Objects

See Detection Point of Tracked Objects

Tamper Detection (DLOT)

Learn more about Tamper Detection.

Loss Of Signal Emit Interval

See Loss Of Signal Emit Interval

Pagination
Previous page
VCA Channel Settings
Next page
VCA Deep Learning Skeleton Tracker