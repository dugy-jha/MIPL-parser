# How to install CA certificate to Windows 10 store | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-install-ca-certificate-to-windows-10-store

How to install CA certificate to Windows 10 store

It is recommended to add the CA certificate to your Windows certificate store so your web browser won’t pop-up a security warning regarding invalid security certificate and won’t block the connection to the device. This will ensure a secure HTTPS connection to your devices.

Open the Windows Start menu and enter mmc to open the Console Root.

In the console, go to File > Add/Remove Snap in…

In the list on the left side, select Certificates and choose to manage the certificates for the Computer account. Click OK.

Navigate to Certificates – Local computer > Trusted Root Certification Authorities and right-click
on Certificates. Choose All Tasks > Import…

Select the generated CA certificate saved on your computer or your own CA certificate and
place it in the Trusted Root Certification Authorities store.

Click Next and Finish. The certificate is now added to the store:

Restart your web browser, the connection is now secure.

Pagination
Previous page
Spotter For Windows real-time images are not updated smoothly
Next page
How to change VMS Service to Automatic (Delayed Start)