# Spotterin käyttäminen palomuurin ulkopuolelta | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-k-ytt-ohje/V9.9/spotterin-kayttaminen-palomuurin-ulkopuolelta

Spotterin käyttäminen palomuurin ulkopuolelta

Suositeltu tapa käyttää Spotteria ulkoisista verkoista tai julkisen Internet-yhteyden kautta on muodostaa VPN-yhteys yrityksen intranetiin.
Näin palomuurin ulkopuolella oleva Spotter-sovellus voi käyttää pääpalvelimen intranet-IP-osoitetta ja videotallennus VMS-palvelimia. (Orjat).
VMS-järjestelmää on mahdollista käyttää myös ilman VPN:tä.
Tässä tapauksessa käyttäjän tulee muodostaa yhteys Master Serveriin ulkopuolisella IP-osoitteen ja portin yhdistelmällä.

Jos käyttäjä käyttää Spotteria useista verkoista, DNS-nimeä on käytettävä VMS-palvelimen staattisen IP-osoitteen sijaan.

HOST-tiedoston muokkaaminen

Tarkista tietokoneen nimi

Selaa C:\Windows\System32\drivers\etc

Avaa HOST-tiedosto tekstieditorilla

Sinun on ehkä suoritettava Notepad järjestelmänvalvojan käyttöoikeuksilla

Lisää uusi rivi host-tiedoston loppuun seuraavassa muodossa: Ulkoverkon IP-osoite ja tietokoneen nimi

Esimerkiksi ulkoinen IP-osoite on 10.99.100.110 ja tietokoneen nimi on DR-master.

Tallenna muutokset

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

Toimenpiteet VMS-palvelimella

Siirry Järjestelmä-välilehdelle System Managerissa

Valitse Muuta Videohallintapalvelimien osoitteita

3. Valitse VMS-palvelin listalta

4. Valitse Muuta VMS-palvelimen osoitetta

5. Kirjoita VMS-palvelimen tietokoneen nimi (DNS-nimi) Uusi VMS-palvelimen osoite -kenttään

6. Valitse OK

Toimenpiteet Spotterin puolella

Selaa C:\Windows\System32\drivers\etc

Avaa host-tiedosto tekstieditorilla

Sinun on ehkä suoritettava Notepad järjestelmänvalvojan käyttöoikeuksilla

Lisää uusi rivi host-tiedoston loppuun seuraavassa muodossa: Ulkoverkon IP-osoite ja tietokoneen nimi

Esimerkiksi ulkoinen IP-osoite on 109.108.11.16 ja DVMS-tallentimen PC-nimi on DR-master

Tallenna muutokset

Jokaisella Mirasys Spotter -asennuksessa asiakkaan on vaihdettava master-palvelimen osoite tietokoneen nimeksi (master-palvelimen tietokoneen nimi ) staattisen IP-osoitteen sijaan.

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

2. Paina Delete-painiketta käynnityksen aikana

3. Valitse Lisää

4. Määritä yhteyden nimi

5. Aseta VMS-palvelintietokoneen tietokoneen nimi kenttään Osoite

6. Valitse Ok

7. Kun yhteys Spotterin ja VMS-palvelimen välillä on kunnossa, yhteyden tila Yhdistetty näytetään

8. Luo yhteys valittuun VMS-palvelimeen painamalla Jatka




Pagination
Previous page
Asentaminen Spotter Only-paketista
Next page
Spotterin käyttäminen useista verkoista