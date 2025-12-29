# Mirasys VCA License Server | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/mirasys-vca-license-server

Mirasys VCA License Server

This license server allows the use of VCA in virtual machine/s or if you want to handle licensing in one place for all servers. For this, you need to install Mirasys VCA License Server to physical hardware and license it.
This server can then share licenses to virtual machine/s.

This feature is supported by 9.4 forward.

Do not install any other services to license server. This can cause issues on licensing side.

You don’t need install VCA License Server if you are using example Master as License Server and this is physical server. On this case VMS include VCA and you can install licenses via System Manager - VCA Settings. Then connect each servers to this Master IP-address.

Port

8080, TCP for VCA License Server Management

15769, TCP for VCA License Port

Installation

Download the latest Mirasys VCA License Server package from Mirasys Extranet.

Extract ZIP-package on the wanted place and start installation double-clicking installation file

Click Next to proceed

Accept End-User License Agreement and click Next

Follow instructions until the installation is finalized

Usage and licensing

To log in to Mirasys VCA License Server, you need to use the browser and go to the site http://localhost:8080/.
The default username is admin, and the default password is admin

On the main page, you can access settings via the burger menu.
Adding the license

Open Settings

Open Licenses

Copy Hardware Code and send it to Mirasys to receive license details.

When you have received the activation code from Mirasys, paste the code to the Activation Code field and click Add the new license

When you have added wanted licenses or licenses to the system, you can proceed on Mirasys VMS side.

Mirasys VMS Configuration

Open System Manager, go to the server section and select VCA Settings.

This opens a new window to find a similar burger menu like earlier.

Under this menu, you can find Settings to tell license server address DNS/IP-address.

When you have to fill License Server address, you can click Connect to this.

If the connection is made successfully, this shows Mirasys VCA License Server licenses.

After this, you can go to VCA Settings and sources to assign a wanted license to the wanted camera channel.

Pagination
Previous page
Mirasys VCA Deep Learning
Next page
Cloud Licensing