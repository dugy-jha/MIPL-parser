# Countdown I/O | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/countdown-i-o

Countdown I/O

With Countdown I/O, it is possible to create actions based on whether some events happen or do not happen at a defined period.

When a new Countdown I/O is created in System Manager, it automatically creates 4 inputs and 4 outputs.

Countdown I/O has two basic modes. The first two input/output pairs are of type 1, and the last two pairs are of type 2.

A license controls logical IO and countdown IO. If the license is not present, creating new IO will fail.

Event Duration Exceeded Mode (Type 1)

Firstly, it is possible to trigger an alarm if some event takes longer than the planned duration. 

For example, let’s say the time is 10 seconds. If output one is triggered and stays active for less than the defined duration, there is no alarm.

If the output is triggered and stays active for longer than the defined duration, there is an alarm.

When creating a new Countdown I/O, the first two input-output pair is of this type.

Expected Trigger Mode (Type 2)

Secondly, it is possible to trigger an alarm if an expected pulse is not received inside the defined time. 

For example, the time is 10 seconds, and we expect the regular operation to get pulses from output 3 every 2-3 seconds.

When the pulse is missing for longer than 10 seconds, the input state is changed to active. It stays active until the next output trigger is received.

When creating a new Countdown I/O, the last input-output pair is of this type.

Pagination
Previous page
Logical I/O
Next page
Scheduled IO