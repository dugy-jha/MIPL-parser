# General settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/general-settings

General settings

In General settings, the columns display the camera number, if the camera is in use, the camera name, quality, resolution, and rate, if the camera uses an AI service, which service, and which camera driver the camera uses. All columns can be sorted in ascending or descending order.

Name

The name of the camera. The system suggests the names like Camera 1, Camera 2, etc.

In Use

Clear this check box if no camera is connected to the camera input or if you want to disable the camera.

360 camera

This tells the Spotter client that the camera is a 360 camera, and Spotter will show the image de-warping options in the camera toolbar (if installed)

Control Mode

This setting has two options: Active (default) and Passive.
If multiple servers have the same camera configured, then one should be made Active, and the others should be Passive.
This way, only the Active server settings are communicated to the camera.

Transport Type

This setting controls how the media stream is transported from camera to server.
The available options are RTP over UDP (default) and RTP over RTSP.
If the camera seems to work poorly with one setting (for example, if there are holes in camera material or difficulty to get all frames from a camera), then the other set can be used.

Decompression codecs

Codecs are used for encoding and decoding video data

Description

Here you can type a description of the camera shown to all users in the Spotter, given they have the user permissions to view this.

Administrative Description

Here you can type a description of the camera. The description will be shown in Spotter, given they have the user permissions to view this.

Camera Info

The “Camera info” tab has checkboxes for what should be automatically included in the Camera Info:

VMS Server

IP address 

Camera model 

AI features used 

Resolution

Frame rate settings 

The information included by ticking the boxes for the camera will be automatically included in the Camera Description in Spotter for that Camera. All boxes are selected by default.

For the information to be shown in Spotter, permission must be given under User Group > Mirasys Spotter Enterprise role properties > Screen > Screen elements to View Camera Info.

Reference image

A reference image is an image captured from the camera, making it easier to identify the cameras.
In addition, in the Spotter program, the users can compare what they see in the video view against the reference image to ensure that the camera is pointed in the right direction.
To change the current reference image, click the Capture image button. To delete a reference image, click the Delete image button.

Pagination
Previous page
Camera settings
Next page
Streams