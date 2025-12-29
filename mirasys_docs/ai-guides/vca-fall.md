# VCA - Fall | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/vca-fall

VCA - Fall

The fall rule detects when a object classified as a Person, by the Deep Learning People Tracker, is in the fallen state.

When the Fall rule is added to a channel configuration, the fall detection algorithm begins to run in the background which will have a GPU overhead. Currently this rule is only available when using the Deep Learning People Tracker.

Graphical View
Form View
Configuration
Use table header to sort columns

Property

	

Description

	

Default Value




Name

	

A user-specified name for this rule

	

“Fall #”




Zone

	

The zone this rule is associated with

	

None




Duration

	

Period of time a object must have been fallen before the rule triggers

	

1 to 60 seconds




Confidence Threshold

	

The algorithm confidence (as a percentage) required to trigger the rule

	




0




Can Trigger Actions

	

The algorithm confidence (as a percentage) required to trigger the rule

	

Active

Pagination
Previous page
VCA - Dwell
Next page
VCA - Presence