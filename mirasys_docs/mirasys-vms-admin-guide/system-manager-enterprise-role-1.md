# System Manager Enterprise role | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.8/system-manager-enterprise-role-1

System Manager Enterprise role

It is possible to set explicit permissions for the system manager for different user groups.
This allows, for instance, implementing functionality for allowing different user groups for hardware maintenance and user administration, which is helpful for large scale systems.
To enable the functionality - check the "System manager enterprise role" tickbox for the user group and click the "wrench" icon to edit the details for this group.

System

The System tab permissions can be enabled or disabled for a user group, disabling, for example, System settings hides system settings for all users in the user group

VMS Servers

The VMS servers tab allows permissions for a user group to View, Add, Delete and edit either all or only selected VMS Servers to be noted: if "Edit selected" is checked, the shuttle box below enables defining which specific servers this user group has access to.

This is convenient in large installations if specific user groups are working with specific servers (e.g. if there are separate maintenance groups for different sites - and the recording servers are site-specific.)

Profiles

The Profiles tab/permissions that can be set for the user group:

“Edit selected” enables you to decide to which profiles the functionality applies (similar to the "servers" permission configuration).

Users

The user tab/permissions that can be set for the user group:

Edit all or Edit selected must be enabled for a user group for users to add and/or delete (these options get automatically disabled if Edit all or Edit selected is disabled).

This functionality affects VMS Servers, Profiles and Users tabs

Pagination
Previous page
User Roles
Next page
Monitoring role