# If Spotter Web installations fails | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/if-spotter-web-installations-fails

If Spotter Web installations fails

In some cases it’s possible that Spotter Web installation fails. Spotter Web installer use Windows DISM tool to install necessary Windows side components.

Troubleshooting

Check what is possible error on installation logs.

Check that Windows is updated with latest updates.

Check that .NET Framework 3.5 is installed on Windows.

Windows 11 and Windows 10 guide

Windows Server

Run System File Checker tool

Try installing needed components via Command Prompt.

If Windows components installation via Command Prompt is failing, you can find more information from these logs.

DISM tool log → C:\Windows\Logs\DISM → dism.log

Component-Based Servicing → C:\Windows\Logs\CBS → CBS.log

If you find error SxS_Assembly_Missing, this indicate that some Windows packages are broken. You can download missing package from Microsoft Update Catalog.

After this create new folder C:\temp\cab and download needed KB package to c:\temp folder.

Run command line to extract the .cab file from the msu file.

expand -F:* C:\temp\kbfilenamehere C:\temp\cab


Then run DISM tool below to add .cab file to your wim image.

DISM /online /add-package /packagepath:c:\temp\cab\kbfilename.cab


And wait that install succesfully.

That can take sometimes until is done.

Install all missing/broken packages and then reboot Windows.

Now you can try again install components via Command Prompt.

If these tips are not helping, please contact with logs to Mirasys Support.

Pagination
Previous page
Spotter Web Certificate using Let´s Encrypt - v1.0
Next page
IIS Manual installation via Command Prompt