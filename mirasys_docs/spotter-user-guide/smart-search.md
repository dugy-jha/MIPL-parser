# Smart Search | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/smart-search

Smart Search

The Smart Search plugin is used for Licence Plate Recognition (LPR), Face Recognition (FR), Similarity Search for people, and Object Recognition (OR) search. For live search, please use the Smart Recognition plugin.

All recognition smart searches require licenses for each recognition stream.

Smart Search plugin for LPR, FR, OR, and similarity searching

You can use smart search by selecting it under Search > Smart Search in Spotter, or by clicking the Smart Search plugin under plugins in the left-hand side menu.





Smart Search plugin is opened and it can be used to search for detection events that have occurred in the past. Found results are shown in results list with detection and identity details.

See the sub-pages of this page for how to search for FR, LPR, and Object recognition events, as well as how to do a similarity search.

To allow more space for the list viewing, it is possible to click the arrow at the top-right corner of the search criteria. The space occupied by the video, and the list can also be adjusted by clicking and dragging.

Search parameters

There are several search parameters that can be used to define when, where, and what is being searched.

Time - Start time and optional search end time

Detection type - Faces, License Plates or Attributes.

Cameras - All cameras or selected cameras.

Object - Faces, license plate numbers, attributes or search for similar faces.

Identity - All, unknown or selected identities.

List - All, unknown or selected identity lists.

Search for - Free text search uses detected plate numbers and identity fields.

Result count - Maximum number of result rows.

After selecting all appropriate search parameters, the search can be started by clicking the Search button.

Search results

Search results are shown in the recognition event list with the following fields.

Time - Time and date of the recognition.

Camera - Name of the camera and thumbnail of the full image.

Detection - Face or license plate recognition event thumbnail, recognized information, and recognition confidence value.

Identity - Matched identity information.

List - Identity list information that the matched identity belongs to.

List content can be arranged by field type by clicking the list header.

Additional Options
Detection window

Under settings, you can select the time added before and after detection.

Add to export

The selected event can be added to the storyboard or to clip export. Recognition event pre and post-record time can be adjusted from the drop-down settings button.

Save to PDF file

Search results with all recognition details can be saved to a PDF report file. The file can be saved locally or to Storage Locker. Notice that this depends on user role settings.

Add face or license plate to identity

Found license plate or face can be added to a new identity or existing identity. These functionalities are only possible if the user is authorized to change the identity information. By clicking the add new identity or add to existing identity buttons, the Smart List Management plugin is opened. See more information in the Smart List Management plugin documentation.

Quick search

Found license plate or face can be used for a more detailed search. By clicking the quick search button, search parameters are updated with the selected recognition event details to easily perform a search for found faces and license plates.




Pagination
Previous page
Smart Recognition
Next page
FR and LPR detection events