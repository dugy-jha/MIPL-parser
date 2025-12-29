# Smart Recognition | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/smart-recognition

Smart Recognition

The Smart Recognition plugin is a Spotter plugin that shows Face Recognition (FR), License Plate Recognition (LPR), and Object Recognition (OR) events.

Object, license plate and face recognition requires license for each recognition stream.

Open the plugin and view live detection events

Click the Spotter plugin toolbar item to open the plugin:

When you open the plugin, it displays all live events.


Select if you want to filter by LPR, FR, and OR under Where. This will determine which cameras are displayed for selection.

Select which cameras to use under Where to narrow down the events displayed.

Under What / Who the tabs for the select services and cameras will be enabled depending on the services and cameras selected under Where. All selections under these tabs will apply when applying the filter.

Click Apply.

For example, if you are selecting both OR and LPR services and cameras, the attributes selected for vehicles in the OR tab and the LPR tab will be applied when filtering out the events when you click Apply. The FR tab will be disabled.

What / Who Filtering
Faces

Filter recognition events based on Identity, and List (the identity list information that the matched identity belongs to, if applicable).

License plates

Filter recognition events based on Identity, and List (the identity list information that the matched identity belongs to, if applicable).

Attributes - People

Select the attributes for object recognition to find people based on upper or lower body wear color and whether they are wearing headwear or carrying a bag. To add filtering attributes, click Add attribute. You can, for example, filter out live events to find a person with a white top, blue trousers, wearing a hat, and carrying a bag by adding attributes.

You can select from 4 types of clothing/accessories:

Hat

Top

Bottom

Bag

For the Top attribute, you can select the following colors:

Black

White

Gray

Red

Yellow

Blue

Green

Other*

For the Bottom attribute, you can select the following colors:

Black

White

Gray

Blue

Brown

Green

Other*

*Other corresponds to colors that are not on the list, any patterns in clothing or colors that can be tricky to fit into one of the categories.

It is not possible to specify the color of headwear or bag.

Attributes - Vehicles

Filter events to see vehicles based on type and colors using our Smart Search. When you select Attributes followed by Vehicles, you can select from 6 vehicle types for detection:

Car

Bus

Van

Truck

Motorcycle

Bicycle

For every attribute, except motorcycle and bicycle, you can also select colors to search for:

Black

White

Gray

Blue

Green

Red

Orange

Yellow

Brown

Other*

*Other corresponds to colors not on the list and vehicles with multiple colors or patterns can also be found under others.

Reset filters

If you want to reset the filtering, click Reset.

Customizable UI

To allow more space for the list viewing, it is possible to click the arrow at the top-right corner of the filtering criteria. The space occupied by the video, and the list can also be adjusted by clicking and dragging.

Export

The selected event can be added to the storyboard or to clip export. Recognition event pre and post-record time can be adjusted from the drop-down settings button.

Add face or license plate to identity

A recognized license plate or face can be added to a new identity or existing identity. These functionalities are only possible if the user is authorized to change the identity information. By clicking the add new identity or add to existing identity buttons, the Smart List Management plugin is opened. See more information in the Smart List Management plugin documentation.

Quick search

Recognized license plates or faces can be searched by using the Smart Search plugin. In the Smart Recognition plugin, there is a quick search button that opens the Smart Search plugin. The recognized license plate or face information from selected recognition events is filled up automatically to easily perform a search for recognized faces and license plates.







Pagination
Previous page
Spotter Alarm Popup
Next page
Smart Search