# VCA Classification | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/vca-classification

VCA Classification

VCAcore can define a moving objects class using either its Deep Learning models or by using properties extracted from an object in a calibrated scene.

Both methods of classification are applied through the use of filters in the rules interface.

Classification filters allow an object, which has triggered a rule, to be evaluated against its predicted class and filtered out if needed.

Object classification

Once a camera view has been calibrated, each detected object in that view will have a number of properties extracted including object area and speed.

VCAserver's object classification performs classification by comparing these properties to a set of configurable object classifiers.

VCAserver comes pre-loaded with the most common object classifiers, and in most cases these will not need to be modified.




Pagination
Previous page
VCA Calibration
Next page
VCA Burnt-in Annotation