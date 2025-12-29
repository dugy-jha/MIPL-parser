# List Management settings | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/list-management-settings

List Management settings

List management makes it possible to define identities and lists so that the allowed or not allowed identities can be defined.

The settings define and manage identity and list management settings. Settings allow you to:

Add, edit, and delete identities containing license plates and face images

Add, edit, and delete lists and manage list content

Import and export lists and identities

Configure LPR and FR event database retention limits

Enable and define integration and its settings

The System manager application provides several dialogs to access and modify list management service data and settings. The dialogs can be found in the “System settings“ section.

Integration requires LPR and FR integration license.

List Management Settings

How to open the List Management Settings dialog:

Go to the System tab

Under System settings, double-click the List Management Settings tree node, as shown in the picture below:

3. When you double-click List Management Settings he dialog loads request the settings from the list management service and display them if successful. If loading fails, the error message is displayed to the user, and the dialog is closed.

List Management Settings dialog

In the dialog, you can find the following tabs:

Identities - list of identities and their settings

Lists - identity lists and their settings

Import/Export - import/export functionality to restore/save list management data to CSV text format

Database Settings - parameters related to the list management service database

Integration Settings - integration enabling and integration settings

All changes you make in these dialog tabs can be saved by clicking the OK button.

If you do not need to keep the changes, you can close the dialog with the Close or the Cancel button.

Below you can find a detailed description of each tab.

Identities tab

In the “Identities” tab you can perform operations with identities:

Identities tab

Identity selection is done using the left mouse button. If you must select multiple identities (multiple rows in the list), you can use the left mouse button + Ctrl/Shift keys. With multiple selections, you can set selected identities to the "active" or "not active" state by clicking the checkboxes in the “Active“ column.

Above the list of identities, you can find the Search field: when you type here, the list of identities is automatically filtered if the text is found in identity names or plates.

You can add and remove selected identities with the Add and Remove buttons below the identity list.

You can see detailed information about identity in the Identity Details area, but all these fields are read-only. To modify the selected identity, you can click the Modify button or double-click it with the mouse button.

When you add or modify identity, the following dialog is shown:

Add/modify identity dialog

You can change any field data or add/remove identity face images or vehicles (license plates).

To add a face image, click the “Add a new face image” button, and the following dialog will open:

Add Face Image dialog

Several face images can be defined for an identity. All face images will be used when doing identity face matching, so using multiple face images for an identity, may increase the face detection confidence

You can write a face image name and select a face image file here. After file selection, the image will be loaded, and the feature vector data of the image will be calculated.

To calculate the face feature vector, at least one face recognition service must be started and registered in VMS

To remove a face image, you need to select it in the combo box and click the Remove Selected face image button.

Set face image as default

One face image is the default, which is used as a thumbnail in all plugins and identity lists. To set the face image as the default, you need to select the face image in the combo box and click on the Set selected face image as default button:

Set selected face image as default
Add or remove vehicles

You can add or remove vehicles. To add a vehicle, click the Add a new vehicle button, and the following dialog will open:

Add Vehicle dialog

In the Add Vehicle dialog, you can type the license plate number, area code, manufacturer, model, and vehicle color. To remove a vehicle, you need to select it in the combo box and click the Remove selected vehicle button.

Lists tab

In the Lists tab you can perform operations with identity lists:

Lists tab

List selection is done using the left mouse button. If you need to select multiple lists (multiple rows), then you can use the left mouse button + Ctrl/Shift keys. With multiple selections, you can set selected lists to the active or not active state by clicking the checkboxes in the Active column.

You can add and remove selected lists with the Add and Remove buttons below the lists.

To modify the selected identity list, you can click the Modify button or double-click it with the mouse button.

When you add or modify the identity list, the following dialog is shown:

Add/Modify List Settings dialog

You can move identities to the list or remove them from the list, define the name of the list, and color.

Import/Export tab

In the "Import/Export" tab you can import list management data from a CSV file or export list management data to a CSV file:

Import/Export tab
Import parameters

The following parameters must be set for the import process:

File path - path to the CSV file which contains list management data

Import type - “Identities only“ or “Identities and lists“

CSV delimiter - “Comma” or “Semicolon“

Items with the same identifier - “Skip“ them, “Overwrite“ or “Create new“ identifier for them

When the correct parameters are selected, the Import data from file button is active, and users can start the import process. During the process, users will see the progress and result of the import.

Export parameters

The following parameters must be set for the export process:

Folder path - path to the folder where list management data will be exported and where the CSV file will be created

Export type - “Identities only“ or “Identities and lists“

CSV delimiter - “Comma” or “Semicolon“

When the correct parameters are selected, the “Export data to file“ button is active, and users can start the export process. During the process, users will see the progress and result of the export.

Database Settings tab

In the Database Settings tab, you can setup database settings for the list management service:

Database Settings tab
Integration Settings tab

In the Integration Settings tab, you can setup integration settings for the list management service:

Integration Settings tab

Here you can define settings for the event queue and enable/disable integration settings. The tab is not visible if the license does not enable list management integration.

List management data update notification

If list management data has been changed in another application, the System Manager will receive an event with updated information and display the following message:

Data update warning

When you click the OK button of the message dialog, all settings dialogs will be closed to reload data from the list management service. All changes that were not saved will be lost.

Pagination
Previous page
Storage Locker Settings
Next page
Backup