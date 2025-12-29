# Liikkeentunnistus | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/liikkeentunnistus

Liikkeentunnistus

Liiketunnistusominaisuutemme avulla voit määrittää, mitkä tallenteet tallennetaan tiedostojärjestelmäämme ja mitä voidaan käyttää hälytysten käynnistämiseen.

Aloittaaksesi liikkeentunnistuksen käytön sinun on määritettävä liikemaskit, joita käytetään määrittämään, havaitaanko kamerassa tai videovirrassa liikettä.

Aikataulun avulla voit päättää, mitä liikemaskia käytetään tallenteiden tallentamisessa tiedostojärjestelmään.

Liiketunnistuksen kautta saatuja tietoja voidaan käyttää hälytysasetuksissa hälytysten käynnistämiseen. Hälytyksen laukaisuasetuksissa määritetään, mitä liikemaskin liiketunnistusta käytetään hälytyksen laukaisijana.

Pääset liikkeentunnistuksen määrityksiin System Managerissa valitsemalla VMS-palvelimen asetukset > Kameran asetukset > Liiketunnistus.

Herkkyys ja määrä

Järjestelmä havaitsee liikkeen herkkyyden ja määrän perusteella:

Herkkyys: Pikselit muuttuvat enemmän kuin asetettu raja

Määrä: Määritetty määrä pikseleitä muuttuu

Kun kuvassa on paljon taustakohinaa (esimerkiksi valaistusolosuhteiden muutokset), voit pienentää herkkyyttä vetämällä liukusäädintä vasemmalle tai suurentaa määrällistä rajaa vetämällä liukusäädintä oikealle.

Liikkeentunnistusmenetelmät
Vertaileva havaitseminen 

Vertaileva tunnistus vertaa kuvaa sitä edeltävään kuvaan, ja sitä voidaan käyttää useimmissa olosuhteissa.

Jos erot ylittävät asetetut rajat, järjestelmä havaitsee liikkeen.

Kun taustalla on paljon liikettä, esimerkiksi sade, liikkuvat lehdet tai valoisuuden muutokset, käytä mukautuvaa liikkeentunnistusta.

Adaptiivinen tunnistus 

Adaptiivinen tunnistus vertaa kutakin kuvaa taustakuvaan.

Järjestelmä oppii taustakuvan automaattisesti eikä se tulkitse esimerkiksi liikkuvia lehtiä liikkeeksi.

Jos yli puolet kuvan pikseleistä muuttuu, järjestelmä päättelee, että valaistusolosuhteet ovat muuttuneet, minkä seurauksena se nollaa vertailukuvan ja aloittaa sen oppimisen uudelleen.

Hermeneuttinen havaitseminen 

Hermeneuttinen tunnistus on kehittynyt liikkeentunnistusjärjestelmä haastaviin sääolosuhteisiin, kuten rankkasateeseen, ”meluisiin” taustakuviin ja tilanteisiin, joissa käytetään ulkoisia videosisällön analysointityökaluja (VCA).

Hermeneuttinen tunnistus vaatii enemmän prosessointiresursseja kuin muut tunnistusmenetelmät.

Liiketunnistuksen kuvataajuus

Liiketunnistuksen kuvataajuus määrittää liiketunnistuksessa käytettävän kuvataajuuden.

On yleensä suositeltavaa käyttää oletuskuvanopeutta.

IP-kameroissa liikkeentunnistus käyttää kehysten sisäisiä ruutuja ja vastaa kehysten sisäistä ruutunopeutta. Tyypillisesti tämä on yksi kuva sekunnissa.

Pagination
Previous page
Moxa-asetukset
Next page
Liiketunnistuksen konfigurointi