# Spotterin käyttäminen useista verkoista | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-k-ytt-ohje/V9.9/spotterin-kayttaminen-useista-verkoista

Spotterin käyttäminen useista verkoista

Jos käyttäjä käyttää Spotteria useista verkoista, DNS-nimeä on käytettävä VMS-palvelimen staattisen IP-osoitteen sijaan.

Host-tiedoston muokkaaminen

Tarkista tietokoneen nimi

Selaa C:\Windows\System32\drivers\etc

Avaa host-tiedosto tekstieditorilla

Sinun on ehkä suoritettava Notepad järjestelmänvalvojan käyttöoikeuksilla

Lisää uusi rivi host-tiedoston loppuun seuraavassa muodossa: Sisäinen IP-osoite ja Windows-tietokoneen nimi.

Esimerkiksi sisäinen IP-osoite on 10.99.100.110 ja tietokoneen nimi on DR-master.

Tallenna muiutokset

Host-tiedoston esimerkki

# Copyright (c) 1993-2009 Microsoft Corp.

#

# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.

#

# This file contains the mappings of IP addresses to hostnames. Each

# entry should be kept on an individual line. The IP address should

# be placed in the first column followed by the corresponding hostname.

# The IP address and the hostname should be separated by at least one

# space.

#

# Additionally, comments (such as these) may be inserted on individual

# lines or following the machine name denoted by a '#' symbol.

#

# For example:

#

# 102.54.94.97 rhino.acme.com # source server

# 38.25.63.10 x.acme.com # x client host

# localhost name resolution is handled within DNS itself.

# 127.0.0.1 localhost

109.108.11.16 DR-master

Toimenpiteet System Managerissa

Avaa Järjestelmä-välilehti System Managerista

Valitse Muuta VMS-palvelimien osoitteita

3. Valitse VMS-palvelin listalta

4. Valitse Muuta VMS-palvelimen osoitetta

5. Kirjoita VMS-palvelimen tietokoneen nimi (DNS-nimi) Uusi VMS-palvelimen osoite -kenttään

6. Valitse OK




Toimenpiteet Spotterin puolella

Selaa C:\Windows\System32\drivers\etc

Avaa host-tiedosto tektieditorilla

Sinun on ehkä suoritettava Notepad järjestelmänvalvojan käyttöoikeuksilla

Lisää uusi rivi host-tiedoston loppuun seuraavassa muodossa: Sisäinen IP-osoite ja Windows-tietokoneen nimi.

Esimerkiksi sisäinen IP-osoite on 10.99.100.110 ja tietokoneen nimi on DR-master.

Tallenna muutokset

Jokaisella Mirasys Spotter -sivustolla asiakkaan on vaihdettava päätallennettu osoite tietokoneen nimeksi (pääpalvelimen tietokoneen nimi) staattisen IP-osoitteen sijaan.

Host-tiedoston esimerkki

# Copyright (c) 1993-2009 Microsoft Corp.

#

# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.

#

# This file contains the mappings of IP addresses to hostnames. Each

# entry should be kept on an individual line. The IP address should

# be placed in the first column followed by the corresponding hostname.

# The IP address and the hostname should be separated by at least one

# space.

#

# Additionally, comments (such as these) may be inserted on individual

# lines or following the machine name denoted by a '#' symbol.

#

# For example:

#

# 102.54.94.97 rhino.acme.com # source server

# 38.25.63.10 x.acme.com # x client host

# localhost name resolution is handled within DNS itself.

# 127.0.0.1 localhost

109.108.11.16 DR-master

Spotterin käynnistäminen järjestelmänvalvojana

Kun Spotter käynnistyy Suorita järjestelmänvalvojana, käyttäjä voi valita eri osoitteita ja yhteyden muodostamisen.

Valitse Spotter-kuvaketta hiiren kakkospainikkeella ja valitse Suorita järjestelmänvalvojana

2. Paina Delete-painiketta

3. Valitse Lisää

4. Määritä yhteyden nimi

5. Aseta VMS-palvelintietokoneen tietokoneen nimi kenttään Osoite

6. Valitse OK

7. Kun yhteys Spotterin ja VMS-palvelimen välillä on kunnossa, Yhteyden tila Yhdistetty näytetään

8. Luo yhteys valittuun VMS-palvelimeen napsauttamalla Jatka




Pagination
Previous page
Spotterin käyttäminen palomuurin ulkopuolelta
Next page
Spotter-sovelluksen käynnistäminen