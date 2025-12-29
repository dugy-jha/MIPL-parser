# Spotter can't connect to Smart Event Queue data | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/spotter-can-t-connect-to-smart-event-queue-data

Spotter can't connect to Smart Event Queue data

Some cases is possible that Spotter don’t show Smart Event Queue data on Spotter. These are example Smart Recognition plugin live license plates or faces.

On default when you are installing Smart FR, Smart LPR or Smart List Management services, these are registered to Master server using DNS name of that server. Similar issue can be happening when you open List Management settings via System Manager and you get error that settings opening fails.

If this happens, there is option to check on Spotter Client log if there is communication error related to this.

ERROR EqConnection.Connect [10] - Connect to EQ TESTPC2:5672 error!
ERROR EqConnection.Connect [13] - Connect to EQ TESTPC2:5672 error!
ERROR EqConnection.Connect [54] - Connect to EQ TESTPC2:5672 error!


To fix this there is are few different options.

Option 1

Setup DNS on network and check then that communication is working correctly.

Option 2

Edit client hosts file and write there manually IP-address and DNS name of server.

Default location for hosts file is C:\Windows\System32\Drivers\etc\hosts.

Option 3

Third option is that you edit Smart FR, Smart LPR and Smart LM services to register using server IP-address via service.json file.

Default location is under these services installation folder.

C:\Program Files\DVMS\AdvLmService
C:\Program Files\DVMS\AdvFrService
C:\Program Files\DVMS\AdvLprService

There you can find file service.json.

Example service.json file.

{
  "ServiceSettings": {
    "SmAddress": "127.0.0.1:8082",
    "ServiceAddress": "TESTPC1:8089",
    "ServiceId": "dc28241a-365b-4882-80df-35583c9a67ec",
    "ServiceType": "ListManagement",
    "KeepAliveIntervalSec": 60
  }
}


Via this file you can edit ServiceAddress section. This is name which service use to register VMS Master server. When you change this to example

"ServiceAddress": "192.168.1.101:8089",


And save this file and restart service. This make new connection to VMS Master and register this service using ServiceAddress name, on this case using IP-address.

Pagination
Previous page
Spotter freezes when using machine with two GPU's (Integrated and External)
Next page
Opening multiple systems on one Spotter client