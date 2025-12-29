# Mirasys Rekisterilaattojen tunnistuspalvelun asennus | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/mirasys-rekisterilaattojen-tunnistuspalvelun-asenn

Mirasys Rekisterilaattojen tunnistuspalvelun asennus

Et voi käyttää VCA Deep Learningiä ja rekisterilaattojen tunnistusta samalla palvelimella.

Tämä liittyy Deep Learning -ajureihin. Deep Learning käyttää Nvidia CUDA Toolkit -ajureita, jotka eivät ole yhteensopivia rekisterikilven tunnistus Nvidia-mallien kanssa.

Voit silti asentaa rekisterilaattojen tunnistuksen samalle palvelimelle, jossa VCA Deep Learning on käytössä, jos et ota käyttöön Nvidia-mallien luomista ja käytät vain prosessoria rekisterilaattojen tunnistukseen.

Vaatimukset

Ylläpitäjän oikeudet

Listojenhallinta palvelu asennettuna

Rekisterilaattojen tunnistuslisenssi VMS-palvelimessa

Asennus

Lataa viimeisin version Extranetista

Pura paketti esimerkiksi C:\temp -kansioon

Käynnistä asennus tuplaklikkaamalla asennuspakettia

Klikkaa Install aloittaaksesi asennus

Klikkaa Next jatkaaksesi asennusta

Vaihda tarvittaessa asennuspolku, jos tälle ei ole tarvetta klikkaa Next jatkaaksesi

Vaihda portit ja osoitteet tarvittaessa

Jos esimerkiksi asennat rekisterilaattojen tunnistus palvelun toiseen koneeseen, joka ei ole VMS Master, sinun on vaihdettava Master address -osoite.

Sama koskee Event queue osoitetta. Korvaa tämä osoite sillä palvelimella, johon Listojen hallinta palvelu on asennettu.

Jos sinulla on Nvidia-näytönohjain asennettuna palvelimeen, voit pitää Käytä NVIDIA vaihtoehdon päällä. Tämä luo mallit näytönohjaimen käyttöä varten.

Klikkaa Next jatkaaksesi

Esimerkkikuva paikallisesta asennuksesta.
Esimerkkikuva kun palvelu asennettu toiselle palvelimelle.

Klikkaa Install ja odota

Asennus vie jonkin aikaa kunnes se on valmis

Mallien luonti voi kestää jopa 30 minuuttia, tämä riippuu näytönohjaimen tehoista

Klikkaa Finish lopettaaksesi asennus

Klikkaa Close sulkeaksesi asennus

Nyt License Rekisterilaattojen tunnistuspalvelu on asennettu palvelimelle ja valmis käytettäväksi.

Rekisterilaattojen tunnistuspalvelu lähettää tiedot VMS Master -palvelimelle ja voit määrittää palvelun System Managerin kautta.

Pagination
Previous page
Hälytykset ja konfigurointi
Next page
Easy LPR käyttöohje