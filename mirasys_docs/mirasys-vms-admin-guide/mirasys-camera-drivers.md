# Mirasys Camera Drivers | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/mirasys-camera-drivers

Mirasys Camera Drivers

A list of Mirasys Camera Drivers.

Use table header to sort columns

Driver name

	

Purpose

	

VMS Server compatibility

	

Supported features

	

In installation package

	

Supported files

	

Latest version

	

Release date



OnvifIPCapture
	

To capture MJPEG, MPEG-4, H.264 and H.265 compressed video data from ONVIF-compliant IP cameras and video-servers and to support PTZ functionality of these devices.

Supported cameras:

All ONVIF-compliant IP devices.
Supported ONVIF Profiles: S, G, T, M

Note:

The Edge Storage functionality (Profile G) is integrated for single-channel devices only.

	

VMS version 6.4 or higher

	

Auto-search

H.264 video compression

H.265 video compression

MPEG-4 video compression

MJPEG video compression

Digital I/O

PTZ

Parallel auto-search

Multiple streaming

Audio (2-way)

Device motion detection

Multicast streaming

CCRiA (Can Change Resolution in Alarm)

CCFiA (Can Change Framerate in Alarm)

Edge Storage (video)

Dynamic UI (since DVMS 8.1.2)

HTTPS encrypted streaming (RTSP over HTTPS tunneling)

Focus/Iris adjustment

Privacy Zones

	

Yes

	

OnvifIPCapture.dll

OnvifIPCapture.xml

Readme_OnvifIPCapture.txt

	

1.9.11.0

	

15.11.2024



NewAxisIPCapture
	

To capture MJPEG, MPEG4 and H.264 compressed video data from Axis IP devices
(cameras and video-servers) and to support PTZ functionality.

	

DVMS version 6.4 or higher (x64 versions only)

	

Auto-search

H.264 video compression

H.265 video compression

MPEG-4 video compression

MJPEG video compression

Digital I/O

PTZ

CCRiA (Can Change Resolution in Alarm)

CCFiA (Can Change Framerate in Alarm)

Privacy zones

Device motion detection (firmware version before 5.50)

Audio (2-way)

Multiple streaming

Parallel auto-search

Edge Storage

Multicast streaming

Dynamic UI (since DVMS 8.1.2)

AXIS License Plate Verifier

Vaxtor LPR

	

Yes

	

NewAxisIPCapture.dll

NewAxisIPCapture.xml

Readme_NewAxisIPCapture.txt

	

2.9.7.0

	

28.10.2024



NewBoschIPCapture
	

To capture H.265, H.264, MPEG-4 and MJPEG compressed video data from Bosch IP cameras and video-servers and to support PTZ functionality of Bosch IP devices.

	

VMS 6.4 or higher

	

Auto-search

H.265  video compression

H.264  video compression

MPEG-4 video compression

MJPEG  video compression

Multiple streaming

Two-way audio (G.711Ulaw, AAC)

Privacy zones

Device motion detection

Digital I/O

PTZ

Parallel auto-search

Edge storage

Multicast streaming

CCRiA (Can Change Resolution in Alarm)

CCFiA (Can Change Framerate in Alarm)

HTTPS support (except sending audio to camera)

	

Yes

	

NewBoschIPCapture.dll                

rcpp4.dll or rcpp4x64.dll (v4.61.0.25)

NewBoschIPCapture.xml

Readme_NewBoschIPCapture.txt

	

1.7.8.0

	

10.07.2024



BOSCH_AutoDomeBPDrvG3
	

Old PTZ driver

	




	




	

No

	




	




	






PelcoIPCapture
	

To capture H.264, MPEG-4 and MJPEG compressed video data from Pelco IP cameras and to support PTZ functionality of Pelco IP cameras.

	

VMS version 5.4, 5.9.9 and higher

	

Auto-search

H.264 video compression

MPEG-4 video compression

MJPEG video compression

Digital I/O

PTZ

Parallel auto-search

	

Yes

	

PelcoIPCapture.dll (v1.8.3.5)

PelcoIPCapture.xml

Readme_PelcoIPCapture.txt

	

1.8.3.5

	

20.02.2019



VivotekIPCapture
	

To capture MJPEG, MPEG-4 and H.264 compressed video data from Vivotek IP devices (cameras and video servers) and to support PTZ and IO functionality of Vivotek IP devices.

	

VMS version 6.4 or higher

	

Auto-search

H.264 video compression

H.265 video compression

MPEG-4 video compression

MJPEG video compression

Digital I/O

PTZ

Parallel auto-search

Multiple streaming

Audio (incoming only)

Can Change Resolution in Alarm (CCRiA)

Can Change Framerate in Alarm (CCFiA)

Dynamic UI (since DVMS 8.1.2)

Two Way Audio (Audio sending)

	

Yes

	

VivotekIPCapture.dll

VivotekIPCapture.xml

Readme_VivotekIPCapture.txt

	

2.0.1.1

	

18.09.2024



EHIIPCapture
	

To capture H.265, H.264, MPEG-4 and MJPEG compressed video data from Hikvision, Ernitec and Interlogix IP cameras, DVRs/NVRs and encoders, to support PTZ functionality and other features described below.

Supported cameras:

Hikvision IP cameras

Hikvision DVRs/NVRs

Hikvision encoders

Interlogix IP cameras

Ernitec IP cameras

	

VMS version 6.4 or higher (x64 versions only)

	

Auto-search

Parallel auto-search

MJPEG video compression

MPEG-4 video compression

H.264 video compression

H.265 video compression

Digital I/O

PTZ - Continuous PTZ movement is used by default for all cameras

Device motion detection

Multiple streaming

Audio (two way)

Edge storage (ISAPI devices only)

Can Change Resolution in Alarm (CCRiA)

Can Change Framerate in Alarm (CCFiA)

Multicast streaming

ANPR with list management interface and separate parameters to include/exclude license plate and detection images

	

Yes

	

EHIIPCapture.dll

EHIIPCapture.xml

HikvisionDVRConnector.xml

HikvisionEncoderConnector.xml

Readme_EHIIPCapture.txt

	

2.1.17.0

	

05.03.2024



EIPCapture
	

To capture MJPEG, H.264 and MPEG-4 compressed video data from e-Vision (El.MO), Dynacolor and Planet IP cameras and to support PTZ functionality of PTZ cameras of specified manufacturers.

Supported cameras:

El.MO NH-series cameras (e-Vision TPMX10x)

Dynacolor HD IP cameras (e-Vision TDMX10x)

Dynacolor HD WDR IP cameras (e-Vision TPMX20x)

Dynacolor V-series cameras (e-Vision TPMX30x/TDMX30x)

Dynacolor IP PTZ cameras (e-Vision ElDome)

Planet ICA-HM131/HM131R/HM126/HM126R IP cameras

Planet ICA-H652 IP PTZ cameras

Dynacolor Full HD Quad-Stream cameras

	

DVMS version 5.4 or higher.

	

Auto-search

MJPEG video compression

MPEG-4 video compression

H.264 video compression

Digital I/O

PTZ

Parallel auto-search

Multiple streaming

	

Yes

	

EIPCapture.dll (v2.3.1.0)

EIPCapture.dat

EIPCapture.xml

Readme_EIPCapture.txt

	

2.3.1.0

	

21.02.2014



GatewayIPCapture
	

To capture MJPEG and Native compressed video data from Gateway servers and to support PTZ and I/O functionality.

Supported cameras:

All Gateway server with Promesa 3.0 or higher

	

VMS version 6.4 or higher
(Promesa protocol version 3.0 or higher)

	

Auto-search

MJPEG video compression

Native video compression

Digital I/O

PTZ

Parallel auto-search

	

Yes

	

GatewayIPCapture.dll             

GatewayIPCapture.xml

Readme_GatewayIPCapture.txt

	

1.0.4.0

	

11.08.2016



HTTPIPCapture
	

To capture MJPEG compressed video data from HTTP IP devices.

	

VMS version 5.9.9 or higher

	

Auto-search

Parallel auto-search

MJPEG video compression

	

Yes

	

HTTPIPCapture.dll (v1.0.1.0)

Readme_HTTPIPCapture.txt

	

1.0.1.0

	

07.02.2020



IPCameraCapture
	

To capture JPEG/MPEG-4/H.264 compressed video and audio data from UDP, Amano,
GANZ, Ernitec, Sprinx IPE/NVC and IPN/IPX series of IP video servers and cameras
support PTZ functionality of these devices.

	

VMS version 5.9.9 or higher

	

Auto-search

H.264 video compression

MPEG-4 video compression

MJPEG video compression

Digital I/O

PTZ

Can Change Framerate in Alarm (CCFiA)

Parallel auto-search

Two-way Audio

Multiple streaming

Multicast streaming

Time synchronization

Edge Storage

	

Yes

	

IPCameraCapture.dll (v1.7.3.0)

IPCameraCapture.xml

Readme_IPCameraCapture.txt

	

1.7.3.0

	

20.02.2019



LGEIPCapture
	

To capture H.264 and MJPEG compressed video data from LG Electronics IP devices.

	

VMS version 5.9.9 or higher

	

Auto-search

Parallel auto-search

MJPEG video compression

H.264 video compression

Digital I/O

PTZ

	

Yes

	

LGEIPCapture.dll (v1.0.6.3)

Readme_LGEIPCapture.txt

	

1.0.6.3

	

20.02.2019



NewActiIPCapture
	

To capture MPEG4/MJPEG/H.264 compressed video data from Acti, Messoa NIC910/930/950HPRO and Vido AU-GxxIP IP cameras

	

VMS version 6.4 and higher

	

Auto-search

Parallel auto-search

Device motion detection

H.264 video compression

MPEG-4 video compression

MJPEG video compression

Multiple streaming

Multicast streaming

Privacy mask

Two way audio

Digital I/O

PTZ

Edge storage (starting from firmware 6.07.23 and higher)

	

Yes

	

AADP.dll

ADADP.dll

AFADP.dll

FFMCodec.dll

FisheyeSDK.dll

KMpeg4.dll

PTZParser.dll

NewActiIPcapture.dll

NewActiIPCapture.xml

Readme_NewActiIPCapture.txt

	

2.4.1.0

	

22.11.2017



NewArecontIPCapture
	

To capture MJPEG/H.264 compressed video data from Arecont IP cameras

	




	

Auto search

MJPEG video compression

H.264 video compression

Digital I/O

Multiple streaming

Parallel auto-search

Can Change Resolution in Alarm (CCRiA)

Can Change Framerate in Alarm (CCFiA)

Two-way Audio

	

Yes

	

NewArecontIPcapture.dll

NewArecontIPCapture.xml - example of custom parameters file

Readme_NewArecontIPCapture.txt

	

15.08.2019

	

2.2.3.0



NewIQEyeIPCapture
	

To capture MJPEG/H.264 compressed video data and G.711 compressed audio data from IQEye IP cameras.

	

VMS version 5.12 and higher

	

Auto search

MJPEG video compression

H.264 video compression

Digital I/O

CCFIA (enables through IQEye.xml configuration file)

Audio (G.711 only)

	

Yes

	

NewIQEyeIPcapture.dll (v1.4.6.0)

IQEye.xml

Readme_NewIQEyeIPCapture.txt

	

1.4.6.0

	

21.02.2014



NewMobotixIPCapture
	

To capture MJPEG compressed video data from Mobotix cameras and to support PTZ functionality

	

VMS version 5.4, 5.9.9 and higher

	

Auto-search

MJPEG video compression

MxPEG video compression

Digital I/O

PTZ

Parallel auto-search

Audio

	

Yes

	

NewMobotixIPCapture.dll (1.4.0.0)

NewMobotixIPCapture.xml

Readme_NewMobotixIPCapture.txt

	

1.4.2.0

	

27.01.2022



NewPanasonicIPCapture
	

To capture JPEG/MPEG4/H.264/H.265 compressed video data from Panasonic IP cameras and to support PTZ functionality.

Note that the old Panasonic Driver is PanasonicIPCapture.

	

VMS version 5.9.9 or higher

	

Auto search

Parallel auto-search

JPEG video compression

MPEG4 video compression

H.264 video compression

I/O

PTZ

WV series only:

Device motion detection

Multiple streaming 

Multicast streaming

Privacy mask

Two way audio

CCFIA

CCRIA

Edge storage

H.265 video compression

	




	

NewPanasonicIPcapture.dll

NewPanasonicIPCapture.xml

Readme_PanasonicIPCapture.txt

	

1.5.12.0

	

19.05.2022



NewSiquraIPCapture
	

To capture MJPEG, MPEG-4 and H.264 compressed video data from Siqura C/S-5x/6x IP codecs and MD/HD-2x/6x PTZ cameras and to support PTZ functionality of specified Siqura devices.

	

VMS version 5.4, 5.9.9 and higher

	

Auto-search

MJPEG video compression

MPEG-4 video compression

H.264 video compression

I/O

PTZ

	

Yes

	

NewSiquraIPCapture.dll (v1.9.4.0)

Readme_NewSiquraIPCapture.txt

	

1.9.4.0

	

21.02.2014



NewSonyIPCapture
	

To capture MJPEG, MPEG-4 and H.264 compressed video data from SONY IP devices and to support additional functionality of SONY IP devices.

Supported cameras:

All SONY IP cameras (except SNC-RZ30 and SNC-HM662 cameras) and G5 video servers.

	

VMS version 6.4 or higher

	

Auto-search

MJPEG video compression

MPEG-4 video compression

H.264 video compression

Digital I/O

PTZ

Device motion detection

Privacy Zones

Can Change Resolution in Alarm (CCRiA) (G2-G4 cameras only)

Can Change Framerate  in Alarm (CCFiA) (G2-G4 cameras only)

Parallel auto-search

Multiple streaming (for G5-G7 cameras)

Audio (2-way) (for G5-G7 cameras)

Time synchronization (for G5-G7 cameras)

Edge Storage (for G5-G7 cameras)

Dynamic UI (since DVMS 8.1.2)

	

Yes

	

NewSonyIPCapture.dll (v2.6.4.0)

NewSonyIPCapture.xml

Readme_NewSonyIPCapture.txt

	

2.6.4.0

	

22.08.2019



PSIAIPCapture
	

To capture H.264 compressed video data from PSIA IP cameras.
The PSIA version 1.1 is supported.

Supported Cameras:

PSIA compatible IP cameras

	

VMS version 5.12 or higher

	

Auto-search

H.264 video compression

MPEG-4 video compression

MJPEG  video compression

Digital I/O

Parallel auto-search

Dynamic UI (since DVMS 8.1.2)

	

Yes

	

PSIAIPCapture.dll 

Readme_PSIAIPCapture.txt

	

1.2.6.0

	

03.07.2024



RTSPIPCapture
	

To capture H.265/H.264/MPEG-4/MJPEG compressed video data from RTSP IP devices

	

VMS version 5.9.9 or higher

	

Auto-search

Parallel auto-search

H.265 video compression

H.264 video compression

MPEG-4 video compression

MJPEG video compression

Multicast streaming (RTP only)

Audio input

	

Yes

	

RTSPIPCapture.dll

RTSPIPCapture.xml              

Readme_RTSPIPCapture.txt

	

1.6.4.0

	

30.04.2024



SIPIPCapture
	

Driver for specific Zenitel devices working over SIP protocol: To capture H.264 compressed video data from SIP Proxy

	

VMS version 7.5 and higher

	

Auto-search

H.264 video compression

Two way audio

	

No

	

SIPIPcapture.dll

Readme_SIPIPCapture.txt

	

1.0.0.0

	

17.11.2016



StanleyIPCapture
	

To capture H.264 and MJPEG compressed video data from Stanley IP cameras, to support PTZ functionality and other features described below.

	

VMS version 5.12 or higher.

Supported cameras:

Stanley IP cameras

	

Auto-search

Parallel auto-search

MJPEG video compression

H.264 video compression

Digital I/O

PTZ

Multiple streaming

Device motion detection

Privacy zones

	

Yes

	

StanleyIPCapture.dll

StanleyIPCapture.xml

Readme_StanleyIPCapture.txt

	

1.2.1.6

	

24.09.2021



WisenetIPCapture
	

To capture H.265/HEVC, H.264 and MJPEG compressed video data from Wisenet IP devices and to provide additional functionality (Digital I/O, PTZ, Privacy Masking, etc.) for these devices. SUNAPI specification version 2.x is supported.

	

VMS version 7.5 or higher

Supported cameras:

All Wisenet IP devices

	

Auto-search

Parallel auto-search

H.265/HEVC video compression

H.264 video compression

MPEG-4 video compression

MJPEG video compression

Device motion detection

Multiple streaming

Audio (2-way)

Multicast streaming

Privacy Masking

Digital I/O

PTZ

Edge Storage (since DVMS 8.0.0)

Dynamic UI (since DVMS 8.1.2)

CCRiA (Can Change Resolution in Alarm)

CCFiA (Can Change Framerate in Alarm)

Time synchronization

Video loss detection

Vaxtor ALPR

	

Yes

	

WisenetIPCapture.dll

WisenetIPCapture.xml

TODO: Timezones.xml

Readme_WisenetIPCapture.txt

	

1.2.14.0

	

30.05.2023




Pagination
Previous page
Add-ins
Next page
Installing External Driver Packages