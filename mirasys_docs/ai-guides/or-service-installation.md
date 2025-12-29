# OR Service Installation | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/or-service-installation

OR Service Installation

For Object Recognition (OR) you need to install ORService and ODSService package.

Requirements

Administrator rights

Object Recognition license on the VMS Management Server

RTSP license feature on the VMS Management Server and the VMS Server

The Object Detection Service has a similarity search cache to speed up Similarity Search, which can be switched on or off.

Note: Using the cache will increase the memory consumption.

You can enable or disable the similarity search cache when installing the service.

Installation

Download latest version from Extranet.

Unzip this example to C:\temp folder.

Start installation double clicking installation file.

Click Install to continue.

Click Next to continue.

Change installation location if needed, if not then click Next to continue.

Change the service HTTP port, main (master) server address and port, the event queue address and port if needed.

HTTP port is by default 8092

The main (master) server uses port 8082 by default

Event queue uses port 5672 by default. The event queue is installed with the ODSService package.

Click Next to continue.

Select at least one of the devices that will be used for OR:

CPU

Intel GPU

NVIDIA GPU

Click Install to continue and wait.

Installation will take some times until it finished.

Models creation can take up to 30 minutes. This depends how powerful graphics card is in use.

Click Finish to continue.

Click Close to close installation.

Now the Object Recognition Service is installed to server and ready to use.

Pagination
Previous page
Object Recognition Introduction
Next page
OR Performance