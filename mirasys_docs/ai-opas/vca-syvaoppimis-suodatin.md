# VCA - Syväoppimis-suodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-syvaoppimis-suodatin

VCA - Syväoppimis-suodatin

VCAserver tukee myös luokittelua Deep-learning filter (syväoppimissuodattimen) avulla. Tällöin sääntöä laukaiseva kohde voidaan analysoida syväoppimissuodattimen avulla ja palauttaa ennustettu luokka ja luottamustaso. Käytettävissä olevat objektiluokat määritellään mallissa.

VCAserverissä syväoppimissuodatin voi käyttää GPU-kiihdytystä, katso laitteistovaatimukset kohdasta Syväoppimisvaatimukset.

Ilman GPU-kiihdytystä syväoppimissuodatin käyttää prosessoria, ja syväoppimissuodattimen käyttäminen useilla kanavilla, jotka tuottavat paljon tapahtumia (yli 1 tapahtuma sekunnissa), voi johtaa järjestelmän huonoon suorituskykyyn, eikä sitä suositella.




Jokaisella mahdollisella objektiluokalla on lisäparametreja:

Sallittu: Sallitaanko tämän objektityypin kulkea suodattimen läpi. Jos tämä ei ole valittuna, tähän tyyppiin luokitellut objektit eivät aiheuta mitään toimia.

Luottamuskynnys: Arvo (0,0 - 1,0), joka edustaa luokittelun edellyttämää vähimmäisluottamustasoa. Kaikki kohteet, joiden luokittelupisteet ovat tätä vähimmäisarvoa alhaisemmat, suodatetaan pois eivätkä ne aiheuta mitään toimia.

Pagination
Previous page
VCA - Objektin näyttäminen
Next page
VCA - Suodattimet