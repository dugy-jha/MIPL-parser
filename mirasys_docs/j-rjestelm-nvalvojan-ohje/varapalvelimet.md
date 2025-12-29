# Varapalvelimet | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/varapalvelimet

Varapalvelimet

❗️Jos haluat siirtää myös VCA-kanavat, varapalvelimen tulee sisältää oikea määrä aktivoituja VCA-kanavia. Mirasys VMS tukee varapalvelimia Mirasys VMS -vaihtoehtona.

Mirasys VMS tukee varapalvelimia Mirasys VMS -vaihtoehtona.
Varapalvelimet ovat passiivisessa valmiustilassa olevia VMS-palvelimia, kunnes järjestelmä tunnistaa, että yksi aktiivisista videotallennus-VMS-palvelimista havaitaan vialliseksi; tässä vaiheessa varapalvelin tulee viallisen palvelimen tilalle.
Viallinen palvelin voidaan korjata ja vaihtaa uudeksi varapalvelimeksi, kun taas sen tilalle tullut varapalvelin voi jatkaa toimintaansa aktiivisena palvelimena.
Huomautus: Kun varapalvelin korvaa aktiivisen palvelimen, Spotter-laajennukset (kuten Grafana tai List Management Application), joita ei ole sisäänrakennettu, eivät sisälly varapalvelinprosessiin, ja ne on asennettava uudelleen manuaalisesti palvelimen palauttamisen jälkeen. 

Tallennus- ja vikasietopalvelimien laitteistokokoonpanon tulee olla samanlainen, ja niissä tulee jakaa asemakirjainmääritykset ja versionumerot.
Palvelimen videokaappauskorttiin kytkettyjä analogisia kameroita ei siirretä varapalvelimelle. Vain aiemmin määritetyt IP-kamerat osoitetaan uudelleen vaihdon aikana.

Varapalvelimen toiminnallisuus

Kun järjestelmään lisätään uusi palvelin, järjestelmänvalvoja voi valita, onko lisätty palvelin vakiopalvelin vai varapalvelin.
Jos palvelin on vakiopalvelin, järjestelmänvalvoja voi valita, lisätäänkö kyseinen palvelin vikasietovalvontaan, eli palvelinvian (laitteiston tai ohjelmiston) sattuessa tämä palvelin siirtyy käytettävissä olevaan varapalvelimeen.
On tärkeää huomata, että pääpalvelin on asennettava eri laitteille kuin tallennuslisenssillä tai vikasietokäyttöoikeuksilla toimiville laitteille.
Laitteiston vähimmäiskokoonpano koostuu kolmesta palvelimesta: yksi pääpalvelin, yksi videotallennus VMS-palvelin ja yksi valmiustilan vikasietopalvelin. .

Varapalvelinsiirto käynnistetään seuraavissa olosuhteissa:

Pääpalvelin on menettänyt yhteyden VMS-palvelimeen, ja järjestelmänvalvojan asettama aikakatkaisu on saavutettu

VMS-palvelin on ilmoittanut pääpalvelimelle, että yhteys kaikkiin palvelimella oleviin materiaalilevyihin (tallennusmuistiin) on epäonnistunut

Manuaalista tietojen palautusta palvelimen kiintolevyiltä voidaan yrittää, jos levyt ovat edelleen toiminnassa

Palvelimen Watchdog-palvelu on ilmoittanut pääpalvelimelle, ettei se voi alustaa tallennuspalvelua

Tallennus on jatkuvaa sen jälkeen, kun varapalvelin on ottanut roolin pitääkseen järjestelmän toimintakunnossa.
Ainoa poikkeus on yhteyden katkeamisen ja vikasietotilan laukaisun välinen aikakatkaisuaika. Järjestelmänvalvoja määrittää tämän.
Kun varapalvelin on ottanut viallisen palvelimen tallennusroolin, järjestelmästä luodaan automaattisesti varmuuskopio uuden perustason asettamiseksi.

Varapalvelimen palautusprosessin ja seuraavan järjestelmän varmuuskopion aikana:

Käyttäjät eivät voi suorittaa manuaalisia varmuuskopiointitoimintoja

Kaikki seuraavat rikkinäiset palvelimet lisätään varapalvelinjonoon

Varapalvelimensiirtojono käsitellään sen jälkeen, kun varapalvelintilan palautus on suoritettu.

Varapalvelimen yhteenveto versiosta 9.5.0 eteenpäin

V9.5.0 VMS:ssä varapalvelintoiminto uusittiin toimimaan aiempaa nopeammin. Se voidaan käynnistää manuaalisesti Samassa versiossa toteutettiin myös palautustoiminto ja materiaalin kopiointi varapalvelimelta tallentimeen palautuksen jälkeen.
Lisäksi lisättiin myös vikaloki, josta käyttäjä näkee kaikki tapahtuneet varapalvelinprosessit ja kuinka niitä käsitellään, ja käyttäjä voi myös laukaista palautuksen ja materiaalin kopioinnin. käsin.

Kuvaus

V9.5.0:n varapalvelintoiminto muutettiin siten, että se ei käytä järjestelmän varmuuskopiotiedostoja. Sen sijaan SMServer tallentaa tallentimen asetukset aikatauluineen ja liikemaskeineen palvelimen asetusten välimuistiin ja käyttää näitä asetuksia tehdessään vikasietoa.
Palvelimen asetuksia, aikatauluja ja maskeja pyydetään palvelimelta, kun SMServer muodostaa yhteyden palvelimeen.

Osana varapalvelin prosessin muutosta, myös palvelimen käynnitys optimoitiin käynnistymään mahdollisimman nopeasti.

Nyt on myös lisätty pienempiä verkon katkeamisen havaitsemisaikoja. Aiemmassa versiossa pienin aika oli 1min, mutta nyt on valittavissa 10s, 20s, 30s, 40s ja 50s.

Palvelimen asetusten välimuisti

Palvelimen maskit tallennetaan välimuistiin kansioon "C:\Program Files\DVMS\SystemManagement\RecorderMasksStore"

Palvelimen aikataulut tallennetaan välimuistiin kansioon "C:\Program Files\DVMS\SystemManagement\RecorderSchedulesStore"

Palvelimen aikataulut tallennetaan välimuistiin kansioon "C:\Program Files\DVMS\SystemManagement\RecorderSchedulesStore"

Varapalvelinprosessi

Kun varapalvelinprosessi käynnistetään (käyttäjä laukaisee manuaalisesti, verkkoyhteys katkesi tai tallentimen kriittinen vika), SMServer suorittaa seuraavan toimenpiteen

Tarkista, onko saatavilla varapalvelinta, joka kuuluu samaan varapalvelinryhmään kuin epäonnistunut palvelin, ja onko yhteys varapalvelimeen

Luo varapalvelimen lokimerkinnän varapalvelintilasta

Hanki epäonnistuneen palvelimen asetukset, maskit ja aikataulut palvelimen asetusten välimuistista

Tallentaa epäonnistuneet palvelimen asetukset varapalvelimelle

Tekee muutoksia järjestelmätietoihin, että varapalvelin toimii nyt normaalina palvelimena ja viallinen palvelin on viallisessa tilassa

Tekee muutoksia järjestelmätietoihin, että varapalvelin toimii nyt normaalina palvelimena ja epäonnistunut palvelin on rikki

Asettaa varapalvelinsiirron etenemistuloksen varapalvelinlokiin

Lähettää asiakkaille järjestelmän muutosilmoituksen

Manuaalinen varapalvelimenprosessin käynnistäminen

Käyttäjä voi käynnistää manuaalisen varapalvelinprosessin System Managerin käyttöliittymästä palvelimen asetusten välilehdellä. Manuaalinen varapalvelin on mahdollista, jos

on yhteys varapalvelimeen, joka kuuluu samaan varapalvelinryhmään kuin valittu palvelin

valitussa palvelimessa varapalvelin on käytössä

Käyttäjällä on rooli, jonka avulla vikasieto voidaan käynnistää manuaalisesti

Valitse rikkinäinen VMS-palvelin luettelosta

Valitse Aloita vikasieto valitusta VMS-palvelimesta vikasietopalvelimeen




Pagination
Previous page
TruCastin käyttö
Next page
Vähimmäisvaatimukset