# Yleiset asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/yleiset-asetukset

Yleiset asetukset

VMS-palvelimen nimi

Kuvaus

Salasana

Protokolla

Multicast-osoite

Varapalvelinasetukset

Multicast-osoite

Kun yksittäinen työasemavirta avataan useita kertoja, palvelin – ja verkko – kohtaavat tarpeettoman rasituksen, koska jokaista streamia käsitellään erillisenä kokonaisuutena.
Multicasting mahdollistaa yhden streamin avaamisen ja lähettämisen useille työasemille samanaikaisesti.
Käytettäessä useaa työasemaa, kunkin videokanavan stream lähetetään lähiverkkoon vain kerran.
Kaikki lähiverkon sovellukset voivat vastaanottaa yksittäisen streamin, joten verkon kaistanleveyden käyttö on pienempi kuin lähetettäessä stream jokaiselle sovellukselle erikseen.
Ominaisuus on määritettävä System Managerissa ja verkkoasetusten kautta.
Katso verkkoinfrastruktuuripalvelustasi tietoja monilähetystuen ottamisesta käyttöön verkkotasolla.

Multicastin määritys System Managerissa:

Muuta palvelimen yleisissä asetuksissa protokolla TCP (oletus):stä RTP Multicast:ksi.

Määritä Multicast-osoite

Toista vaiheet 1-2 kaikille järjestelmän vaadituille palvelimille. Huomio: Jokaisen monilähetysosoitteen on oltava erillinen.

Varapalvelinasetukset

Kun uutta palvelinta lisätään järjestelmään, se voidaan määrittää varapalvelimeksi.
Failover-palvelin on varapalvelin, joka vastaa kaikista palvelintehtävistä, jotka on määritelty vikasietoturvan alaisiksi.
Varastopalvelimilla on oltava sama tiedostojärjestelmä (sama asema) kirjaimet) vikasietosuojauksen alaisena VMS-palvelimina, ja niitä voidaan käyttää vain IP-kameran varmuuskopiointiin.
Valmiustilassa vikasietopalvelimet näkyvät erillisessä kansiossa VMS-palvelin-luettelossa.
Kun jokin VMS-palvelin katsotaan rikki tai eivät ole käytettävissä, ne ovat siirtyneet "Vikaantuneet VMS-palvelimet" -kansion alle
.Kaikki käytettävissä olevat vikasietopalvelimet ovat vastuussa epäonnistuneesta palvelimesta.
Varavaihtoasetuksia voidaan hallita valitun palvelimen yleisistä asetuksista.
Viansiirto tapahtuu, jos kaikki materiaalilevyt ovat rikki tai palvelin ei ole käytettävissä pidempään kuin määritetyn ajan.

Käytä varapalvelimena

Tämä asetus määrittää, että palvelinta käytetään varapalvelimena

Tälle VMS-palvelimelle on asetettu varapalvelin

Tämä asetus määrittää, että palvelimen rooli siirretään varapalvelimelle virhetilanteen aikana

Viivästetty failover datan menettämisen estämiseksi

Failover prosessia on päivitetty, datojen menettämisen estämiseksi failover prosessin aikana, esimerkiksi tallentimen päivityksen aikana.

Kun materiaalia kopioidaan failover tallentimesta, palautettu tallennin tarkistaa ensin tallennetut datat ja kopioi sitten vain puuttuvan materiaalin. (Mukaan lukien video, audio, teksti data, metadata, and ANPR data).

Tämä toiminto aktivoidaan täältä System Manager > Videohallintapalvelimen yleinen valikko > valintaruudusta valitse Odota että tallennin soveltaa asetuksia.

Viivästetty Failover voidaan ottaa käyttöön vain tallentimissa V9.7 tai uudemmissa, koska ennen V9.7:ää olevat tallentimet eivät tue valikoivaa materiaalin kopiointia, ja data menee päällekkäin.

Käytä automaattista toimintojen takaisin siirtoa

Tämä asetus ottaa käyttöön automaattisen toimintojen takaisin siirron

Käytä automaattista aineiston kopiointia

Tämä valinta ottaa käyttöön automaattisen aineiston kopioinnin palvelimelle

Esimerkiksi vikatilanteessa, jossa palvelin ei ole käytettävissä yli 2 tuntiin, varapalvelimen käyttö aktivoituu.




Pagination
Previous page
Videonhallintapalvelimet
Next page
Portinohjaus