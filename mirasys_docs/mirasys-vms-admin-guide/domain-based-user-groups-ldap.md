# Domain Based User Groups (Active Directory) | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/domain-based-user-groups-ldap

Domain Based User Groups (Active Directory)
Domain Based User Groups (LDAP)

The system supports domain-level user rights integration (Microsoft Active Directory, LDAP), enabling users to be synchronized from domain groups.

Domain-based users can log into the VMS system with their domain usernames and passwords.

By default, user group rights are synchronized with their parent domain every 30 minutes.

Please contact your system supplier if f you need to change the default interval.

This feature requires a license update.

Adding a new domain-based user group to the system

Click Import User Groups from an external source in the upper-left corner of the Users tab
The Master Server needs to be connected to a domain for the button to be displayed.
If the server is not connected to a domain, the button is not visible.

Type the name of the domain into the Domain name dialogue box.

Select whether to get all user groups or to search for specific groups.
If you want to search specific groups by name, you can add a search criterion based on the text string being equal to the group name, contained in the group name, or the group name starting or ending in the text string.

4. Select whether to skip or include open user groups.

5. Select whether to clear or keep previous search results.

6. Enable Use secure(SSL) connection. If needed

7. Click Ok.

8. In the Import user groups window, select the user groups you wish to import from the domain.

9. Click Ok to import the selected groups.

10. Edit the imported user groups to set their user roles as instructed below.

Pagination
Previous page
Creating a customer-specific User Group
Next page
Active hours - User group access schedule