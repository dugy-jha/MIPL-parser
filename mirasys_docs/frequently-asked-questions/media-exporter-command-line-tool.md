# Media Exporter Command Line Tool | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/media-exporter-command-line-tool

Media Exporter Command Line Tool
Command line arguments

MediaExporter.exe <SettingsFile> [optional arguments]

<SettingsFile> - Name of a XML file which contains export parameters. Mandatory parameter.
/encrypted - Settings file is encrypted.
/remove - Settings file must be removed immediately after it has been read.
/lang=<langCode> - Set user interface language. For example "/lang=fi" sets texts to Finnish language.
/skin=<skinName> - Define which skin is used. For example "/skin=Carbon" sets Carbon skin to MediaExporter. Possible skin values are:
M
Carbon
/autoexit - Exit application when exporting is completed (either successfully or unsuccessfully).

Example: Start MediaExporter with plain text export settings file, and use default language (English) and default skin (M).

 MediaExporter.exe "C:\Temp\ExportSettings.xml"


Example: Start MediaExporter with encrypted export settings file, remove the settings file after it has been read, use Finnish language, Carbon skin and exit application when export is done.

MediaExporter.exe "C:\Temp\ExportSettings.dat" /encrypted /remove /lang=fi /skin=Carbon /autoexit

Export parameters

Export parameters are specified in a XML-file. It is recommended that this file is saved in UTF-8 format.

Parameters

Use table header to sort columns

Element

	

Attribute

	

Required

	

Example

	

Information




session

	




	




	




	










	

server

	

Mandatory

	

127.0.0.1

	

Specifies SmServer address. It can be either an IP address or a DNS name.







	

port

	

Optional

	

5008

	

Specifies SmServer address port. If the port value doesn't exist, 5008 value is used. New in 7.4.3 version.







	

user

	

Mandatory

	

Admin

	

Valid username on SM Server with export- and profile rights.







	

password

	

Mandatory1

	




	

Valid password for given username.







	

passwordsecond

	

Optional1

	




	

Valid second password for given username. New in 7.4.0 version.




time

	




	




	




	










	

start

	

Mandatory

	

2010-05-24 15:25:39.567Z

	

Time has following format: yyyy-MM-dd HH:mm:ss.fff (year, month, day hours, minutes, seconds, milliseconds).
Using capital 'Z' in the end means UTC-time, without 'Z' the time is local time.







	

end

	

Mandatory

	

2010-05-25 15:25:39.567

	

Uses same format as start. End time must be larger than start time.




file

	




	




	




	










	

name

	

Mandatory

	

MyClip

	

File name to be used, without file extension. Extension will be added based on requested fileformat.







	

directory

	

Mandatory

	

F:\

	

Directory where the file will be written. Must contain drive letter.







	

maxVideoWidth

	

Optional

	

2048

	

If defined, video is resized so that it is not wider than this value. Values not divisible by 8 will be converted to nearby 8 divisible. Minimum value is 50.







	

maxVideoHeight

	

Optional

	

2048

	

If defined, video is resized so that it is not taller than this value. Values not divisible by 8 will be converted to nearby 8 divisible. Minimum value is 50.




writer

	




	




	




	










	

assembly

	

Mandatory

	

MediaWriterAsf

	

A valid Mirasys-signed Media Writer assembly.







	

class

	

Mandatory

	

Mirasys.MediaWriter.MediaWriterAsf

	

Matching class name for the assembly.







	

addLogoImages

	

Optional

	

true

	

Specified whether manufacturer and customer logos are added to video clip images. This attribute was added to 6.5.0 version







	

encodeQuality

	

Optional

	

true

	

Encoding quality for ASF files value range of 1-99. This attribute was added to 7.5.1 version







	

keyFrameInterval

	

Optional

	

true

	

Key frame interval in seconds for ASF files. 0 means that each frame is a key frame. This attribute was added to 7.5.1 version




cdrom

	




	




	




	










	

erase

	

Optional

	

true

	

Boolean. Specifies whether cdrom is to be erased prior to writing. Option is not used if target is not a burnable media. Default (false).







	

multisession

	

Optional

	

true

	

Boolean. Specifies whether cdrom multisession is used. Option is not used if target is not a burnable media. Default (false).







	

autorun

	

Optional

	

false

	

Boolean. Specifies whether cdrom will be burned as autorun on inserting the media. Option is not used if target is not a burnable media. Default (false).




profile

	




	




	




	










	

name

	

Mandatory

	

Service

	

Must be a valid profile on target SM server.




node

	




	




	




	










	

path

	

Mandatory

	

/Cameras/Camera 11 or #11

	

Path is composed of "/" character followed by site names, and ending with profile node name. Alternatively path can be a GUID value or Camera index in profile.




player

	




	




	




	







mainfile

	




	




	




	










	

path

	

Optional

	

F:\Myfiles\MediaPlayer.exe

	

Specifies the location where MediaPlayer.exe will be copied from.




file

	




	




	




	










	

path

	

Optional

	

F:\Myfiles\MediaPlayer.exe.config

	

Specifies source location of additional files required by MediaPlayer.exe (mainfile) to function. There may be multiple file-nodes in one xml.




bookmarks

	




	

Optional

	




	










	

data

	

Mandaroty

	




	

Bookmark data




layoutdata

	




	

Optional

	




	







node

	




	

Mandatory (1-N items)

	




	










	

id

	

Mandaroty

	




	

Profile node id







	

data

	

Mandaroty

	




	

Profile node layout data

1 = Can be an empty string

Example XML-file
XML
<?xml version="1.0" encoding="utf-8" ?>
<export>
    <session server="127.0.0.1" user="Admin" password=""/>
    <time start="2010-01-04 09:58:00.000" end="2010-01-04 18:30:00.000"/>
    <file name="MyClip" directory="F:\" maxVideoWidth="2048" maxVideoHeight="1536"/>
    <writer assembly="MediaWriterAsf" class="Mirasys.MediaWriter.MediaWriterAsf"/>
    <cdrom erase="true" multiSession="true" autorun="false"/>
    <profile name="Service">
        <node path="/Cameras/Camera 11"/>
    </profile>
</export>

Example 1: Camera 10 is under Cameras folder
<node path="/Cameras/Camera 10"/>

Example 2: Camera 10 is at the root level
<node path="/Camera 10"/>

Pagination
Previous page
How to fix SQL login error
Next page
How to change programs DEBUG level