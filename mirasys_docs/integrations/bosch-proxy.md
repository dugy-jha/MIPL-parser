# Bosch Proxy | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/bosch-proxy

Bosch Proxy

Bosch Proxy is a separate service that can be installed on a VMS server. With this service, the system can receive Bosch metadata from the camera. This proxy needs to be installed on all VMS servers where you want to fetch metadata from the Bosch camera. Proxy configuration happens using the VMS server Text Channels feature.

Requirements

Net Framework 4.8 or newer

Administrator user rights

Bosch Proxy

The installer can be downloaded from the Extranet.

Bosch SDK

The installer includes this and installs it as part of the proxy installation

The latest UDD files can be found under the DVR folder

Default location C:\Program Files\DVMS\DVR\UDDConfigExamples

Installation

Extract the zip file to the example c:\temp.

Double-click the setup file.

This open installation wizard, click Install to continue.

Now the installer opens the Bosch VideoSDK installation. Click Next to continue.





Accept the license terms and click Next to continue.





Check that features are enabled and click Next to continue.


Click Install to continue and wait for the installation to finish.





Click Finish to close the Bosch VideoSDK installer.





Click Next to start the Bosch Proxy installation.


Select the installation place or use the default place and click Next to continue.





Click Install to start the installation





Wait until the installation is completed and click Finish.





Click Close to end the Bosch Proxy installation.


Now Bosch Proxy is installed on the VMS server.

After installation, check that you have a file under the DVR folder.

BoschIVA.xml

Copy the latest BoschIVA.xml from the zip file to under the DVR folder.

BoschIVA.xsd

If not, you can copy them from the UDDConfigExamples folder to the DVR folder.

Configuration

Check that the Bosch camera is added to the system using native driver and image is working

You can check this under System Managers → Cameras

Create a new Text Channel for the wanted camera

On Text Channel, you need

Select Model; UniversalDataProxyModel

Proxy Service; BoschIVAProxy

Device Address; Camera IP

Device Port; Camera port, default is 80

Username; Camera username

Password; Camera password

Incoming TCP Port; This is the port for Proxy internal communication, Default 40000

If the same server has multiple cameras that use Proxy, this port needs to be different for each Text Channels; for example, starting from 40000, 40001, etc.

Validation; XSD

Configuration file; BoschIVA.xml

Send the “End” event after N; 0

Forward incoming message to; Empty


Now you can save these settings and check via Spotter that the Text Channel is working and you can see data from the camera.

If you are using a different profile on the Spotter side, please add this Text Channel to the wanted profile; without this, you can’t see this Text Channel on Spotter

If everything works, you should see some event data in the Text Channel





When everything is working and you can see data on Text Channel, you can use System Manager to do alarms based on camera metadata events.

NOTE

Suppose you modified the UDD file but didn’t change the name of this file. The VMS update will overwrite this file. Please make a copy or use your file name for the modified UDD file, which you can then update to the text channel Configuration file.

Bosch IVA configuration is made using Bosch Configuration Manager which is a separate tool for configuration.

We use default metadata event names.

If you use your event names, please update the correct event names in the UDD file.

Troubleshooting

No data in the Text Channel

Check the configuration and test that the camera is working as normal on the VMS side.

Check the Text Channel username and password.

Check that the event name matches the XML file event name.

Event missing

If there is an event missing, you can add this to the XML file and then restart services to reload this new file.

Can’t receive events

Check that the camera side has all the needed services enabled

HTTP

HTTPS

RCP+

RCP+ over HTTPS

Pagination
Previous page
Ajax Systems
Next page
Commbox Multi I/O integration