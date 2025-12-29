# VCA - Repeatedly | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-repeatedly

VCA - Repeatedly

Looginen operaattori, joka käynnistyy, kun syöttösääntö käynnistyy tietyn määrän kertoja määritellyn ajanjakson aikana. Kestoaika on aikaikkuna, joka lasketaan jokaisesta syöttötapahtumasta. Kun esimerkiksi Repeatedly (toistuvasti)-sääntö on määritetty tuottamaan tapahtuma, kun tulo laukeaa kolme kertaa kahdeksan sekunnin kuluessa, ja kyseinen tulosääntö laukeaa neljä kertaa kahdeksan sekunnin kuluessa, Repeatedly-sääntö laukeaa sekä kolmannen tulosäännön laukeamisen jälkeen että uudelleen neljännen laukeamisen jälkeen. Tämä johtuu siitä, että kolme ensimmäistä laukaisua (tapahtumat 1-3) tapahtuivat 8 sekunnin ikkunan sisällä, ja lisäksi toinen joukko (tapahtumat 2-4) tapahtui myös omassa 8 sekunnin ikkunassaan.

Per Target -vaihtoehto määrittää, että sen on oltava sama seurattava kohde, joka laukaisee syötteen.

Graafinen näkymä
Lomakkeen näkymä
Konfigurointi
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

“Repeatedly #”




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Duration (Kesto)

	

Aika, jonka kuluessa käynnistettävien tapahtumien määrän on tapahduttava.

	

3




Number of Events to Trigger (Käynnistettävien tapahtumien määrä)

	

Kuinka monta kertaa tulon on laukaistava.

	

4




Per Target (Per kohde)

	

Määrittää, onko tulon oltava saman kohteen käynnistämä.

	

Inactive




Pagination
Previous page
VCA - Previous
Next page
VCA - Muut lähteet