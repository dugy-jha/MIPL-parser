# Grafana Database configuration | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/grafana-database-configuration

Grafana Database configuration

Grafana will need access to the VMS DvmsData, RecorderDB and WDContext databases running on the Master server.

Data source configuration

Before importing Mirasys Dashboards to Grafana you need enable communication between Microsoft SQL and Grafana.

You can add data source connection automatically or manual way and for authentication you can use Windows authentication or create own account for this in Microsoft SQL.

Data source configuration with YAML file and Windows Authentication

Mirasys Dashboards installation package include DvmsData.yaml file which automatically create database access to Grafana. Before using this file open this using example Notepad and change correct Windows username and password on that file. Then you can copy file DvmsData.yaml into C:\Program Files\GrafanaLabs\grafana\conf\provisioning\datasources and after that restart the Grafana service.

When Grafana is started you can find this database connection under Grafana configuration section. Login to Grafana and go to Configuration section. Under this you can find configured data sources on this system.

You can test this connection opening this data source and scrolling down. There is green Test button. Click that and if everything is working you should see message “Database Connection OK”.

Data sources which are created using YAML file can’t be delete in interface. If you want to delete that kind of data source you need create file which you put same location where you put this creation file. More information here https://grafana.com/docs/administration/provisioning/ .

Manually configure data source and use Windows Authentication

Login to Grafana and open Configuration section. Under there you can find Data Sources. In this section you can configure data source connection to Microsoft SQL.

On that section click Add data source.

This will open new section where you need select what kind of database you are going to use. Select Microsoft SQL by clicking it.

This will open new section where you need fill these next details

Name

MSSQL Connection

Host

Database

User (example .\dvr)

Password

Encrypt

Connection limits

Max open

Max idle

Max lifetime

MSSQL Details

When you have filled information this data source you can test it clicking Save and Test. If everything is working you should see message “Database Connection OK”.

Then you can go back clicking Back.

Pagination
Previous page
Login Grafana
Next page
Importing Mirasys dashboards