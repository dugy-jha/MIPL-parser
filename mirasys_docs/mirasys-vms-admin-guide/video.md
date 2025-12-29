# Video | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/video

Video

When adding an IP camera, the following search modes are available.

All drivers: Automatic search with all drivers. The system will attempt to use all available drivers. The mode option combo-box is disabled.

Selected drivers: Automatic search with specific drivers only. The system will use only the drivers specified via the Selected Drivers dialogue during the automatic search.

The additional combo box will show all drivers that are currently selected. A user may use all of them (using the “All” option) or select only one driver.

Currently active drivers: Search the camera using all drivers who are currently used. If this option is selected, the system will use only drivers currently used for already added cameras.

For example, if we have Sony and Axis cameras subscribed, the search will be done by Sony and Axis drivers only.

The mode option combo-box will contain a list of used drivers if the user wants to use one of them and an “All” option for using all drivers from this list for searching.

Driver: Add a camera using a specific driver. The system will use only the specific driver for search.

The mode option combo-box will contain a list of all installed driver names to search.

If a search with specified drivers fails, the system will prompt whether the user wishes to search using all drivers.

The driver currently used for the search also should be excluded.

Camera model: Add camera by model name. This mode is used for adding a camera by using an older capture driver using pre-defined capabilities from the driver configuration XML file.

The mode option combo box will contain a list of available models. 

The Selected drivers -mode will be selected by default for adding the new camera for the first time.

Next time the dialogue is opened, the system will remember the previous model and driver selection to allow the user to add similar cameras faster.
Opening the existing camera using the Modify button will show a dialogue with the Currently active drivers search mode and driver name in mode option combo-box (except cameras added by mod, el of course).
The system will not store last used options for modifying cases because the options will be available for adding cameras only

Pagination
Previous page
Hardware
Next page
Add device