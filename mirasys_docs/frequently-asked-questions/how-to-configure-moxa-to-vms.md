# How to configure Moxa to VMS | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-configure-moxa-to-vms

How to configure Moxa to VMS

In this article, we configure Moxa to VMS and how to use Moxa input as alarm input.
VMS supports all Moxa devices which has MXIO supported. 

Step-by-step guide

If you want to change the Moxa IP address; the default IP address is 192.168.127.254; please check the correct IP address in the Moxa manual

By default, there is no password but you can add this if you want

When you know Moxa IP address, open System Manager

Go to the second tab; VMS Servers

Then double click Digital I/O, this opens a new window that shows what Inputs and Output are configured in the system

To add Moxa, you need to click Add I/O driver button

This opens a new window where you can fill in Moxa information

First, you need to select Model moxaiodriver

Give the number of inputs

Give the number of Outputs

Moxa IP-address

And the last password if you have added this

Then click OK

After adding system is updating settings and show Moxa information

In this example, you see that Moxa has 1 input and 1 output. The number in parentheses tells us which is this input or output number in the system

You can also change the name for these inputs and outputs using the Inputs and Outputs tabs

If you want to use this input as Alarm input, you only need to create an alarm

You can create an alarm using that same server where you added this Moxa

Open Alarm and start creating alarm normally but use Trigger this Moxa input which you earlier added to the system

And last press OK to save this alarm

When an alarm is saved to the system you can find it under the Alarm section

Pagination
Previous page
Correct order to stop and start VMS Services
Next page
How to fix error in V7 "No disks configured recorder "Local recorder""