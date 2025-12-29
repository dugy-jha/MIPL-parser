# Axis Perimeter Defender application | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/axis-perimeter-defender-application

Axis Perimeter Defender application

On this article we make example integration between Mirasys VMS and Axis Perimeter Defender application. More details for Axis Perimeter Defender application you can find here.

Instructions
Preliminaries

Licensed Mirasys VMS (Feature Universal Data Driver)

Axis camera with Axis Perimeter Defender

Setup

Install Mirasys VMS to your server and license it

After that install Axis Perimeter Defender configuration tool

You need this tool to license and configure Axis Perimeter Defender application

Copy UUD4 file for Axis Perimeter Defender application to DVR-folder

You can file UDD4 files end of this article

Now you configure Mirasys VMS Text channel to wanted port, here example picture where configuration is done port 40001




When Text channel configuration is done, you can use Axis Perimeter Defender configuration tool to install, calibrate, make scenarios and configure alarm notifications of Axis Perimeter Defender application

To send out alarm notification to Mirasys VMS Text channel you need to enable XML format sending, here example picture for configuration




You can test Outputs section that alarm notifications are working correctly

If everything is correctly configured you can see alarm event on Spotter

Files

You can find on this zip files two versions of Axis Perimeter Defender application UDD4 files. Version 1 support only one alarm event and version 2 support multiple alarm events. You can use text editor to make change on these xml files.

UDD4AxisPD.zip




Pagination
Previous page
Axis metadata integration
Next page
Ajax Systems