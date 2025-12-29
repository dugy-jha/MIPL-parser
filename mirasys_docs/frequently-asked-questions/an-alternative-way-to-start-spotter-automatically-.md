# An alternative way to start Spotter automatically on Windows startup | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/an-alternative-way-to-start-spotter-automatically-

An alternative way to start Spotter automatically on Windows startup

Open Windows Task Scheduler

Click Create Basic Task

Enter the name of the task

Click Next

Select When I log on

Click Next

Select Start a program

Click Next

Browse the Spotter installation location and select VAU.exe

On default VAU.exe is installed under Program Files\DVMS\VAU

Change this patch is installation is done somewhere else

Enter -c spotter.xml -s 127.0.0.1 to the Add arguments(optional) field

Click Next

Enable Open the Properties dialog for this task when I click Finish

Click Finish

Enable Run only when user is logged on

Open Triggers tab

Click Edit

Enable Delay task for: and set value 1 minute

Click OK

Windows user automatic login

Open Run command box

Type netplwiz

Select/click wanted user, example DVR

Untick Users must enter a use name and password to use this computer

You get prompt where to fill this user name password

Now Windows login automatically in using this user

Pagination
Previous page
Exporting H.265 material give error "This video format is not supported in selected file format"
Next page
How to change Spotter time format