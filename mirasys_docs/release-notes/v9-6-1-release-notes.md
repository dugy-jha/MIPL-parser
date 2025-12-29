# Mirasys VMS V9.6.1 release notes | Mirasys Help Center

Source: https://documentation.mirasys.com/release-notes/releasenotes/v9-6-1-release-notes

Mirasys VMS V9.6.1 release notes
Release date: 30.08.2023
Enhancements

Advantech I/O card driver

Ability for the system to make numerous attempts to find an available network path or disk for archiving, so that archiving still works when the network path is disconnected and reconnected

Fixes 
Spotter

Fixed: English language naming for panning in 360 camera de-warping plugin.

Fixed: Image scaling on live and playback streaming.

Fixed: When Spotter tries to open an unknown WMV file, an information message will be displayed in the Spotter notifications list.

Spotter Web 

Fixed: Vulnerability issues in Spotter Web

Spotter Player

Fixed: The link to logs in the Spotter Player About window has been removed.

System Manager

Fixed: Improved stability and controlled handle count reduction during application use.

Fixed: Finnish translation improvement for streams and stream type naming.

Face Recognition and Licence Plate Recognition

Fixed: LPR and FR Services open and close streams in a proper way. 

Fixed: When using Nvidia GPU and there is a memory error from the AI inference, the FR or LPR service will be restarted.

Gateway

Fixed: Gateway installer now includes all necessary files for remote export via SDK test tool

System

Fixed: Spotter Smart Search plugin uses the correct List Management Service (LMS) address when LMS is installed on another machine than SmServer.

Drivers

Fixed: Parameters handling for text/regex parsing by updating UniversalDataDriver to version 2.16.0.0

Fixed: VideoEncoder2Configuration by updating OnvifIPCapture to version 1.8.13.0

Fixed: EHIIPCapture has been updated to version 2.1.16.0




You can download the release notes as a PDF file here V9.6.1 Release Notes .pdf

Pagination
Previous page
Mirasys VMS V9.6.2.2 release notes
Next page
Mirasys VMS V9.6.0 release notes