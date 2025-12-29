# How to fix error in V7 "No disks configured recorder "Local recorder"" | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-fix-error-in-v7-no-disks-configured-recorde

How to fix error in V7 "No disks configured recorder "Local recorder""

Open Windows local Services

Stop Mirasys VMS services in this order

WDserver

SMServer

DVRServer

Go to Mirasys VMS installation folder

32bit Windows default location C:\Program Files (x86)\DVMS

64bit Windows default location C:\Program Files\DVMS

Open DVR-folder

Copy dvr.xml file to the desktop

Open dvr.xml using Notepad

Go to the line which starts <disks>

Under that, you can see system material disk

Type their correct paths where the material is located

Example

XML
<disks>
<drive number="1" value="D:\dvr\materials\" unusedgb="10" />
<drive number="2" value="E:\dvr\materials\" unusedgb="10" />
</disks>


Save dvr.xml file

Delete dvr.XML.tmp file in DVR-folder and copy this new dvr.xml file to DVR-folder

Start Mirasys VMS services in this order

WDserver

SMServer

DVRServer

Now system start indexing old material and that will take sometimes

After indexing, you can access old material again

Pagination
Previous page
How to configure Moxa to VMS
Next page
Fetch logs