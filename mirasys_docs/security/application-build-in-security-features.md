# Application build-in security features | Mirasys Help Center

Source: https://documentation.mirasys.com/security/security/application-build-in-security-features

Application build-in security features

Mirasys VMS products are designed to deliver secure, end-to-end communication. Mirasys products are designed to protect privacy and secure data.

Data protection is always important, especially if you intend to be General Data Protection Regulation (GDPR) compliant in the EU.

According to GDPR, when processing such data, the controller of personal data must implement technical or organizational measures designed to implement the data protection principles set out in GDPR. GDPR refers to this as privacy by design.

In the context of a surveillance camera, a relevant example of privacy by design would be a feature that digitally allows the user to restrict image capture to a certain perimeter, preventing the camera from capturing any imagery outside this perimeter that would otherwise be captured.

Recognizable people are the main issue of video surveillance systems. Personal data is any data related to the identified person in the video. It is illegal to record or photograph people in cases this would violate their privacy. Thus, the company or people cannot record anyone at places where there is a reasonable expectation of privacy. Such places include washrooms, homes, toilets, and hotel rooms. Recording people on videos when they are in such locations may cause a violation of privacy, which is protected by Section 10 of the Finnish Constitution.

A company or person can record videos of people in a public place since that person has no reasonable expectation of privacy when he is located in a public place. However, it is not always obvious which place is public and which has privacy properties that cannot be violated by video camera filming. According to the definition, a public place is a place that is generally open and accessible to people—examples of public places: public squares, streets, parks, roads, and beaches. Nevertheless, public places can include pieces of private territories or objects. Thus, the private territories and an object that could be viewed in the public spaces should be defined before choosing the camera angle location and recording the video view. Then, if private objects were defined in the video overview, the camera should be positioned in order not to record private spaces or objects. In case the installation of such a position is impossible, the organization of a video surveillance system should get the official consent of the objects’ owners. Examples of private spaces: are private houses, house entrances and gardens, common neighbor areas, and spaces inside personal cars. Another way to protect privacy zones on web application streams and recorded videos is to create a special feature inside the application when installing a camera. This feature allows choosing part of the camera view that must not be recorded or sent to the web application when the video is streaming. These zones can be black squire or have another form; the private zone can also be blurred. Administrators can set up private zones and user permissions regarding these private zones.

In Mirasys VMS, there is support for privacy masking in two forms – a privacy zone on the camera that cannot be removed and a privacy zone on the camera that (with the right permissions) can be removed to reveal the image behind the mask.

The controller also must implement technical or organizational measures which, by default, ensure the least privacy intrusive processing of the personal data in question. GDPR refers to this as privacy by default.

In the context of a camera, a relevant example of privacy by default could be using privacy masking to keep a sensitive area within the view of the camera private.

1. GDPR - Privacy zones

Use privacy zones to help eliminate surveillance of areas irrelevant to your surveillance target.

Mirasys recommends setting a privacy zone for clients in sensitive areas and places where personal identification is not allowed. Create then a second role that can authorize the mask to be removed.

2. GDPR - Retention time

According to Article 4(1)(e) of the GDPR, recordings must not be retained longer than necessary for the specific purposes for which they were made.

Mirasys recommends that you set the retention time according to regional laws and requirements, and in any case, set the retention time to a maximum of 30 days.

3. Resolution of different points

Different purposes require different image qualities.

When identification is unnecessary, the camera resolution and other modifiable factors should be chosen to ensure no recognizable facial images are captured.

4. Secure material export

Mirasys recommends allowing access to export functionality for a select set of users needing this permission.

Mirasys also recommends only changing the Mirasys Spotter Enterprise Plus role to allow export in SEF Format.

AVI and JPEG exports should not be allowed because they can not be made secure.

This makes the export of any evidence material password-protected, encrypted, and digitally signed, making sure forensic material is genuine, untampered with, and viewed by the authorized receiver only.

5. Client Data encryption functionality

Mirasys recommends that customers use data encryption between the VMS server and clients.

6. Two-Factor Authentication (2FA)

Mirasys recommends that you specify an additional login step for users of Mirasys System Manager.

7. User roles

Apply the principle of least privilege (PoLP).

Mirasys recommends that you only allow access to functionality for a select user set that needs this permission. Only the system administrator can access the system and perform tasks by default.
All new roles and users that are created have no access to any functions until an administrator deliberately configures them.

Set up permissions for all functionality, including viewing live video and recordings, listening to the audio, accessing metadata, controlling PTZ cameras, accessing and configuring, removing privacy zones on the client, working with exports, saving snapshots, and so on.

Grant access to only the cameras that the specific operator needs to access, and restrict access to recorded video, audio, and metadata for operators, either completely or grant access to only the video, audio, or metadata recorded in the past few hours or less.

Regularly assess and review roles and responsibilities for operators, investigators, system administrators, and others with access to the system.

8. Functionality to restrict administrator permissions with user roles

Mirasys recommends limiting the number of users with a System Manager role.
Suppose you need to create multiple Administrator roles. In that case, you can restrict their access by creating Administrator roles that can manage only select parts of the system, such as certain devices or functions.

Mirasys also recommends that the VMS administrator does not have full administrator rights.

Mirasys VMS allows setting different kinds of permissions in the following areas:

System

VMS Servers · Profiles

Users

Pagination
Previous page
Hardening VMS Components