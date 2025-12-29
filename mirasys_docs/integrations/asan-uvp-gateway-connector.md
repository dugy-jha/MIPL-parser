# Asan UVP Gateway Connector | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/asan-uvp-gateway-connector

Asan UVP Gateway Connector

Asan UVP Gateway Connector this integration allow Asan UVP connect to Mirasys VMS system and playback live or recorder material and fetch events over Mirasys Gateway.

Requirements

Licenses Mirasys VMS

Mirasys Gateway

Same version as Mirasys VMS.

Mirasys Gateway is not always installed with Mirasys VMS.

Please check under Windows installed programs that Mirasys Gateway is installed.

Standalone environment Mirasys Gateway is usually installed with Mirasys VMS server.

Multi-server environment there is no need to install multiple Mirasys Gateways per server, only one is enough if that has access to all Mirasys VMS servers.

Asan UVP Gateway Connector feature on license

Mirasys Gateway installation

Download latest Mirasys Gateway installation package from Extranet or Documentation Portal.

Double click installation package and wait.

When wizard is started click Install to continue and wait.

Click Next to continue.

Accept license agreement and click Next to continue.

Change installation path if needed and click Next to continue.

Change SM Server address (VMS Master) if that is needed and click Next to continue.

Click Install to make installation and wait.

Click Finish to close installation wizard.

Click Close to close installation.

Now you have installed Mirasys Gateway on server.

Configuration

Open System Manager

Go to Profiles tab

Create new profile which has wanted cameras and alarms which can be fetch to Asan UVP.

After profile creation, go to Users Group tab

Create new Users Group for Asan UVP

Create user under this created group which is allowed to connect this VMS environment.

Now you have created user for Asan UVP.

More information can be found in Mirasys VMS Admin Guide.

Connecting via Asan UVP

Check that port 9000 TCP is allowed incoming connections on Windows Firewall.

On default installer make port openings.

Share username and password with IP-address or DNS name to Asan UVP configuration personel.

They can add this Mirasys VMS part of Asan UVP environment.

Now Asan UVP can make connection to Mirasys VMS environment.

Troubleshooting

Asan UVP can’t make connection

Check shared username and password.

Check that port 9000 TCP is open in Windows Firewall.

Check that Mirasys Gateway is installed and that is same version as Mirasys VMS.

Check that license has Asan UVP Gateway Connector feature included.

Pagination
Previous page
Advantech IO card implementation
Next page
Axis metadata integration