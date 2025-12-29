# How to install the Nvidia CUDA Toolkit | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-install-nvidia-cuda-toolkit

How to install the Nvidia CUDA Toolkit

Nvidia CUDA Toolkit is an essential part of Mirasys VMS when you want to use VCA Deep Learning features.

Currently, this component is needed to install separately on the server where you want to use VCA Deep Learning features with Mirasys VMS and an Nvidia GPU.

Package Download

The package Mirasys-VCA-Deep-Learning-VX.X.X.zip can be downloaded from

Mirasys Extranet

Or the Documentation site Software Download section

When you have downloaded the package, extract this to the desired location example, C:\temp.

Installation

Double-click the setup file: cuda_XX.X.X_XXX.XX_windows.exe.

After this, Windows will ask permission to run this setup file.

Click Yes to continue.

The installer is asking now where to extract the package details.

If there is a need, change this, but if not, then click OK to continue.

Extraction takes some time until it is done.

This depends server specifications, how long this will take.

After this, you should see NVIDIA Installer, which checks the system.

Accept the NVIDIA software license agreement by clicking Agree and Continue.

Select Custom installation type and click Next.

Select CUDA Component and under that select Development and Runtime components. You can untick Other components and Driver components.

If you select these components, this will install the package, including drivers and other components.

In some cases, those drivers can be too old for normal usage.

Click Next to continue.

Use the default installation location and click Next to continue.

If you have selected more than one library, you can get the window below.

Click I understand tick box and click Next to continue.

Now the installer starts installing CUDA Components on this server.

Please wait until the installation is done.

After installation, you get a summary of the installation if there was selected more than the needed components were selected. Click Next to continue.

Click Close to close the installer.

Now NVIDIA CUDA Toolkit is installed on the server, and you are ready to use VCA Deep Learning features.

If the VMS Server does not recognize CUDA and can’t initialize VCA Deep Learning trackers, please restart the VMS Server.

Pagination
Previous page
How to use Wireshark
Next page
Software Download