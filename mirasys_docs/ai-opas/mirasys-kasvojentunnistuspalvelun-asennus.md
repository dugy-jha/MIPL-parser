# Mirasys Kasvojentunnistuspalvelun asennus | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/mirasys-kasvojentunnistuspalvelun-asennus

Mirasys Kasvojentunnistuspalvelun asennus

Et voi käyttää VCA Deep Learning- ja Kasvojentunnistuspalvelua samalla palvelimella.

Tämä liittyy Deep Learning -ajureihin. Deep Learning käyttää Nvidia CUDA Toolkit -ajureita, jotka eivät ole yhteensopivia kasvojentunnistuspalvelun Nvidia-mallien kanssa.

Voit silti asentaa kasvojentunnistuspalvelun samalle palvelimelle, jossa VCA Deep Learning on käytössä, jos et ota käyttöön Nvidia-mallien luomista ja käytät vain prosessoria kasvojentunnistuspalveluun.

Vaatimukset

Ylläpitäjän oikeudet

Listojenhallinta palvelu asennettuna

Kasvojentunnistuslisenssi VMS-palvelimessa

Asennus

Lataa viimeisin version Extranetista

Pura paketti esimerkiksi C:\temp -kansioon

Käynnistä asennus tuplaklikkaamalla asennuspakettia

Klikkaa Install aloittaaksesi asennus

Klikkaa Next jatkaaksesi asennusta

Vaihda tarvittaessa asennuspolku, jos tälle ei ole tarvetta klikkaa Next jatkaaksesi

Vaihda portit ja osoitteet tarvittaessa

Jos esimerkiksi asennat kasvojentunnistuspalvelun toiseen koneeseen, joka ei ole VMS Master, sinun on vaihdettava Master address -osoite.

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

Nyt kasvojentunnistuspalvelu on asennettu palvelimelle ja valmis käytettäväksi.

Kasvojentunnistuspalvelu lähettää tiedot VMS Master -palvelimelle ja voit määrittää palvelun System Managerin kautta.

Pagination
Previous page
Hälytykset ja FR-asetukset
Next page
Ohjeita rekisterilaatojen tunnistuskameroiden sijoittelulle