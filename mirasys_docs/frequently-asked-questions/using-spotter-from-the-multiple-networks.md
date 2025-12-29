# Using Spotter from the multiple networks | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/using-spotter-from-the-multiple-networks

Using Spotter from the multiple networks

If the user is using Spotter from the multiple networks, then the DNS name must be used instead of the static IP address on the VMS server side.

Editing host file

Check your Windows computer name.

Browse C:\Windows\System32\drivers\etc

Open host file with Notepad

You may need to run Notepad with Administrator user rights

Add the new line to the end of the host file with the following format: Internal IP address and Windows Computer name.

For example, an internal IP address is 10.99.100.110, and the PC name is DR-master.

Save changes.

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

# 102.54.94.97 rhino.acme.com # source server

# 38.25.63.10 x.acme.com # x client host

# localhost name resolution is handled within DNS itself.

# 127.0.0.1 localhost

109.108.11.16 DR-master

Actions in the System Manager

Go to the System tab in the System Manager

Click Change VMS server addresses

Select the VMS server from the list

Click Change VMS server address

Enter the VMS server computer name(DNS name) to the New VMS server address field

Click OK

Actions in the Spotter side

Browse C:\Windows\System32\drivers\etc

Open host file with Notepad

You may need to run Notepad with Administrator user rights

Add the new line to the end of the host file with the following format: Internal IP address and Windows Computer name.

For example, an internal IP address is 10.99.100.110, and the PC name is DR-master.

Save changes

On each Mirasys Spotter site, the customer must change the master recorded address to a computer name(master server computer name ) instead of a static IP address

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

# 102.54.94.97 rhino.acme.com # source server 

# 38.25.63.10 x.acme.com # x client host 

# localhost name resolution is handled within DNS itself. 

# 127.0.0.1 localhost 

109.108.11.16 DR-master

Running Spotter as Administrator

When the Spotter starts with Run as administrator, the user can select different addresses and where to connect.

Right-click top of the Spotter icon and select Run as administrator

Hit the Delete button

Click Add

Set the name of the connection

Set the computer name of the VMS server PC to the Address field

Click Ok

When connection between the Spotter and VMS server is okay, Connection status Connected is shown

Click Continue to create connection to the selected VMS server

Pagination
Previous page
Using Spotter From Outside A Firewall
Next page
Spotter freezes when using machine with two GPU's (Integrated and External)