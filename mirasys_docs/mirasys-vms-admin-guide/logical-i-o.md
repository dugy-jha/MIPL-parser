# Logical I/O | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/logical-i-o

Logical I/O

With Logical I/O, it is possible to create actions based on the OR and AND operators.

The I/O driver emulates an external I/O that is connected to itself. Example:

For example, if the customer wants to confirm that an Automatic Number Plate Recognition (ANPR) event is triggered when a car is in front of the camera, the Logical I/O can be used to create a “rule” that results in action only when VCA detects a car, AND at the same time, there is an ANPR read event.

Another example could be that an entry “gate” with two doors only allows the second door to be opened when the first one is closed.

Logical I/O can be operated from the same interface as the rest of the Digital I/O in System Manager.

A license controls logical IO and countdown IO. If the license is not present, creating new IO will fail.

When a new Logical I/O is being added, the first option in the dialogue is how many output states are used as operands in the AND/OR decision making.

The minimum number is two, and the maximum is 32.

 

All Logical I/Os will automatically generate four inputs that can be used. 

 

Input

	

Type




1

	

OR




2

	

AND




3

	

HOLD AND




4

	

PULSE AND

The following sections will describe the different inputs in more detail by using the below example:

The example has 2 outputs that are the operands. These can be seen in the IO list as outputs 3 and 4.

The automatically created 4 inputs are seen in the list as inputs 5,6,7 and 8.

“OR” Input

The first input that the Logical I/O will generate is OR signal. If any of the outputs are on, the OR input will be turned on.

In our example, input 5 is the OR signal. If either output 3 OR output 4 are turned on, input 5 will be turned on as a result.

Input will remain on as long as any of the outputs remains on. (Unless pulse mode is selected, see below for details)

“AND” Input

The second input is the AND signal. If all the outputs are on at the same time, the AND input will be turned on. In our example, if both outputs 3 and 4 are on simultaneously, input 6 will be turned on.

Input will remain on as long as all of the outputs remain on. (Unless pulse mode is selected, see below for details)

“HOLD AND” Input

HOLD AND input become active if all the outputs are active simultaneously, and the time from the first activation to the last activation is less than the time defined in the HOLD AND wait time slider.

In our example, if output 3 is turned on, and then output 4 is turned on inside 10 seconds, input 7 will become active.

Input will remain on as long as all of the outputs remain on. (Unless pulse mode is selected, see below for details

“PULSE AND” Input

PULSE AND input will become active if all outputs have been active within a specified time.

In our example, if output 3 has been active inside 10 seconds, and output 4 becomes active, then input 8 will be turned on.

Input 8 remains until the specified time has elapsed from the oldest activating output (unless pulse mode is selected, see below for details).

In our example, when 10 seconds have elapsed from output 3 activation, input 8 will be turned off.

Pulse Mode For Inputs

For each of the four inputs, it is possible to define pulse mode to be in use. 

and

The pulse duration can also be adjusted.

If the pulse mode is in use, the input will turn off after the set pulse duration. 

If in our example, we would set the AND input to be in pulse mode like this:

It would mean behaviour like this:

Pagination
Previous page
LoopBack I/O
Next page
Countdown I/O