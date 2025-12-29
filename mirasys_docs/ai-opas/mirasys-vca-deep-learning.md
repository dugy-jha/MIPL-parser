# Mirasys VCA Deep Learning | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/mirasys-vca-deep-learning

Mirasys VCA Deep Learning
Vaatimukset

Nvidian näytönohjain, jossa on CUDA-ytimiä

NVIDIAn näytönohjain, jossa on CUDA Compute Capability 7.5 tai uudempi.

Riippuen GPU:n CUDA-ytimistä, kuinka monta Deep Learning -kanavaa voit käyttää järjestelmässä.

Uusimmat NVIDIAn grafiikkaohjaimet (vähintään 460.73 tai uudempi).

CUDA-työkalupakki

Mirasys VMS 9.4 tai uudempi.

Deep Learning -objektitiedostot

Asennus

Asenna uusimmat Nvidia-ajurit järjestelmään

Lataa Mirasys VCA Deep Learning -paketti Mirasys Extranetistä.

Pura paketti

Selaa kansioon CUDA Toolkit

Asenna CUDA Toolkit kaikkine ominaisuuksineen

Löydät yksityiskohtaisen asennusohjeen täältä. here.

Joitakin ominaisuuksia ei asenneta, koska Microsoft Visual Studiota ei tarvita asennukseen, mutta työkalupakki tarjoaa esimerkkitiedostoja.

Jos olet jo asentanut Mirasys VMS:n, ennen tiedostojen kopiointia VMS-palvelut on pysäytettävä.

Pysäytä palvelut: WDServer, DVRServer ja SMServer

Tätä ei tarvitse tehdä, jos käytät V9.6:ta tai uudempaa versiota.

Kopioi VCA Deep Learning -tiedostokansioiden sisältö paikkaan C:\Program Files\DVMS\DVR\vca\bin.

Tätä ei tarvitse tehdä, jos käytössäsi on V9.6 tai uudempi versio.

Tämä polku on Mirasys VMS:n oletusasennuspaikka.
Jos olet asentanut Mirasys VMS:n johonkin muuhun paikkaan, kopioi tiedostot sinne.

Käynnistä WDServer, DVRServer ja SMServer palvelut

Tätä ei tarvitse tehdä, jos käytössäsi on V9.6 tai uudempi versio.

Nyt olet asentanut ja valmis aloittamaan Deep Learning -seurannan. Deep Learning tracking.

VCA-moottori käynnistyy VMS-palvelimessa, kun vähintään yksi kamera on määritetty käyttämään VCA:ta System Managerin kamera-asetuksissa. Ensimmäisellä VCA-moottorin käynnistyksellä käännetään NVIDIA-kirjastot, mikä voi viedä paljon aikaa. Käännöksen kesto riippuu käytetystä laitteistosta. Käänöksen aikana VCA ei toimi.

On erittäin suositeltavaa odottaa, kunnes NVIDIA-kirjastot on käännetty VCA:n käyttöönoton jälkeen, ennen kuin suoritat muita toimintoja VMS-palvelimella.

Lisensointi tapahtuu paikallisen VCA Deep Learning -lisensoinnin kautta tai lisenssipalvelimen avulla (virtuaaliympäristö tai jos haluat käsitellä lisenssejä yhdessä paikassa). VCA-lisenssin HWGUID-tunnuksen saamiseksi yksi kamera on otettava käyttöön System Managerin kamera-asetuksissa, jotta VCA-moottori käynnistyy. Kun VCA on käynnissä, VCA HWGUID-tunnus voidaan hakea System Managerin VMS-palvelimen lisenssidialogista.

Joissakin tapauksissa tunnistus ei ehkä toimi oikein. Yritä lisätä kuvanlaatua tai siirtää/zoomata kameran kuvaa lähemmäs haluttua tunnistusaluetta.

Mallit koulutetaan käyttämällä kirkkaita kuvia, joissakin tapauksissa mustavalkokuvan tai lämpökamerakuvan käyttäminen voi aiheuttaa sen, että tunnistus ei toimi oikein. Tätä varten voit kokeilla Deep Learning -suodattimen käyttöä Object Trackerin kanssa.

Pagination
Previous page
VCA Asetukset System Managerissa
Next page
Mirasys VCA Lisenssi Serveri