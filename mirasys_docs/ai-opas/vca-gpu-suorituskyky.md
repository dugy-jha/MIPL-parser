# VCA - GPU Suorituskyky | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-gpu-suorituskyky

VCA - GPU Suorituskyky

Tässä on perusselvitys siitä, mihin prosessoria käytetään. CPU:ta käytetään seuraaviin tehtäviin

Saapuvan RTSP-virran dekoodaus

Minkä tahansa lähtevän kommentoidun RTSP:n koodaus.

Kuvan koon muuttaminen ennen niiden siirtämistä analyysimoottoriin

Esikäsittely ennen kuin kuva siirretään GPU:lle DL-seurannan käsittelyä varten.

Kolme ensimmäistä pistettä suoritetaan tällä hetkellä kaikille seurantalaitteille, tavalliselle liikekohteen seurantalaitteelle ja DL-seurantalaitteille.

Viimeinen kohta suoritetaan, kun käytetään DL-seurantalaitteita, ja se vaatii suorittimelta joitakin lisäresursseja. Tämän seurauksena DL-seurantalaitteita käytettäessä tietyllä suorittimella tuettavien kanavien määrä vähenee.

Tämä kaavio antaa yleiskuvan siitä, miten VCA voi toimia GPU:n kanssa. Eri skenaariot voivat vaikuttaa suorituskykyyn.

GPU

	

CUDA ytimet

	

Tensor ytimet

	

Muisti

	

Prosessorin taajuus

	

Muistin kaistanleveys (GB/sec)

	

Todelliset kanavat DLOT testatut




RTX A4000

	

6144

	

192

	

16 GB

	

1750

	

448

	

56




GeForce RTX 3070

	

5888

	

180

	

8 GB

	

1440-1710

	

19

	

54




GeForce RTX 2080 Ti

	

4352

	

368

	

11GB

	

1350-1545

	

616

	

50




Tesla T4

	

2560

	

320

	

16GB

	




	

320

	

45




GeForce GTX 1660 SUPER

	

1408

	




	

6 GB

	

1530-1785

	

336

	

28




GeForce GTX 1650

	

896

	




	

4 GB

	

1485-1665

	

128

	

18

Pagination
Previous page
VCA - Läsnäolo A- tai B-alueella