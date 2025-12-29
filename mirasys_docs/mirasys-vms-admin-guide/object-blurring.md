# Object Blurring | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/object-blurring

Object Blurring

“Blur faces” and “Blur moving objects” settings are available to be set up as additional privacy.
If the facial- or motion-based blurring is enabled for a camera, these are also available on the Spotter side (provided that the user has sufficient permissions.)
The blurring will not be functional on the spotter side- or for exports of the video material for the cameras if they have not been selected on the system administrator side.
Higher resolutions used for the algorithms mean higher accuracy for the algorithms- but also higher CPU loads.

Blur Faces
Minimum face detection confidence
Face detection image size

Using a small face detection size value, a person face must be closer to the camera. Face detection will be faster.

Using bigger face detection size value. a person's face is detected more away from the camera.

300x384

672x384

1008*576

1344x768

Blur Moving objects
Motion detection sensitivity

How sensitively pixel in the image is detected as motion pixel

Background image detection history length

How quickly stationary objects are detected as background

Motion detection input image size

 The smaller size is quicker to process but outputs the worse results.

Original size

1:2 size

1:4 size

1:8 size

Pagination
Previous page
Privacy zone on the client
Next page
Scheduler