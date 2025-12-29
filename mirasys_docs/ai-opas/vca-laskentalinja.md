# VCA - Laskentalinja | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-laskentalinja

VCA - Laskentalinja

Counting line (Laskentalinja) on havaintosuodatin, joka on optimoitu suunnattujen kohteiden (esim. ihmisten tai ajoneuvojen) laskemiseen vilkkaammissa havaintotilanteissa.

Esimerkkejä tällaisista sovelluksista voivat olla:

Ihmisten laskenta yläpuolella olevilla kameroilla vähittäiskaupassa.

Ajoneuvojen laskenta kameroiden avulla yleisillä valtateillä.

Joissakin tilanteissa, kuten sisäänkäynneillä, joissa on yläpuolelle asennettuja kameroita, laskentalinja tuottaa tyypillisesti tarkemman laskennan kuin käyttämällä edellä mainittuja läsnäolosääntöön liitettyjä laskureita.

Tapahtuma syntyy aina, kun objekti ylittää viivan määritettyyn suuntaan.
Jos useat kohteet ylittävät viivan yhdessä, syntyy useita vastaavia tapahtumia.
Näitä tapahtumia voidaan käyttää suoraan toimintojen käynnistämiseen, jos Can Trigger Actions -ominaisuus on valittuna.
Laskentaviivat liitetään alueisiin, joille on määritetty Line-muoto.
Katso lisätietoja kohdasta Alueet.

Jos laskentalinjalle määritetään alue, jota ei ole määritetty viivamuodolla, alueominaisuus muuttuu automaattisesti (aluemuotoa ei voi muuttaa takaisin ennen kuin laskentarivi lakkaa viittaamasta kyseiseen alueeseen).

Laskentalinjoilla on tietty suunta, joka on merkitty käyttöliittymän nuolella (suunta A tai B), ja tämän nuolen suunta määräytyy määritetyn alueen mukaan.
Jokainen säännön esiintymä laskee yhteen suuntaan. Jos haluat laskea molempiin suuntiin, samaan alueeseen on lisättävä toinen laskentaviivasääntö, jonka vastakkainen suunta on valittu.
Seuraavassa on esimerkki laskurilla konfiguroidun kaksisuuntaisen laskentalinjan sääntökuvaajasta, joka havainnollistaa tätä.

HUOMAUTUS: Videokanavaa kohden voidaan käyttää enintään 5 laskentalinjasuodatinta.

Laskentalinjan kalibrointi

Tarkkojen lukemien tuottamiseksi laskentalinja vaatii kalibroinnin.
Toisin kuin objektinseurantatoiminnon moottoria, tätä ei voida tehdä yleisellä tasolla koko kohtaukselle 3D-kalibrointityökalun avulla.
Tämä johtuu siitä, että laskentalinjaa ei aina sijoiteta maanpinnan tasolle, vaan se voi sijaita missä tahansa suunnassa ja missä tahansa kohdassa kohtauksessa.

Esimerkiksi laskentalinja voidaan konfiguroida pystysuoraan ja kameranäkymä sivulle.
3D-kalibrointityökalun sijaan laskentalinjalla on oma kalibrointiasetus.
Kaksi viivan keskipisteestä yhtä kaukana olevaa palkkia edustaa odotetun kohteen leveyttä. Näin laskentalinja voi hylätä kohinan ja laskea myös useita kohteita.

Laskentalinjan kalibrointi:

Valitse counting line (laskentalinja) sääntö.

Valitse Enable width calibration (Ota leveyskalibrointi käyttöön) -vaihtoehto.

Säädä kalibrointimerkkien välistä etäisyyttä vetämällä kalibrointimerkkejä, kunnes etäisyys vastaa suunnilleen laskettavien kohteiden kokoa. Vaihtoehtoisesti voit saavuttaa saman tuloksen siirtämällä Width (leveys)-liukusäädintä.

Kalibroinnin leveys näkyy laskentarivin säännössä, ja sitä voidaan muokata suoraan kalibroinnin leveyden muuttamiseksi.

Pienet merkit isojen merkkien molemmin puolin osoittavat pienimmän ja suurimman leveyden, joka lasketaan yhdeksi objektiksi.

HUOMAUTUS: jos Leveys-liukusäädin on asetettu nollaan, Ota leveyden kalibrointi käyttöön -valintaruutu poistetaan automaattisesti käytöstä.

Laskentalinjan kalibroinnin palaute

Jotta käyttäjä voi määrittää laskentalinjan kalibroinnin tarkemmin, havaittujen kohteiden leveydet näytetään päällekkäin laskentalinjan vieressä, kun kohteet kulkevat sen yli.
Oletusarvoisesti tämä näyttövaihtoehto on käytössä. Jos se ei kuitenkaan näy, varmista, että vaihtoehto on käytössä Burnt-in Annotaation -asetuksissa.

Kalibrointipalaute esitetään mustavalkoisina viivoina laskentaviivan molemmin puolin alueiden määritykset -sivulla.Jokainen viiva edustaa laskenta-algoritmin havaitsemaa kohdetta.Viivan leveys osoittaa viivan havaitseman kohteen leveyden. Viimeisimmät havaitut kohteet näytetään kussakin suunnassa siten, että viimeisin havainto näkyy lähimpänä laskentalinjaa.

Varjon suodatin

Laskentalinjassa on shadow filter (varjosuodatin), joka on suunniteltu poistamaan laskenta-algoritmiin vaikuttavien kohteiden varjojen vaikutukset.
Varjot voivat aiheuttaa epätarkkoja laskentatuloksia saamalla kohteen näyttämään todellista kokoaan suuremmalta tai yhdistämällä kaksi tai useampia kohteita toisiinsa.
Jos varjot aiheuttavat epätarkkaa laskentaa, varjosuodatin on otettava käyttöön valitsemalla rivin Filter Shadows (varjosuodatin)-valintaruutu.
Varjosuodatin suositellaan otettavaksi käyttöön vain silloin, kun varjoja esiintyy, koska algoritmi voi erehtyä pitämään tiettyjä kohteen osia varjoina, mikä voi johtaa huonompiin laskentatuloksiin.
Tämä koskee erityisesti kohteita, joiden kontrasti taustaan nähden on pieni (esim. mustatakkiset ihmiset mustaa mattoa vasten).

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

Line_Counter




Zone (alue)

	

Alue, johon tämä sääntö liittyy

	

None




Direction (Suunta)

	

Ota laskenta käyttöön A- tai B-suunnassa (yksi suunta per laskentalinja).

	

None




Enable Width Calibration (Ota leveyskalibrointi käyttöön)

	

Leveyskalibrointi tarkemman laskennan mahdollistamiseksi

	

None




Width (leveys)

	

Leveyden kalibrointiarvo

	

0




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active

Pagination
Previous page
VCA - Pysähtynyt
Next page
VCA - Ehdolliset säännöt