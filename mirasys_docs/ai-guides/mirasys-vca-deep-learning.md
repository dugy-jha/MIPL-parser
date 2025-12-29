# Mirasys VCA Deep Learning | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/mirasys-vca-deep-learning

Mirasys VCA Deep Learning
Requirements

Nvidia GPU with CUDA cores

An NVIDIA GPU with CUDA Compute Capability 7.5 or higher

Depending on the GPU CUDA cores, how many Deep Learning channels you can use on the system

The latest NVIDIA graphics drivers (at least 460.73 or higher).

CUDA Toolkit

Mirasys VMS 9.4 or newer

Deep Learning object files

Installation

Install the latest Nvidia drivers in the system

Download the Mirasys VCA Deep Learning package from the Mirasys Extranet

Extract the package

Browse to the folder CUDA Toolkit

Install CUDA Toolkit with all features

You can find a detailed installation guide here.

Some features are not installed because Microsoft Visual Studio is not needed to install, but the toolkit provides example files

If you have already installed Mirasys VMS, before copying files, the VMS services need to be stopped.

Stop services: WDServer, DVRServer, and SMServer

This is not needed to do if you are using V9.6 or newer

Copy the content of the VCA Deep Learning files folder to C:\Program Files\DVMS\DVR\vca\bin location

This is not needed to do if you are using V9.6 or newer

This path is the default installation location of Mirasys VMS
If you have installed Mirasys VMS in another location, copy the files there

Start WDServer, DVRServer, and SMServer services

This is not needed to do if you are using V9.6 or newer

Now you have installed and are ready to go with Deep Learning tracking.

The VCA engine is started in the VMS server when at least one camera is configured to use the VCA in the System Manager camera settings. The very first VCA engine start will compile the NVIDIA libraries, which can take a lot of time. The time of the compilation depends on the hardware used. During the compilation time, the VCA is not functioning.

It is highly recommended to wait until the NVIDIA libraries are compiled after the VCA is enabled, before doing any other operations on the VMS server.

Licensing is done via local VCA Deep Learning licensing or using License Server (Virtual Environment or, if you want to handle licenses in one place). To get the HWGUID for the VCA license, one camera has to be enabled in the System Manager camera settings to get the VCA engine running. After the VCA is running, the VCA HWGUID can be retrieved from the VMS server license dialog in the System Manager.

In some cases, detection may not work correctly. Please try to increase the image quality or move/zoom the camera image closer to the wanted detection area.

Models are trained using clear images, and in some cases, when using a black and white image or a thermal camera image, the detection might not work correctly. To solve this, you can try using the Deep Learning Filter with Object Tracker.

Pagination
Previous page
VCA Settings on System Manager
Next page
Mirasys VCA License Server