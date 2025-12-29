# How to edit host file | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-edit-host-file

How to edit host file
When host file editing is necessary?

Host file must be edited, when the customer has multiple networks, where Mirasys Spotter will be used.

How to edit the Host file in VMS server-side

(This is not needed to do if there is not used DynDNS etc. service.)

Check your Windows computer name.

Browse C:\Windows\System32\drivers\etc

Open host file with Notepad
You may need to run Notepad with Administrator user rights

Add the last line with the following format: Internal IP address and Windows Computer name.
For example, an internal IP address is 10.99.100.110, and the PC name is MIRASYSDVMS.

Save changes.

Start the System Manager

Go System and Change recorder addresses.

Enter the computer name into the field.

Hosts-file example

# Copyright (c) 1993-2009 Microsoft Corp. 
# 
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows. 
# 
# This file contains the mappings of IP addresses to hostnames. Each 
# entry should be kept on an individual line. The IP address should 
# be placed in the first column followed by the corresponding hostname. 
# The IP address and the hostname should be separated by at least one 
# space. 
# 
# Additionally, comments (such as these) may be inserted on individual 
# lines or following the machine name denoted by a '#' symbol. 
# 
# For example: 
# 
#      102.54.94.97     rhino.acme.com          # source server 
#       38.25.63.10     x.acme.com              # x client host 
# localhost name resolution is handled within DNS itself. 
# 127.0.0.1       localhost 
109.108.100.1110 MIRASYSIDVMS

How to edit the host file in remote client-side 

Browse C:\Windows\System32\drivers\etc

Open host file with Notepad
You may need to run Notepad with Administrator user rights

Add the last line with the following format: Internal IP address and Windows Computer name.
For  example, the external IP address is 109.108.11.16 and the DVMS recorder PC name is MIRASYSDVMS

Save  changes

On each  Mirasys Spotter site,  the customer must  change the master  recorded address to a computer  name(master  server computer name ) instead of a static IP  address

Hosts-file example

# Copyright (c) 1993-2009 Microsoft Corp. 
# 
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows. 
# 
# This file contains the mappings of IP addresses to hostnames. Each 
# entry should be kept on an individual line. The IP address should 
# be placed in the first column followed by the corresponding hostname. 
# The IP address and the hostname should be separated by at least one 
# space. 
# 
# Additionally, comments (such as these) may be inserted on individual 
# lines or following the machine name denoted by a '#' symbol. 
# 
# For example: 
# 
#      102.54.94.97     rhino.acme.com          # source server 
#       38.25.63.10     x.acme.com              # x client host 
# localhost name resolution is handled within DNS itself. 
# 127.0.0.1       localhost 
109.108.11.16 MIRASYSIDVMS





Pagination
Previous page
How to test connection to Mirasys VMS server from client
Next page
How to configure remote client over public network