# VCA - Uudelleentriggeröintisuodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-uudelleentriggerointisuodatin

VCA - Uudelleentriggeröintisuodatin

Retrigger (Uudelleentriggeröinti)-suodatin toimii tapahtuman läpivientinä, joka luo tapahtuman vain, jos tulo ei ole aiemmin lauennut määritellyn aikavälin sisällä.

Tyypillisesti Retrigger Filter -suodatinta käytetään sääntöjen yhdistelmän lopussa päällekkäisten hälytysten lähettämisen estämiseksi, ja tämä tarjoaa tarkemman hallinnan kuin Event Retrigger Time -vaihtoehto. Retrigger Filter -suodattimen tuottamat tapahtumat ovat syöttösäännön tapahtumatyyppiä.

Graphical View
Form View
Configuration
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

“Retrigger #”




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Interval (Aikaväli)

	

Aika, jolloin syöttötapahtuma ei voi synnyttää toista tapahtumaa.

	

3

Pagination
Previous page
VCA - Väri suodatin
Next page
VCA - Deep Learning suodatin