# Double-knock Rule | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/double-knock-rule

Double-knock Rule

The “double-knock” logical rule triggers when an object enters a zone which had previously entered another defined, zone within a set period of time. The interval on the Previous rule decides how much time can elapse between the object entering the first and second zone. The graph for a double-knock logical rule is as follows:

The rule may be interpreted as follows: “An object is in Zone 2, and was previously in Zone 1 in the last 1000 milliseconds”. This rule can be used as a robust way to detect entry into an area. Since the object has to enter two zones in a specific order, it has the ability to eliminate false positives that may arise from a simple Presence rule.

Pagination
Previous page
Combined Rule Examples
Next page
Presence in A or B