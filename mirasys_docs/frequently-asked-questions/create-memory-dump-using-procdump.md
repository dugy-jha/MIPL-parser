# Create memory dump using ProcDump | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/create-memory-dump-using-procdump

Create memory dump using ProcDump

In some cases logs are not enough to find reason. For this we need to get memory dump from running service.

There is several ways to take that. One way is to use Windows Task Manager but there is also other way to do it, example using Microsoft tool ProcDump. ProcDump is better option when application or service is crashing and to find reason there is need to make memory dump.

Download ProcDump from Microsoft site

Extract zip package to example C:\temp

Then open Command Prompt “Run as administrator”

Go to that folder where this ProcDump is extracted

Then run command procdump -e -ma servicename.exe C:\temp

This command run ProcDump and start monitoring wanted service

When this service example crash, this generate memory dump file to C:\temp folder, where this can be zip and send to forward




Pagination
Previous page
Create memory dump using Windows Task Manager
Next page
How to upgrade Windows 7 to Windows 10