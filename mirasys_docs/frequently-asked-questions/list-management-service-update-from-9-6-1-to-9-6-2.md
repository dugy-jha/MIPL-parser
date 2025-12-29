# List Management Service update from 9.6.1 to 9.6.2 fails | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/list-management-service-update-from-9-6-1-to-9-6-2

List Management Service update from 9.6.1 to 9.6.2 fails

In some special cases, an update from List Management Service 9.6.1 to 9.6.2 fails.

Symptoms are that you may get an error that the service failed to start.

On the log side, you can see an error that database migration fails.

Mirasys.LmsDb.Repository.LmsRepository[0]
LMS db migrate failed!
Npgsql.PostgresException (0x80004005): 23503: insert or update on table "face_images" violates foreign key constraint "fk_face_images_identities_identity_id"


This happens when List Management Service 9.6.1 is installed on the system and identification, which includes face image, is removed.

On List Management Service (Version 9.6.1), when you delete identification, this does not delete the face image with that deletion. This causes installation failure when you try to update the current version to a newer installation.

On the List Management Service (Version 9.6.2) side, this is fixed, and now, when you delete identification, this also deletes face images or images that are related to that identification.

How to fix the database

To fix this issue, you need to open pgAdmin, which is a PostgreSQL management tool. This is installed with List Management Service, and you can find this tool on the Windows Start Menu and under Applications.

When you open the tool, it will ask for the password. You filled in this password when you made the List Management Service installation. The default password is postgres.

When pgAdmin is opened, go to Browser, open LMS database, and go to Tables.

You may need to give the password again when opening the database and Tables.

In the Tables section, we are interested only in face_images and identities tables.

Right-click the identities table and open All Rows.

This opens a new window on the right side of the pgAdmin tool and shows all identities on this table.

In this table, you need to check current identities and ID numbers. In the example image, we have four identities, and their ID’s are 1, 2, 7 and 11.

Now, you need to open the face_image table the same way you opened identities. Right-click the face_image table and open All Raws.

This opens a new window on the right side of the pgAdmin tool and shows all face_image on this table.

On this Data Output field, you need to scroll to the horizontal end of this and find the identity_id row.

Earlier, we checked identities table IDs and took current IDs. Now, there is a need to compare these IDs on this row. If there is any extra ID on this row, you can delete this image from the table.

Select the wanted line and delete it.

Repeat this all on those lines that have this extra ID included.

When this is done, you can try the List Management Service 9.6.2 installation again, and it should go trough normally.

If there are still problems, please contact Mirasys Support.

Pagination
Previous page
VMS Performance Counters
Next page
How to fix SQL login error