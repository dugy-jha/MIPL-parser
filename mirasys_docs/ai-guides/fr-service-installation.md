# FR Service Installation | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/fr-service-installation

FR Service Installation

Smart services can be used together with the VCA Deep Learning feature. In this case, you should note that you are using the latest NVIDIA drivers, and not the ones that come with the CUDA Toolkit package. More information can be found here.

Requirements

Administrator rights

List Management Service installed

Face Recognition license on the VMS Management Server

RTSP license feature on the VMS Management Server and the VMS Server

Installation

Download latest version from Extranet.

Unzip this example to C:\temp folder.

Start installation double clicking installation file.

Click Install to continue.

Click Next to continue.

Change installation location if needed, if not then click Next to continue.

Change ports and addresses if needed.

If you example install Face Recognition service to other machine than VMS Master, you need change Master address to correct one.

Same apply for Event queue address. Replace this address with that server address where List Management Service is installed.

If you have Nvidia graphics card installed to server, you can keep Use NVIDIA for inference enabled. This create Nvidia models to use graphics card.

Click Next to continue.

FR Installed on local machine

If Face Recognition Service is installed on other machine specifying the name or IP address of the machine using the Face Recognition Service (in this case, tajudeenb-dev2 is using Face Recognition Service from some other machine)

FR Installed on other machine

Click Install to continue and wait.

Installation will take some times until it finished.

Models creation can take up to 30 minutes. This depends how powerful graphics card is in use.

Click Finish to continue.

Click Close to close installation.

Now Face Recognition Service is installed to server and ready to use.

Face Recognition Service send details to VMS Master server and you can configure service via System Manager.

Pagination
Previous page
Face Recognition Introduction
Next page
FR Privacy masks