# VCA Seuranta | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-seuranta

VCA Seuranta
Alustaminen

Kun käyttäjä valitsee seurantalaitteen, tarvitaan alustusvaihe. Tämä vaihtelee valitun seurantalaitteen mukaan.

Objektinseuranta: kun se on valittu, seurantalaitteen on "opittava kohtaus", jotta se voi määrittää taustan liikkuvien etualan kohteiden perusteella.

Kohtauksen oppimisen aikana live-näkymässä näkyy seuraava viesti, eikä kohteita seurata tänä aikana.

DL People Tracker & DL Object Tracker: Kun DL-moottori valitaan ensimmäisen kerran, se käynnistää mallin luomisprosessin. Tämä optimoi DL-mallit siten, että ne toimivat käytettävissä olevalla GPU-laitteistolla.

Riippumatta siitä, mikä seurantamalli on valittu, DL People Tracker -malli, DL Object Tracker -malli ja DL Filter -malli optimoidaan kaikki yhdellä kertaa.

Prosessi voi kestää jopa 10 minuuttia mallia kohti, ja se voi kasvaa eri näytönohjainkokoonpanoilla. Kun optimoidut mallit on saatu valmiiksi, ne tallennetaan konfigurointikansioon.

Prosessia ei tarvitse suorittaa uudelleen, ellei näytönohjaimen laitteistoa muuteta. Optimoinnin aikana live-näkymässä näkyy viesti, eikä kohteita seurata tänä aikana.

Huomaa: DL-suodatin vaatii saman alustamisprosessin, mutta se ei näytä viestiä.

Kun VCAserver on alustettu, se alkaa analysoida videovirtaa valitulla seurantalaitteella. Seurannalle ominaiset asetukset näkyvät myös seurantamoottorin valintavaihtoehdon alapuolella.

Valitusta seurantalaitteesta riippumatta mikä tahansa seurattava kohde voidaan siirtää käytettävissä olevien sääntöjen läpi.

Joissakin tapauksissa tietyt säännöt tai algoritmit ovat kuitenkin käytettävissä vain tietyn jäljittäjän kanssa.
Esimerkiksi DL-suodatin ja hylättyjä ja poistettuja kohteita koskevat säännöt ovat käytettävissä vain objektinseurannan kanssa.

Objekti seuranta

Objekti seuranta on liikkeisiin perustuva havaintomoottori. Kuvassa havaittujen muutosten perusteella algoritmi jakaa kuvan etualaan ja taustaan ja seuraa kaikkia etualan kohteita, jotka liikkuvat yli asetetun kynnysarvon.

Objekti seurannan asetukset ovat seuraavat:

Paikallaan olevan kohteen seuranta-aika

Paikallaan olevan kohteen seuranta-aika määrittää ajan, jonka moottori seuraa kohdetta sen jälkeen, kun se on pysähtynyt.
Koska paikallaan pysyvät kohteet on "sulautettava" kohtaukseen tietyn ajan kuluttua, seurantamoottori unohtaa paikallaan pysyneet kohteet paikallaan olevan kohteen seuranta-ajan jälkeen.

Oletusasetus on 60 sekuntia.

Hylätyn / poistetun kohteen kynnysarvo

Tämä kynnysaika, jonka objektin on oltava hylätty tai poistettu, ennen kuin Hylätyt / Poistetut-sääntö käynnistyy.

Oletusasetus on 5 sekuntia.

Seuratun kohteen vähimmäiskoko

Seurattavan kohteen vähimmäiskoko määrittää pienimmän kohteen koon, joka otetaan huomioon seurannassa.

Useimmissa sovelluksissa suositellaan oletusasetusta 10. Joissakin tilanteissa, joissa tarvitaan lisäherkkyyttä, arvo voidaan määrittää manuaalisesti.
Vaikka pienemmät arvot mahdollistavat pienempien kohteiden jäljittämisen, se voi lisätä alttiutta vääriin havaintoihin.

Kohteen jäljittäjän herkkyys

Objektinseurannan herkkyys -arvon avulla objektinseuranta voidaan virittää niin, että se ei huomioi tietyn kynnysarvon alittavaa liikettä.
Yhdistettynä huomautuksissa olevaan Blob Map -poltettuun merkintään, joka visualisoi sen alueen, jolla objektinseuranta havaitsee liikettä, tätä arvoa voidaan säätää ympäristöhäiriöiden suodattamiseksi pois.

Oletusasetus on 4.

Kohtauksen muutoksen tunnistus (Object Tracker)

Katso kohdasta kohtauksen muutoksen tunnistus -toiminnosta

Seurattujen kohteiden havaitsemispiste

Jokaisen seuratun kohteen kohdalla käytetään pistettä kohteen sijainnin määrittämiseksi ja sen arvioimiseksi, leikkaako se vyöhykkeen ja laukaiseeko se säännön. Tätä pistettä kutsutaan havaintopisteeksi.
Tunnistuspisteen määrittäminen suhteessa kohteeseen tapahtuu kolmessa eri tilassa:

Automaattinen

Automaattisessa tilassa havaintopiste asetetaan automaattisesti sen mukaan, miten kanava on määritetty.
Se valitsee 'Centroid' (keskipiste), jos kamera on kalibroitu yläpuolelle, tai 'Mid-bottom' (keskipohja), jos kamera on kalibroitu sivulle tai ei ole kalibroitu.

Keskipiste

Tässä tilassa havaintopisteen on pakko olla kohteen keskipiste.

Pohjan puoliväli

Tässä tilassa havaintopisteen on pakko olla seurattavan kohteen alareunan keskellä.
Tavallisesti tämä on kohteen maakosketuspiste (jossa kohde leikkaa maanpinnan).

Manipuloinnin tunnistus (Objekti seuranta)

Katso kohdasta Manipuloinnin tunnistuksesta.

Signaalin menetys Emit-väli

Katso kohdasta Signaalin menetys Emit-väli

Deep Learning henkilöiden seuranta

Deep Learning henkilöiden seuranta on suunniteltu seuraamaan ihmisiä tilanteissa, joissa kameran näkökenttä on suhteellisen lähellä.
Deep Learning henkilöiden seuranta perustuu Pose Estimation -tekniikkaan, joka tarjoaa henkilön sijainnin näkökentässä sekä kehon osien metatietoja avainpisteistä.
Katso tämän algoritmin laitteistovaatimukset kohdasta Deep Learning vaatimukset.

Deep Learning henkilö seurannassa on seuraavat asetukset:

Manipuloinnin tunnistus (DLPT)

Katso kohdasta manipuloinnin tunnistuksesta.

Signaalin menetys Emit-väli

Katso kohdasta Signaalin menetys Emit-väli

DL henkilöiden seurannan käyttöönotto

Avaa View channels (Kanavat)

Valitse kamera

Avaa Tracking (Seuranta)

Open Tracking Engine (seuranta moottori) pudotusvalikko ja valitse DL People Tracker (DL Henkilöiden seuranta)

Deep Learning objektinseuranta

The Deep Learning objektiseuranta on suunniteltu ihmisten, ajoneuvojen ja keskeisten kohteiden tarkkaan havaitsemiseen ja seurantaan haastavissa ympäristöissä, joissa liikkeisiin perustuvilla seurantamenetelmillä on vaikeuksia.
Seuraavassa on luettelo Deep Learning objektiseurannan havaitsemista kohteista:

Use table header to sort columns

Class Name

	

Description




person

	

Henkilö tai jäljitettävä esine, jossa on henkilö (esim. polkupyörä).




motorcycle

	

Moottoripyörä




bicycle

	

Polkupyörä




cyclist

	

Polkupyörällä ajava henkilö voidaan ilmoittaa kahtena erillisenä esineenä.




bus

	

Linja-auto




car

	

auto




van

	

pakettiauto, mukaan lukien mini-pakettiautot ja minibussit.




truck

	

Kuorma-auto, mukaan lukien kuorma-autot ja hyötyajoneuvot,




forklift

	

Trukki




bag

	

Rinkka tai reppu (urheilukassi)







	




Deep Learning Objekti seuranta perustuu luokittelu- ja havaintomalliin, joka antaa kohteen sijainnin näkökentässä. Katso tämän algoritmin laitteistovaatimukset kohdasta Deep Learning vaatimukset.

Deep Learning Objekti seurannassa on seuraavat asetukset:

Paikallaan olevien kohteiden suodatus

Katso kohdasta Stationary Hold On Time

Stationary Hold On Time -asetuksen lisäksi käytettävissä on lisäasetus Require Initial Movement (Vaadi alustava liike), joka estää sellaisten kohteiden seurannan, jotka eivät ole liikkuneet.

Seurattujen kohteiden havaitsemispiste

Katso kohdasta Seurattujen kohteiden havaintopiste

Manipulaation tunnistus (DLOT)

Katso kohdasta manipuloinnin tunnistuksesta.

Signaalin menetys Emit-väli

Katso kohdasta Signaalin menetys Emit-väli

Pagination
Previous page
VCA kanava asetukset
Next page
VCA Deep Learning Skeleton Tracker