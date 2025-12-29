# Mirasys Kamera-Treiber | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/mirasys-kamera-treiber

Mirasys Kamera-Treiber

Eine Liste von Mirasys Kamera-Treibern.

Use table header to sort columns

Mirasys Kamera-Treibern

	

Zweck

	

VMS-Server-Kompatibilität

	

Unterstützte Funktionen

	

Im Installationspaket

	

Unterstützte Dateien

	

Letzte Version

	

Datum der Veröffentlichung



OnvifIPCapture
	

Zur Erfassung von MJPEG-, MPEG-4-, H.264- und H.265-komprimierten Videodaten von ONVIF-kompatiblen IP-Kameras und Videoservern und zur Unterstützung der PTZ-Funktionalität dieser Geräte.

Unterstützte Kameras:

Alle ONVIF-kompatiblen IP-Geräte.
Unterstützte ONVIF-Profile: S, G, T, M

Anmerkung:

Die Edge-Storage-Funktionalität (Profil G) ist nur für einkanalige Geräte integriert.

	

VMS Version 6.4 oder höher

	

Automatische Suche

H.264-Videokomprimierung

H.265-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

PTZ

Parallele Auto-Suche

Mehrfaches Streaming

Audio (2-Wege)

Geräte-Bewegungserkennung

Multicast-Streaming

CCRiA (Kann die Auflösung im Alarmfall ändern)

CCFiA (Kann im Alarmfall die Framerate ändern)

Edge Storage (Video)

Dynamische Benutzeroberfläche (seit DVMS 8.1.2)

HTTPS-verschlüsseltes Streaming (RTSP über HTTPS-Tunneling)

Fokus/Iris-Einstellung

Privatsphäre-Zonen

	

Ja

	

OnvifIPCapture.dll

OnvifIPCapture.xml

Readme_OnvifIPCapture.txt

	

1.9.11.0

	

15.11.2024



NewAxisIPCapture
	

Zur Erfassung von MJPEG-, MPEG4- und H.264-komprimierten Videodaten von Axis IP-Geräten
(Kameras und Videoserver) und zur Unterstützung der PTZ-Funktionalität.

	

VMS Version 6.4 oder höher (nur x64-Versionen)

	

Automatische Suche

H.264-Videokomprimierung

H.265-Videokompression

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

PTZ

CCRiA (Kann Auflösung bei Alarm ändern)

CCFiA (Can Change Framerate in Alarm)

Datenschutzzonen

Bewegungserkennung des Geräts (Firmware-Version vor 5.50)

Audio (2-Wege)

Mehrfaches Streaming

Parallele Auto-Suche

Kantenlagerung

Multicast-Streaming

Dynamische Benutzeroberfläche (seit VMS 8.1.2)

AXIS License Plate Verifier

Vaxtor LPR

	

Ja

	

NewAxisIPCapture.dll

NewAxisIPCapture.xml

Readme_NewAxisIPCapture.txt

	

2.9.7.0

	

28.10.2024



NewBoschIPCapture
	

Zur Erfassung von H.265-, H.264-, MPEG-4- und MJPEG-komprimierten Videodaten von Bosch IP-Kameras und Videoservern sowie zur Unterstützung der PTZ-Funktionalität von Bosch IP-Geräten.

	

VMS 6.4 oder höher

	

Automatische Suche

H.265-Videokomprimierung

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Mehrfaches Streaming

Zwei-Wege-Audio (G.711Ulaw, AAC)

Privatzonen

Geräte-Bewegungserkennung

Digitale E/A

PTZ

Parallele Auto-Suche

Edge-Speicher

Multicast-Streaming

CCRiA (Kann Auflösung im Alarmfall ändern)

CCFiA (Kann die Framerate im Alarmfall ändern)

HTTPS-Unterstützung (außer beim Senden von Audio an die Kamera)

	

Ja

	

NewBoschIPCapture.dll                

rcpp4.dll or rcpp4x64.dll (v4.61.0.25)

NewBoschIPCapture.xml

Readme_NewBoschIPCapture.txt

	

1.7.8.0

	

10.07.2024



BOSCH_AutoDomeBPDrvG3
	

Alter PTZ-Treiber

	




	




	

Nein

	




	




	






PelcoIPCapture
	

Zur Erfassung von H.264-, MPEG-4- und MJPEG-komprimierten Videodaten von Pelco IP-Kameras und zur Unterstützung der PTZ-Funktionalität von Pelco IP-Kameras.

	

VMS Version 5.4, 5.9.9 und höher

	

Automatische Suche

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

PTZ

Parallele Auto-Suche

	

Ja

	

PelcoIPCapture.dll (v1.8.3.5)

PelcoIPCapture.xml

Readme_PelcoIPCapture.txt

	

1.8.3.5

	

20.02.2019



VivotekIPCapture
	

Zur Erfassung von MJPEG-, MPEG-4- und H.264-komprimierten Videodaten von Vivotek IP-Geräten (Kameras und Videoserver) und zur Unterstützung von PTZ- und IO-Funktionen von Vivotek IP-Geräten.

	

VMS Version 6.4 oder höher

	

Automatische Suche

H.264-Videokomprimierung

H.265-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

PTZ

Parallele Auto-Suche

Mehrfaches Streaming

Audio (nur eingehend)

Kann Auflösung im Alarmfall ändern (CCRiA)

Kann die Framerate im Alarm ändern (CCFiA)

Dynamische Benutzeroberfläche (seit DVMS 8.1.2)

Zwei-Wege-Audio (Audio senden)

	

Ja

	

VivotekIPCapture.dll

VivotekIPCapture.xml

Readme_VivotekIPCapture.txt

	

2.0.1.1

	

18.09.2024



EHIIPCapture
	

Zur Erfassung von H.265-, H.264-, MPEG-4- und MJPEG-komprimierten Videodaten von Hikvision-, Ernitec- und Interlogix-IP-Kameras, DVRs/NVRs und Encodern, zur Unterstützung der PTZ-Funktionalität und anderer unten beschriebener Funktionen.

Unterstützte Kameras:

Hikvision IP-Kameras

Hikvision DVRs/NVRs

Hikvision Encoder

Interlogix IP-Kameras

Ernitec IP-Kameras

	

VMS Version 6.4 oder höher (nur x64-Versionen)

	

Automatische Suche

Parallele automatische Suche

MJPEG-Videokomprimierung

MPEG-4-Videokomprimierung

H.264-Videokomprimierung

H.265-Videokomprimierung

Digitale E/A

PTZ - Kontinuierliche PTZ-Bewegung wird standardmäßig für alle Kameras verwendet

Bewegungserkennung für Geräte

Mehrfaches Streaming

Audio (Zweiwege)

Edge-Speicherung (nur ISAPI-Geräte)

Auflösung im Alarmfall ändern (CCRiA)

Kann die Framerate im Alarmfall ändern (CCFiA)

Multicast-Streaming

ANPR mit Listenverwaltungsschnittstelle und separaten Parametern zum Ein- und Ausschließen von Nummernschild- und Erkennungsbildern

	

Ja

	

EHIIPCapture.dll

EHIIPCapture.xml

HikvisionDVRConnector.xml

HikvisionEncoderConnector.xml

Readme_EHIIPCapture.txt

	

2.1.17.0

	

05.03.2024



EIPCapture
	

Zur Erfassung von MJPEG-, H.264- und MPEG-4-komprimierten Videodaten von e-Vision (El.MO), Dynacolor und Planet IP-Kameras und zur Unterstützung der PTZ-Funktionalität von PTZ-Kameras der genannten Hersteller.

Unterstützte Kameras:

El.MO-Kameras der NH-Serie (e-Vision TPMX10x)

Dynacolor HD IP-Kameras (e-Vision TDMX10x)

Dynacolor HD WDR IP-Kameras (e-Vision TPMX20x)

Dynacolor Kameras der V-Serie (e-Vision TPMX30x/TDMX30x)

Dynacolor IP PTZ-Kameras (e-Vision ElDome)

Planet ICA-HM131/HM131R/HM126/HM126R IP-Kameras

Planet ICA-H652 IP PTZ-Kameras

Dynacolor Full HD Quad-Stream Kameras

	

VMS Version 5.4 oder höher.

	

Automatische Suche

MJPEG-Videokomprimierung

MPEG-4-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

PTZ

Parallele Auto-Suche

Mehrfaches Streaming

	

Ja

	

EIPCapture.dll (v2.3.1.0)

EIPCapture.dat

EIPCapture.xml

Readme_EIPCapture.txt

	

2.3.1.0

	

21.02.2014



GatewayIPCapture
	

Zur Erfassung von MJPEG- und Native-komprimierten Videodaten von Gateway-Servern und zur Unterstützung von PTZ- und E/A-Funktionen.

Unterstützte Kameras:

Alle Gateway-Server mit Promesa 3.0 oder höher

	

VMS Version 6.4 oder höher
(Promesa-Protokoll Version 3.0 oder höher).

	

Automatische Suche

MJPEG-Videokomprimierung

Native Videokompression

Digitale E/A

PTZ

Parallele automatische Suche

	

Ja

	

GatewayIPCapture.dll             

GatewayIPCapture.xml

Readme_GatewayIPCapture.txt

	

1.0.4.0

	

11.08.2016



HTTPIPCapture
	

Zur Erfassung von MJPEG-komprimierten Videodaten von HTTP-IP-Geräten.

	

VMS Version 5.9.9 oder höher.

	

Automatische Suche

Parallele automatische Suche

MJPEG-Videokomprimierung

	

Ja

	

HTTPIPCapture.dll (v1.0.1.0)

Readme_HTTPIPCapture.txt

	

1.0.1.0

	

07.02.2020



IPCameraCapture
	

Zur Erfassung von JPEG/MPEG-4/H.264 komprimierten Video- und Audiodaten von UDP, Amano,
GANZ, Ernitec, Sprinx IPE/NVC und IPN/IPX-Serie von IP-Videoservern und -Kameras
Unterstützung der PTZ-Funktionalität dieser Geräte.

	

VMS Version 5.9.9 oder höher.

	

Automatische Suche

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

PTZ

Kann die Framerate bei Alarm ändern (CCFiA)

Parallele Auto-Suche

Zwei-Wege-Audio

Mehrfaches Streaming

Multicast-Streaming

Zeitsynchronisation

Edge-Speicherung

	

Ja

	

IPCameraCapture.dll (v1.7.3.0)

IPCameraCapture.xml

Readme_IPCameraCapture.txt

	

1.7.3.0

	

20.02.2019



LGEIPCapture
	

Zur Erfassung von H.264- und MJPEG-komprimierten Videodaten von LG Electronics IP-Geräten.

	

VMS Version 5.9.9 oder höher.

	

Automatische Suche

Parallele automatische Suche

MJPEG-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

PTZ

	

Ja

	

LGEIPCapture.dll (v1.0.6.3)

Readme_LGEIPCapture.txt

	

1.0.6.3

	

20.02.2019



NewActiIPCapture
	

Zur Erfassung von MPEG4/MJPEG/H.264 komprimierten Videodaten von Acti, Messoa NIC910/930/950HPRO und Vido AU-GxxIP IP Kameras

	

VMS Version 6.4 und höher.

	

Automatische Suche

Parallele automatische Suche

Erkennung von Gerätebewegungen

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Mehrfaches Streaming

Multicast-Streaming

Datenschutz-Maske

Zwei-Wege-Audio

Digitale E/A

PTZ

Edge-Storage (ab Firmware 6.07.23 und höher)

	

Ja

	

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
	

So erfassen Sie MJPEG/H.264-komprimierte Videodaten von Arecont IP-Kameras

	




	

Automatische Suche

MJPEG-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

Mehrfaches Streaming

Parallele automatische Suche

Kann Auflösung im Alarmfall ändern (CCRiA)

Ändern der Framerate im Alarmfall (CCFiA)

Zwei-Wege-Audio

	

Ja

	

NewArecontIPcapture.dll

NewArecontIPCapture.xml - example of custom parameters file

Readme_NewArecontIPCapture.txt

	

15.08.2019

	

2.2.3.0



NewIQEyeIPCapture
	

Zur Erfassung von MJPEG/H.264 komprimierten Videodaten und G.711 komprimierten Audiodaten von IQEye IP-Kameras.

	

VMS Version 5.12 und höher.

	

Automatische Suche

MJPEG-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

CCFIA (wird über die Konfigurationsdatei IQEye.xml aktiviert)

Audio (nur G.711)

	

Ja

	

NewIQEyeIPcapture.dll (v1.4.6.0)

IQEye.xml

Readme_NewIQEyeIPCapture.txt

	

1.4.6.0

	

21.02.2014



NewMobotixIPCapture
	

Zur Erfassung von MJPEG-komprimierten Videodaten von Mobotix-Kameras und zur Unterstützung der PTZ-Funktionalität

	

VMS Version 5.4, 5.9.9 und höher.

	

Automatische Suche

MJPEG-Videokomprimierung

MxPEG-Videokomprimierung

Digitale E/A

PTZ

Parallele automatische Suche

Audio

	

Ja

	

NewMobotixIPCapture.dll (1.4.0.0)

NewMobotixIPCapture.xml

Readme_NewMobotixIPCapture.txt

	

1.4.2.0

	

27.01.2022



NewPanasonicIPCapture
	

Zur Erfassung von JPEG/MPEG4/H.264/H.265 komprimierten Videodaten von Panasonic IP-Kameras und zur Unterstützung der PTZ-Funktionalität.

Beachten Sie, dass der alte Panasonic-Treiber PanasonicIPCapture heißt.

	

VMS Version 5.9.9 oder höher.

	

Automatische Suche

Parallele automatische Suche

JPEG-Videokomprimierung

MPEG4-Videokomprimierung

H.264-Videokomprimierung

E/A

PTZ

Nur WV-Serie:

Geräte-Bewegungserkennung

Mehrfach-Streaming

Multicast-Streaming

Datenschutz-Maske

Zwei-Wege-Audio

CCFIA

CCRIA

Edge-Speicherung

H.265-Videokompression

	




	

NewPanasonicIPcapture.dll

NewPanasonicIPCapture.xml

Readme_PanasonicIPCapture.txt

	

1.5.12.0

	

19.05.2022



NewSiquraIPCapture
	

Zur Erfassung von MJPEG-, MPEG-4- und H.264-komprimierten Videodaten von Siqura C/S-5x/6x IP-Codecs und MD/HD-2x/6x PTZ-Kameras sowie zur Unterstützung der PTZ-Funktionalität bestimmter Siqura-Geräte.

	

VMS Version 5.4, 5.9.9 und höher.

	

Automatische Suche

MJPEG-Videokomprimierung

MPEG-4-Videokomprimierung

H.264-Videokomprimierung

E/A

PTZ

	

Ja

	

NewSiquraIPCapture.dll (v1.9.4.0)

Readme_NewSiquraIPCapture.txt

	

1.9.4.0

	

21.02.2014



NewSonyIPCapture
	

Zur Erfassung von MJPEG-, MPEG-4- und H.264-komprimierten Videodaten von SONY IP-Geräten und zur Unterstützung zusätzlicher Funktionen von SONY IP-Geräten.

Unterstützte Kameras:

Alle SONY IP-Kameras (außer SNC-RZ30 und SNC-HM662 Kameras) und G5-Videoserver.

	

VMS Version 6.4 oder höher.

	

Automatische Suche

MJPEG-Videokomprimierung

MPEG-4-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

PTZ

Geräte-Bewegungserkennung

Privatzonen

Auflösung im Alarmfall ändern (CCRiA) (nur G2-G4-Kameras)

Änderung der Bildrate im Alarmfall (CCFiA) (nur G2-G4-Kameras)

Parallele automatische Suche

Mehrfaches Streaming (für G5-G7-Kameras)

Audio (2-Wege) (für G5-G7-Kameras)

Zeitsynchronisierung (für G5-G7-Kameras)

Edge-Storage (für G5-G7-Kameras)

Dynamische Benutzeroberfläche (seit DVMS 8.1.2)

	

Ja

	

NewSonyIPCapture.dll (v2.6.4.0)

NewSonyIPCapture.xml

Readme_NewSonyIPCapture.txt

	

2.6.4.0

	

22.08.2019



PSIAIPCapture
	

Zur Erfassung von H.264-komprimierten Videodaten von PSIA-IP-Kameras.
Es wird die PSIA-Version 1.1 unterstützt.

Unterstützte Kameras:

PSIA-kompatible IP-Kameras

	

VMS Version 5.12 oder höher.

	

Automatische Suche

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Digitale E/A

Parallele automatische Suche

Dynamische Benutzeroberfläche (seit DVMS 8.1.2)

	

Ja

	

PSIAIPCapture.dll 

Readme_PSIAIPCapture.txt

	

1.2.6.0

	

03.07.2024



RTSPIPCapture
	

So erfassen Sie H.265/H.264/MPEG-4/MJPEG-komprimierte Videodaten von RTSP-IP-Geräten

	

VMS Version 5.9.9 oder höher.

	

Automatische Suche

Parallele automatische Suche

H.265-Videokomprimierung

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Multicast-Streaming (nur RTP)

Audio-Eingang

	

Nein

	

RTSPIPCapture.dll

RTSPIPCapture.xml              

Readme_RTSPIPCapture.txt

	

1.6.4.0

	

30.04.2024



SIPIPCapture
	

Treiber für bestimmte Zenitel-Geräte, die über das SIP-Protokoll arbeiten: Zur Erfassung von H.264-komprimierten Videodaten vom SIP-Proxy

	

VMS Version 7.5 und höher.

	

Automatische Suche

H.264-Videokomprimierung

Zwei-Wege-Audio

	

Nein

	

SIPIPcapture.dll

Readme_SIPIPCapture.txt

	

1.0.0.0

	

17.11.2016



StanleyIPCapture
	

Zur Erfassung von H.264- und MJPEG-komprimierten Videodaten von Stanley IP-Kameras, zur Unterstützung von PTZ-Funktionen und anderen unten beschriebenen Funktionen.

	

VMS Version 5.12 oder höher.

Unterstützte Kameras:

Stanley IP-Kameras

	

Automatische Suche

Parallele automatische Suche

MJPEG-Videokomprimierung

H.264-Videokomprimierung

Digitale E/A

PTZ

Mehrfaches Streaming

Geräte-Bewegungserkennung

Privatzonen

	

Ja

	

StanleyIPCapture.dll

StanleyIPCapture.xml

Readme_StanleyIPCapture.txt

	

1.2.1.6

	

24.09.2021



WisenetIPCapture
	

Zur Erfassung von H.265/HEVC-, H.264- und MJPEG-komprimierten Videodaten von Wisenet IP-Geräten und zur Bereitstellung zusätzlicher Funktionen (Digital I/O, PTZ, Privacy Masking usw.) für diese Geräte. Die SUNAPI-Spezifikation Version 2.x wird unterstützt.

	

VMS Version 7.5 oder höher

Unterstützte Kameras:

Alle Wisenet IP-Geräte

	

Automatische Suche

Parallele automatische Suche

H.265/HEVC-Videokomprimierung

H.264-Videokomprimierung

MPEG-4-Videokomprimierung

MJPEG-Videokomprimierung

Erkennung von Gerätebewegungen

Mehrfaches Streaming

Audio (2-Wege)

Multicast-Streaming

Datenschutz-Maskierung

Digitale E/A

PTZ

Edge Storage (seit DVMS 8.0.0)

Dynamische Benutzeroberfläche (seit DVMS 8.1.2)

CCRiA (Kann die Auflösung im Alarmfall ändern)

CCFiA (Kann die Framerate im Alarmfall ändern)

Zeitsynchronisation

Videoverlust-Erkennung

Vaxtor ALPR

	

Ja

	

WisenetIPCapture.dll

WisenetIPCapture.xml

TODO: Timezones.xml

Readme_WisenetIPCapture.txt

	

1.2.14.0

	

30.05.2023




Pagination
Previous page
Add-Ins
Next page
Installieren externer Treiberpakete