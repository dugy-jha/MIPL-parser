# Installer fails with the error "Create NATS keys error!" | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/installer-show-error-create-nats-keys-error

Installer fails with the error "Create NATS keys error!"

When installing 9.9.2 or a newer version, which includes a new method to handle VMS events, the installer may fail with an error “Create NATS keys error!”. This error indicates that Windows cannot generate the NATS encryption key, which causes the installation to fail.

This issue can be solved by running the “Machine Key Cleanup” tool:

Download the tool from the Extranet.

Run the tool by right-clicking the exe-file and selecting “Run as Administrator” from the opened context menu.

The tool starts to validate the system keys, and if orphaned files are found, the tool asks the user if the files can be removed. To fix this installation error, the found orphaned files have to be removed.

Exit from the tool and run the installer again.

Pagination
Previous page
Audio channels found -popup window
Next page
Spotter Tips and Tricks