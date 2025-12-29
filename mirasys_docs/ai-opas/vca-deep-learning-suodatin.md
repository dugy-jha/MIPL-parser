# VCA - Deep Learning suodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-deep-learning-suodatin

VCA - Deep Learning suodatin

Deep learning (Syväoppimis)-suodatin tarjoaa mahdollisuuden suodattaa pois kohteet, jotka laukaisevat säännön, jos syväoppimismalli ei luokittele niitä tiettyyn luokkaan.

Syväoppimissuodattimen asetukset määritetään Deep learning-sivulla.

Deep learning -sivulla on perusteellinen kuvaus suodattimen toiminnasta.

Yleensä syväoppimissuodatin yhdistetään johonkin toiseen sääntöön (sääntöihin), jotta ei-toivotut kohteet eivät laukaise hälytystä. Huomaa, että syväoppimissuodatinta ei voi käyttää minkään muun sääntötyypin syötteenä. Näin ollen sen on oltava graafin viimeinen sääntö.

Edellinen kuva havainnollistaa, miten syväoppimissuodatin, joka on määritetty vain ajoneuvoluokalle (luottamuskynnys 0,5), toimii vain ajoneuvo-objektin kohdalla.

Vyöhykkeellä oleva henkilö suodatetaan pois, koska henkilöluokka Sallittu -asetusta ei ole otettu käyttöön Deep Learning -määrityssivulla.

Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"DL Filter #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None

Tyypillinen loogisen säännön yhdistelmä

Alla oleva looginen sääntö tarkastaa, onko vyöhykkeeseen Centre liitetyn läsnäolosäännön laukaiseva objekti yksi Deep Learning -asetussivulla määritetyistä kiinnostavista luokista (katso yllä oleva asetussivun kuva).
Ainoastaan syväoppimissuodattimen arvoksi on asetettu Can Trigger Actions, mikä tarkoittaa, että vain tämä loogisen säännön osa on käytettävissä toimien lähteenä.

Lisäksi kaikilla nopeussuodattimen tuottamilla toiminnoilla on tapahtumatyyppi Läsnäolo.

Pagination
Previous page
VCA - Uudelleentriggeröintisuodatin
Next page
VCA - Ehdolliset sääntötyypit