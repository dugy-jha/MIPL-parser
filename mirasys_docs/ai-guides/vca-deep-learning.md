# VCA - Deep-Learning Filter | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/vca-deep-learning

VCA - Deep-Learning Filter

VCAserver also supports classification through the use of the deep learning filter. In this case an object, which has triggered a rule, can be analyzed using the deep learning filter and a predicted class and confidence level returned. The available object classes are defined by the model.

On VCAserver the Deep Learning Filter can use GPU acceleration, see Deep Learning Requirements for hardware requirements.

Without GPU acceleration the deep learning filter will use the CPU, enabling the deep learning filter on multiple channels which are generating a high volume of events, (more than 1 per second) may result in poor performance of the system and is not advised.




Each of the possible object classes has additional parameters:

Allowed: Whether this object type will be allowed to pass through the filter. If this is unchecked, any objects classified as this type will not trigger any actions.

Confidence Threshold: A value (0.0 - 1.0) representing the minimum confidence level required for classification. Any objects with a lower classification score than this minimum value will be filtered out and will not trigger any actions.

Pagination
Previous page
VCA - Object display
Next page
VCA - Filters