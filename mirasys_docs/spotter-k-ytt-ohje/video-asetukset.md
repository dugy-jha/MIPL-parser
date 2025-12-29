# Video (Asetukset) | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-k-ytt-ohje/V9.9/video-asetukset

Video (Asetukset)

Videoasetukset mahdollistavat mukautetun dekoodauksen asettamisen ja renderöintitekniikoiden muuttamisen suorituskyvyn parantamiseksi laitteistosta riippuen.

Videon dekoodaus

Käytä muokattuja dekoodausasetuksia  avulla voit valita tietyn dekoodausasetuksen ja päättää, kuinka monta prosenttia virroista puretaan GPU:n avulla.

H.264 codec

IPP: käyttää prosessoria

CoreAVC Voi käyttää prosessoria tai NVIDIA CUDAA

NVIDIA; vaatii NVIDIAN näytönohjaimen

Intel: käyttää suoritinta; jos prosessorissa on sisäänrakennettu Intel Graphics -grafiikkasuoritin, se voi myös käyttää GPU:ta

H.265 codec

NVIDIA: vaatii NVIDIAN näytönohjaimen

Intel: käyttää suoritinta; jos prosessorisirussa on sisäänrakennettu Intel Graphics GPU, se voi myös käyttää GPU:ta, liukusäädin vaikuttaa kuinka monta kameraa käyttää CPU/GPU:ta.

Kuinka monta streamia dekoodataan näyttölaitteistolla

Määrittää, kuinka prosenttiosuudet kameroista käyttävät CPU/GPU:ta.
Jos dekoodausmenetelmäksi on valittu Nvidia ja liukusäädin on asetettu esim. 50 %, puolet kameroista puretaan Nvidian avulla ja toinen puoli käyttää CoreAVC:tä, jos ne ovat H.264 ja Intel CPU, jos ne ovat H.265

Videon piirto

Mahdollistaa videon piirron muuttamisen WPF:ksi (oletus) tai DirectX:ksi

Ota sujuva videon skaalaus käyttöön

Se käyttää erilaista kuvan piirtomekanismia, ja sillä on tasoittava vaikutus videoon, varsinkin jos kuvanopeus on korkea (yli 20 fps).
Sujuvan videon skaalausasetusta ei kuitenkaan tule käyttää, jos käyttäjällä on useita Spotter-ikkunoita auki. 
 Tasainen videon skaalaus parantaa videokuvan ulkonäköä, mutta tämä asetus lisää tietokoneen kuormitusta hieman.

Pagination
Previous page
Striimaus
Next page
Näytön asetukset