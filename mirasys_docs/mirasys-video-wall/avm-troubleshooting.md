# AVM Troubleshooting | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-video-wall/Video-Wall-Guide/avm-troubleshooting

AVM Troubleshooting
No connection to the AVM DS 

 Spotter running and logged in at another end?

 IP address/monitor number correct in the setting?

 Firewall on?

 Ports 8084 / other opened at all OC/DS/all windows users

The maximum number of virtual displays in AVM Display Server reached

Solution: check the number of spotter windows in target DS. Close Unnecessary windows and try again

Check OC monitor configuration: do you have any weird IP address Monitor number

Check the DS monitor configuration. Do you have screens incorrect order and resolution, and upper edges aligned?

Is the monitor on and connected?

”Black images” or no images in AVM DS. 

Do you have the correct profile selected?

AVM OC and AVM DS need to have the same profile

No images in the AVM OC

Do you have reference images in the VMS server camera settings?

An alternative way to automatically start Spotter on Windows startup

Open Windows Task Scheduler

Click Create Basic Task

3. Enter the name of the task

4. Click Next

5. Select When I log on

6. Click Next

7. Select Start a program

8. Click Next

On default VAU.exe is installed under Program Files\DVMS\VAU

Change this patch is installation is done somewhere else

9. Browse the Spotter installation location and select VAU.exe

10. Enter -c spotter.xml -s 127.0.0.1 to the Add arguments(optional) field

11. Click Next

12. Enable Open the Properties dialog for this task when I click Finish

13. Click Finish

14. Enable Run only when user is logged on

15. Open Triggers tab

16. Click Edit

17. Enable Delay task for: and set value 1 minute

18. Click OK

Windows user automatic login

Open Run command box

Type netplwiz

Select/click wanted user, example DVR

Untick Users must enter a use name and password to use this computer

You get prompt where to fill this user name password

Now Windows login automatically in using this user

Pagination
Previous page
AVM Operator Console