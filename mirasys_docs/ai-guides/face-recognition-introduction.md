# Face Recognition Introduction | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/face-recognition-introduction

Face Recognition Introduction

Face Recognition (FR) is used to identify a human face. It is used in the VMS System to get events when faces are detected from selected video streams and to detect when specific persons are seen in the video. Together with the Mirasys List Management, this allows you to, for example, create an automatic detection system of a person’s access to the premises.

Note that anti-spoofing is not included in version 9.6.

The FR service receives video streams, processes images, detects faces, and sends notifications with detection data to List Management (LM) service for identity and list matching.

Face Recognition service has a separate installer, so it can execute on a separate server or on some VMS server.

Face recognition works with 112 x 112 image size. If the face is larger in the picture, it is first reduced to 112 x 112 assembled before identification is made. Likewise, if the face is smaller in the picture, it is first enlarged to that 112 x112 to size. The recommended size of the face in the image is at least 112 pixels.

On licensing side there is need to add RTSP Streaming Server feature to Management Server and all those servers where is plan to use SmartFR feature. On Management Server side there is need to be add wanted amount of channels of SmartFR feature.

Pagination
Previous page
Mirasys Face Recognition (FR)
Next page
FR Service Installation