# Listojenhallinnan asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/listojenhallinnan-asetukset

Listojenhallinnan asetukset

Listojenhallinta mahdollistaa henkilöllisyyksien ja listojen määrittämisen sallituille ja ei-sallituille henkilöille.

Asetuksissa voi:

Lisätä, muokata ja poistaa henkilöllisyyksiä

Lisätä, muokata ja poistaa listoja

Ladata ja tallentaa listoja ja henkilöllisyyksiä

Säätää LPR ja FR tapahtumien säilytysaikoja

Aktivoida ja määritellä integraatioita ja niiden asetuksia

System manager sovelluksessa on useita dialogeja list management palvelun asetuksille, dialogit löytyvät “Järjestelmäasetukset“ kohdasta.

LPR ja FR integraatio ominaisuus pitää olla mukana lisenssissä jotta integraatioita voi käyttää.

Listojenhallinnan asetukset

Listojenhallinnan asetusten avaaminen:

Valitse Järjestelmä välilehti

Järjestelmäasetukset valikosta tuplaklikkaa Listojenhallinnan asetuksia:

Listojenhallinnan asetusten avaus lataa asetukset list management palvelulta ja näyttää asetukset. Jos asetusten lataus epäonnistuu, virheilmoitus näytetään ja dialogi sulkeutuu.

Listojenhallinnan asetusdialogi

Dialogissa on nämä välilehdet:

Identiteetit - lista henkilöllisyyksistä ja niihin liittyvistä asetuksista

Listat - listat ja niiden asetukset

Vie/Tuo - listojenhallintadatan tallennus CSV tiedostoon ja lataus CSV tiedostosta

Tietokanta-asetukset - list management palvelun tietokantaan liittyvät asetukset

Integratioasetukset - integratioiden aktivointi ja niiden asetukset

Kaikilla välilehdillä tehdyt muutokset tallentuvat OK nappulaa klikkaamalla.

Dialogi voidaan sulke tallentamatta muutoksia klikkaamalla Sulje tai Peruuta nappulaa.

Alla on yksityiskohtaista tietoa eri välilehdistä.

Identiteetit välilehti

Identiteetit välilehdellä voi muokata henkilöllisyyksiä:

Identiteettien välilehti

Identiteetin valinta tapahtuu hiiren vasemmalla nappulalla. Useamman identiteetin valinta (useampi rivi listalta), tapahtuu hiiren vasemmalla nappulalla + Ctrl/Shift nappuloilla. “Aktiivinen” tilan vaihto onnistuu kaikille valituille identiteeteille laittamalla “Aktiivinen” rasti päälle tai pois päältä.

Identiteettilistan yläpuolella on Hae kenttä: kun kirjoitat siihen, lista päivittyy automaattisesti näyttämään hakutuloksia mistä löytyi haettu henkilön nimi tai rekisterinumero.

Identiteettejä voi lisätä ja poistaa Lisää ja Poista nappuloilla jotka ovat listan alapuolella.

Identiteetin tiedot kohdassa näytetään yksityiskohtaista tietoa identiteetistä, mutta näitä tietoja ei voi muuttaa. Identiteetin tietojen muuttamin tapahtuu klikkaamalla Muokkaa nappulaa tai tuplaklikkaamalla listan identiteettiä.

Kun lisäätään tai muutetaan identiteetin tietoja, näytetään tämä dialogi:

Lisää/muokkaa identiteetin tietoja

Tietoja voi muuttaa, lisätä/poistaa identiteetin kasvokuvia ja ajoneuvoja (rekisterikilvet).

Lisätäksesi identiteetille kuva, klikkaa“Lisää uusi kasvojen kuva” nappulaa, ja allaoleva dialogi aukeaa:

Lisää kasvokuva -dialogi

Useampi kuva voidaan lisätä identiteetille. Kaikkia kuvia käytetään identiteetin kasvojen tunnistuksessa, useamman kuvan käyttö voi parantaa tunnistuksen tarkkuutta.

Tässä kohtaa voidaan valita kasvokuva ja antaa nimi sille. Kun kuva on valittu, kasvoista luodaan tunnistustiedot.

Tunnistustietojen luonti edellyttää että vähintään yksi face recognition palvelu on käynnissä ja rekisteröitynyt järjestelmään.

Kuvan poisto tapahtuu valitsemalla kuva valikosta ja klikkaamalla Poista nappulaa.

Oletuskuvan asetus

Yksi kuvista on oletuskuva, mitä käytetään pikkukuvana Spotter sovelluksessa ja identiteettilistalla. Kuvan valinta oletuskuvaksi tapahtuu valitsemalla kuva valikosta ja klikkaamalla Aseta valittu kasvokuva oletuskuvaksi nappulaa:

Aseta valittu kuva oletuskuvaksi
Ajoneuvojen lisäys ja poisto

Ajoneuvoja voi lisätä ja poistaa. Ajoneuvon lisääminen tapahtuuklikkaamalla Lisää kulkuneuvo nappulaa, joka aukaisee allaolevan dialogin:

Lisää kulkuneuvo

Lisää kulkuneuvo dialogissa voidaan antaa rekisterinumero, aluekoodi, valmistaja, malli ja ajoneuvon väri. Ajoneuvon poistaminen tapahtuu valitsemalla ajoneuvo valikosta ja klikkaamalla Poista valittu kulkuneuvo nappulaa.

Listat välilehti

Listat välilehdellä voidaan muokata listoja:

Listojen välilehti

Listan valinta tapahtuu hiiren vasemmalla nappulalla. Useamman listan valinta onnistuu hiiren vasemmalla nappulalla + Ctrl/Shift nappuloilla. Aktiivinen tilaa voi muuttaa kaikille valituille listoille laittamalla Aktiivinen-rasti päälle tai pois päältä.

Listojen lisäys ja poisto tapahtuu listan alapuolella olevilla Lisää ja Poista nappuloilla.

Listan tietoja voi muuttaa klikkaamalla Muokkaa nappulaa tai tuplaklikkaamalla listaa.

Allaoleva dialogi näytetään listaa lisättäessä ja muokattaessa:

Lisää/muokkaa listoja

Identiteettejä voidaan lisätä listalle tai poistaa listalta, sekä antaa listalle nimi ja väri.

Vie/Tuo välilehti

"View/Tuo" välilehdellä voidaan tallentaa listojenhallintadata CSV tiedostoon tai ladata listojenhallintadata CSV tiedostosta:

Vie/tuo välilehti
Tuo

Seuraavat parametrit tarvitaan datan lataamiseen:

Tiedoston polku - polku CSV tiedostoon minne listojenhallintadata on tallennettu

Tuontityyppi - vain identiteetit tai identiteetit ja listat

CSV erotin - pilkku tai puolipiste

Kohteet joilla on sama tunniste - Sivuuta, ylikirjoita tai luo uusi tunniste

Kun parametrit on valittu, Tuo tiedot tiedostosta nappula aktivoituu, ja datan tuonti voidaan aloittaa. Tuonnin edistyminen ja tulos näytetään käyttöliittymässä.

Vie

Seuraavat parametrit tarvitaan datan tallentamiseen:

Tiedoston polku - polku CSV tiedostoon minne listojenhallintadata talletetaan

Tuontityyppi - vain identiteetit tai identiteetit ja listat

CSV erotin - pilkku tai puolipiste

Kun parametrit on valittu, the Vie tiedot tiedostoon nappula aktivoituu, ja datan tallennus voidaan aloittaa. Tuonnin edistyminen ja tulos näytetään käyttöliittymässä.

Tietokanta-asetukset välilehti

Tietokanta-asetukset välilehdellä asetetaan list management palvelun tietokannan asetukset.:

Tietokanta-asetusten välilehti
Integraatioasetukset välilehti

Integraatioasetukset välilehdellä asetetaan list management palvelun integraatioon liittyvät asetukset:

Integraatioasetusten välilehti

Tässä määritellään viestijonon asetukset ja integraation aktivointi. Välilehti ei ole käytettävissä jos lisenssissä ei ole mukana listojenhallinnan integraatio ominaisuus.

Ilmoitus listojenhallinta asetuksien päivityksestä

Jos listojenhallinta asetuksia muutetaan toisesta sovelluksesta, System Manager sovellus saa tiedon muutoksista ja näyttää alla olevan viestin:

Tietojen muutosten varoitus

Kun klikkaat dialogin OK nappulaa, asetusdialogit suljetaan asetusten lataamiseksi list management palvelulta. Kaikki tallentamattomat muutokset häviävät.

Pagination
Previous page
Tallennevarastoasetukset
Next page
Varmuuskopiointi