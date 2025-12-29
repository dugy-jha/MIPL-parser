# Cannot add VMS server to system (Duplicate identifier) | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/cannot-add-vms-server-to-system-duplicate-identifi

Cannot add VMS server to system (Duplicate identifier)

If you try to add VMS server to Master and you get error

“Failed to add the new VMS server because VMS server identifier is already used by another VMS Server.”

The most likely reason is that you have copied/cloned virtual machine and system has two VMS servers with same identifier/DvrId.

You can recreate DvrId by following steps.

Stop VMS services from that copied/cloned virtual machine.

Go to C:\Program Files\DVMS\DVR.

Delete DvrId.dat file.

If you can’t find this file, check that “Show hidden files, folders, and drivers” are enabled on Windows File Explorer settings.

Start VMS services.

Login to System Manager and check that system is licensed correctly.

Now you can add this server under to Master server.




Pagination
Previous page
Gateway and Multiple Streaming
Next page
VCA license page giving error "Local daemon failed to start"