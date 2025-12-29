# How to run Command Prompt as SYSTEM user | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-run-command-prompt-as-system-user

How to run Command Prompt as SYSTEM user

Download PsTools to your machine.

Extract this zip package to wanted place; example C:\temp

Open Command Prompt using Administrator user rights

Go to PsTools extracted folder

Run command

psexec -i -s cmd.exe


This open new Command Prompt window and on that window you are SYSTEM user

You can check this using command

whoami


This output results of user who you are currently

nt authority\system

Pagination
Previous page
Lost Microsoft SQL Express password/user
Next page
How to run HP Diagnostics