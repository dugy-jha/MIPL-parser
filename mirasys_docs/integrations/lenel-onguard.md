# Lenel OnGuard | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/lenel-onguard

Lenel OnGuard

Mirasys VMS is integrated with Lenel to have the possibility to get live, playback, PTZ, alarms, digital IO events, and motion detection events from DVMS to Lenel OnGuard. Integration is done over Gateway.

Lenel OnGuard uses these VMS functionality:

Add Mirasys DVMS as Recorder to the Lenel OnGuard

Add cameras to Lenel OnGuard

Watch Live video from the cameras

Watch playback from cameras

Control PTZ for PTZ cameras

Get IO states

Get alarms

Get motion detection events

Requirements

Mirasys VMS 9.5 or newer

License feature Lenel Gateway Connector

Lenel OnGuard 8.1

Configuration
Mirasys VMS

Create new user which can be used for this integration

Add wanted cameras to this user profile

Check that user has access rights to use Gateway

Lenel OnGuard use ports 9999 and 9000 TCP, which is also in use Mirasys VMS Gateway.

Change Mirasys VMS Gateway ports to example 9998 and 7000 TCP.

Lenel OnGuard

Install Mirasys add-on to Lenel

Use the Mirasys VMS Lenel add-on installer (8.1 Accessory Add On for Mirasys VMS 1.0.2 or newer)

Add Mirasys recorder to Lenel OnGuard using System Administration -> Digital Video

Add cameras

Using Alarm Monitor

An alarm monitoring application is used as a client to work with Mirasys VMS.

In this application, the user can see the connection status of the recorder and cameras, open live, playback, control PTZ, receive alarms, digital IO states, and motion events.

Check that "LS Communication Server" is running in Windows services

Camera live and playback
Working with alarms, IO states, and motion events

To enable motion detection events, this need to be activate via Mirasys System Manager.

Open System Manager

Go to General System Settings

Enable Use motion detection events

Updating to newer Lenel version

Before Lenel can be upgraded to newer version example 8.2, check that there is available new Mirasys VMS add-on installer which is certificated to work wanted newer Lenel version.

Troubleshooting
Lenel can’t make connection to Mirasys VMS

Check that license has Lenel Gateway Connector feature enabled

Check that Gateway communication is working

Pagination
Previous page
ivIP Webservice integration (IVA)
Next page
Magos Radar