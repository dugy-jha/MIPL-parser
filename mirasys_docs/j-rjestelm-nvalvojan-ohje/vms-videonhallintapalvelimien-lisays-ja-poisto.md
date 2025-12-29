# VMS-videonhallintapalvelimien lisäys ja poisto | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/vms-videonhallintapalvelimien-lisays-ja-poisto

VMS-videonhallintapalvelimien lisäys ja poisto

Sinulla voi olla (lisenssistä riippuen) yhdestä rajattomaan palvelimeen yhdessä järjestelmässä.
Yksi palvelin ei saa kuulua useampaan kuin yhdelle pääpalvelimelle (SMS-palvelimelle).
Voit määrittää salasanan kullekin palvelimelle.
Järjestelmä pyytää salasanaa, jos joku yrittää lisätä palvelimen toiseen järjestelmään.

VMS-videonhallintapalvelimen lisääminen järjestelmään

Avaa Videonhallintapalvelimet -välilehti

Valitse Lisää VMS-palvelin

Yleiset asetukset avataan

Määritä palvelimen nimi

Määriä kuvaus, jos tarpeellista

Kirjoita palvelimen IP-osoite tai DNS-nimi.

Aseta tarvittaessa palvelimen salasana

Valitse OK Palvelin ja siihen liitetyt laitteet (kamerat ja äänikanavat) lisätään luetteloon.

Huom: Jos palvelin on suojattu salasanalla, järjestelmä pyytää salasanaa.

VMS-videonhallintapalvelimen poistaminen järjestelmästä

Valitse poistettava palvelin listasta

Valitse Poista VMS-palvelin

Valitse OK

Yhteyden tila:

Jos yhteys palvelimeen katkeaa, System Manager -sovellus yrittää automaattisesti muodostaa yhteyden palvelimeen.

HUOMIO:

Kun olet lisännyt Mirasys VMS-videonhallintapalvelimen masterin alle, tee seuraavat toimet:

Vaihda järjestelmänvalvojan käyttäjän salasana slave-palvelimen System Managerin avulla

Poista SMServer-palvelu käytöstä slave-palvelimelta

Pagination
Previous page
Kameroiden lisääminen CSV-tiedoston avulla
Next page
Haku VMS-palvelimen asetuksista