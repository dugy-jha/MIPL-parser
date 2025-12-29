# LM Service Installation | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/lm-service-installation

LM Service Installation
Requirements

Administrator rights

List Management Service feature is included on V9.6.0 and forward

Installation

Download latest version from Extranet.

Unzip this example to C:\temp folder.

Start installation double clicking installation file.

Click Install to continue.

Change PostgreSQL database password

Wait that PostgreSQL is installed.

You made need to apply firewall rules when installation is going forward.

Click Next to continue.

Change installation location if needed, if not then click Next to continue.

Change ports and addresses if needed.

If you are installing List Management Service on other server, then you need to change this.

Event queue address is same address where List Management Service is installed. Keep this as default.

Click Next to continue.

Click Install to continue.

Wait that installation is finished.

You made need to apply firewall rules when installation is going forward.

Installer install RabbitMQ Server which handle events from List Management Service, Face Recognition Service and License Plate Recognition Service.

Default port 5672 TCP.

Click Finish to end installation.

Click Close to close installation.

Now List Management Service is installed to server and ready to use.

List Management Service send details to VMS Master server and you can configure service via System Manager.

Pagination
Previous page
Mirasys List Management Introduction
Next page
Mirasys Face Recognition (FR)