# Plugin installation | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/plugin-installation

Plugin installation

Mirasys Dashboards use few plugins providing information. Both plugins are included in installation package or they can be download separately from Grafana Plugins site (https://grafana.com/grafana/plugins ).

There is two way install plugin. First way is use Grafana own command line tool if server has internet connection.

Default location for this tool is C:\Program Files\GrafanaLabs\grafana\bin. Because Mirasys Dashboards use two different plugins Multistat and Grafana Image Renderer. These can be installed that you open command prompt or PowerShell as administrative rights and run commands

grafana-cli plugins install michaeldmoore-multistat-panel

and

grafana-cli plugins install grafana-image-renderer

After plugin installation you need restart Grafana service in Windows Service.

Second way install plugins is extract plugin zip file to Grafana Plugins-folder. Default location for this folder is C:\Program Files\GrafanaLabs\grafana\data\plugins.

After plugin extraction you need restart Grafana service in Windows Service.

After this you can found plugins under Plugins section.

Pagination
Previous page
Install Mirasys Reporting Grafana
Next page
Login Grafana