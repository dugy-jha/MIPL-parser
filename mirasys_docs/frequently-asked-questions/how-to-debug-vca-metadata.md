# How to debug VCA Metadata | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/how-to-debug-vca-metadata

How to debug VCA Metadata

If there is need to debug VCA Metadata example to check what system is detecting from video stream etc.

This is possible to do editing MetadataEnrichmentDriverUdp.xml file. Default this file is located C:\Program Files\DVMS\DVR\MetadataEnrichment-folder.

Default MetadataEnrichmentDriverUdp.xml

XML
<Vca>
<version number="3.8.7"/>
<Log>
<!-- Channel numbers to log, -1 = no log (default), 0 = all channels, multiple channels with own channel element  --> <channels>
<channel ChannelNumber="-1">
<OriginalMetadataFilters>
<filter>some original metadata filter text here</filter>
</OriginalMetadataFilters>
<MetadataFilters>
<!-- Filter text for search match. Empty = no search. Text "all" = show all meta data -->
<filter>some metadata filter text here</filter>
</MetadataFilters>
</channel>
</channels>
</Log>
<PerformanceLog>
<!-- LogLevel values: info, warning, error (default) --> <LogLevel> error </LogLevel>
<!-- PerformanceMode values are minutes, zero = not in use (default) --> <PerformanceMode> 0 </PerformanceMode>
<!-- PerformanceLevels values are percents --> <PerformanceLevels error="150"  warning="100" />
</PerformanceLog>
</Vca>


On this file you need edit line 5, where you can put wanted camera number. This can be check via System Manager Hardware section or Cameras section.

After this you need to change lines 7 and 11 to all. This option to show all metadata what is coming originally and how that is formatted to Mirasys Metadata format.

If there is already know what is needed to find, then you can use filters to give text for search match.

When all needed changes are done, you need restart DVRServer service.

After this metadata is included DVRServer log file.

Pagination
Previous page
VCA license page giving error "Local daemon failed to start"
Next page
Device Compatibility Tool