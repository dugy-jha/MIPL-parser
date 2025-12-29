# Daylight Savings Time (DST) | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/daylight-savings-time-dst

Daylight Savings Time (DST)

This guide explains how to handle potential issues caused by the Daylight Saving Time (DST) transitions when using our video management software (VMS). It also provides instructions on retrieving recorded footage during DST transitions, particularly the first hour after the time change.

Introduction

Daylight Saving Time involves adjusting clocks forward by one hour in the spring ("spring forward") and back by one hour in the fall ("fall back"). The specific time of the change varies across countries and regions, but the general principle remains the same globally.

Our VMS stores footage using Coordinated Universal Time (UTC).

UTC is not affected by DST adjustments. This ensures that no recorded material is lost or duplicated.

Impact of DST on Video Surveillance Systems

DST transitions can cause confusion when reviewing footage because the local time on the system changes, even though UTC remains consistent.

While no footage is lost or duplicated in UTC, the change in local time may affect how it is presented to users:

The skipped hour may lead users to think that footage is missing.

The repeated hour may cause confusion, as it creates two sets of footage with the same local timestamp.

Spring Forward

During the spring DST transition, clocks are moved forward by one hour, skipping over a specific hour. Since our system operates on UTC, this hour is not recorded because it effectively does not exist in the local time.

No video will be recorded for the hour that is skipped during the spring DST transition (the specific hour depends on the local time zone).

Users may perceive missing footage, but the skipped hour simply does not exist in the system's local time.

Material Retrieval During Spring Forward

In the case of spring forward, understand that the skipped hour does not exist in the system. The last available footage before the time change will be just before the time changes to summertime, and the next available footage will be an hour later. There is no footage to retrieve for the skipped hour.

Spring Forward

The specific hour that is skipped will not have any footage. This hour will vary depending on the time zone where the system is located.

Retrieving recordings: The last available footage before the time change will be just before the skipped hour, and the next available footage will resume after the skipped hour.

Fall Back

In the fall, clocks are moved back by one hour, repeating a specific hour. Because our system operates in UTC, this means that two separate sets of footage will be recorded for the repeated hour.

When using the Spotter application time selection on duplicated hour, all time requests are converted to the second hour. This means that when using the Spotter timeline, the playback plays the materials and does to search from the second hour.

To access the materials for the first hour, operators can start the playback forward from the hour before the Daylights Savings time shift or start the backward playback from the hour of the Daylight Savings time shift time.

Instructions for Material Retrieval during Fall Back

For the Fall Back transition, two separate hours will be recorded. These two separate hours can be differentiated by the system’s timestamp. You can ensure that the correct hour is being accessed by reviewing the system log or watermark, which indicates the actual time of the recording.

Review the system logs and event logs to identify the exact times when the system adjusted its clock.

When using the Spotter application time selection on duplicated hour, all time requests are converted to the second hour. This means that when using the Spotter timeline, the playback plays the materials and does to search from the second hour.

To access the materials for the first hour, operators can start the playback forward from the hour before the Daylights Savings time shift or start the backward playback from the hour of the Daylight Savings time shift time.

Fall Back

The specific hour will be recorded twice, once before the clock is adjusted back and once after.

Retrieving recordings: Distinguishing Between Two Recorded Hours. Review the system log or watermark to differentiate between the two sets of footage from the repeated hour.

When using the Spotter application for playback, note that all time requests during the duplicated hour default to the second occurrence of that hour.

To retrieve footage from the first occurrence of the duplicated hour, you can:

Start playback from the hour before the DST adjustment.

Use backward playback starting from the hour after the DST change.

Best Practices for Handling DST Transitions in Mirasys VMS

To minimize confusion and ensure that the system behaves as expected during DST transitions, it is important to follow these best practices:

Notify all operators and users about the upcoming DST change and explain its impact on recorded footage, particularly the skipped hour during spring forward and the duplicated hour during fall back.

Ensure that all system components, including servers, cameras, and associated devices, are synchronized with an accurate time source to prevent time drift during the transition.

For time-stamped footage, prepare operators for potential confusion in these timestamps during and after the transition.

After the DST change, check the footage during the transition period. Ensure that recordings from before and after the time change are intact and accessible.

In the case of fall back, be aware that two sets of footage exist for the same hour. Ensure operators know how to differentiate between the two periods of recording.

For systems that trigger based on motion or alarms, review any events that occurred during the time change to ensure they were recorded properly.

Pagination
Previous page
Use of Multiple Alarm Monitors
Next page
System Monitoring