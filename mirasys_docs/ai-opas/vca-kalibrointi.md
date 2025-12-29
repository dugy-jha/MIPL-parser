# VCA Kalibrointi | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-kalibrointi

VCA Kalibrointi

Kameran kalibrointi on tarpeen, jotta VCAcore voi luokitella kohteet eri objektiluokkiin.
Kun kanava on kalibroitu, VCA Core pystyy päättelemään kohteen todelliset ominaisuudet, kuten nopeuden, korkeuden ja pinta-alan, ja luokittelemaan kohteet niiden mukaisesti.

Kalibrointia ei tarvitse tehdä, kun käytetään Deep Learning -seurantaa, ainoastaan kun käytetään normaalia VCA:ta tai Deep Learning -suodatinta.

Kameran kalibrointi jakautuu seuraaviin alateemoihin:

Kalibroinnin käyttöönotto

Kalibroinnin ohjaimet

Kanavan kalibrointi

Kalibroinnin lisäparametrit

Kalibroinnin käyttöönotto

Kalibrointi on oletusarvoisesti poistettu käytöstä.
Jos haluat ottaa kalibroinnin käyttöön kanavassa, merkitse Enable Calibration (Ota kalibrointi käyttöön) -valintaruutu.

Kalibrointisäädöt
3D-grafiikan päällyste

Kalibrointiprosessin aikana videokuvan piirteet on sovitettava yhteen 3D-grafiikkapeitteen kanssa.
3D-grafiikkapeite koostuu vihreästä ruudukosta, joka edustaa maatasoa.
Pohjatasolle on sijoitettu useita 3D-mimikoita (ihmisen muotoisia hahmoja), jotka edustavat ihmisen mittoja nykyisillä kalibrointiparametreilla.
Kalibrointijäljitelmiä käytetään henkilön koon tarkistamiseen näyttämöllä, ja ne ovat 1,8 metriä korkeita.
Mimikoita voidaan liikuttaa näyttämöllä siten, että ne asettuvat ihmisten (tai tunnetusti vastaavankorkuisten esineiden) kanssa samalle viivalle kuin henkilö.

Hiiren ohjaimet

Kalibrointiparametreja voidaan säätää hiirellä seuraavasti:

Napsauta ja vedä maatasoa kameran kallistuskulman muuttamiseksi.

Käytä hiiren pyörää kameran korkeuden säätämiseen. - Vedä liukusäädintä muuttaaksesi pystysuoraa näkökenttää.

Huomautus: Kameran kallistuskulmaa ja korkeutta voidaan säätää myös ohjauspaneelin liukusäätimillä.

Ohjauspaneelin kohteet

Ohjauspaneeli (näkyy oikealla puolella yllä olevassa kuvassa) sisältää seuraavat hallintalaitteet:

Height (Korkeus): Säätää kameran korkeutta

Tilt (Kallistus): Säätää kameran kallistuskulmaa

VFOV: Säätää kameran pystysuuntaista näkökenttää. Huomautus: Oikea arvo kameran pystysuuntaiselle näkökentälle on olennaisen tärkeä tarkan kalibroinnin ja luokittelun kannalta.

Horizon (Horisontti): Ottaa käyttöön tai poistaa käytöstä horisontin näytön. Hyödyllinen, kun halutaan linjata horisontti syvällä olevassa kohtauksessa.

Grid (Ruudukko): Ottaa käyttöön tai poistaa käytöstä maatason ruudukkonäytön. Laajenna/tappaa-säädin (<) paljastaa lisäasetukset, joilla voidaan muuttaa maatason ruudukon väriä, peittävyyttä ja kokoa.

Advanced (Edistyneet): Tuo näkyviin lisäasetukset kameran panorointia ja kääntämistä varten.

Burnt-in Annotaatiot: Paljastaa Burnt-in Annotation -ohjaimet kätevästi.

Kontekstivalikon kohteet

Kun napsautat hiiren oikealla painikkeella (tai napautat ja pidät hiiren painettuna tabletilla) ruudukkoa, näyttöön tulee kontekstivalikko:

Kun sama toiminto suoritetaan jäljitelmälle, jäljitelmän kontekstivalikko tulee näkyviin:

Kontekstivalikon mahdolliset toiminnot ovat:

Kanavan kalibrointi

Kanavan kalibrointi on tarpeen kohteen parametrien, kuten korkeuden, pinta-alan, nopeuden ja luokituksen, arvioimiseksi.

Jos asennusta vastaava korkeus, kallistuskulma ja pystysuora näkökenttä ovat tiedossa, ne voidaan yksinkertaisesti syöttää parametreina ohjauspaneelin asianmukaisiin kenttiin.

Jos näitä parametreja ei kuitenkaan tiedetä, tässä osassa annetaan vaiheittainen opas kanavan kalibrointiin.

Vaihe 1: Löydä ihmiset paikasta

Etsi kohtauksesta ihmisiä tai ihmisten kokoisia esineitä.
Yritä löytää henkilö läheltä kameraa ja henkilö kauempaa kamerasta.
On hyödyllistä pysäyttää video toisto/taukosäätimellä, jotta mimiikat voidaan sijoittaa tarkasti. Sijoita mimiikat ihmisten päälle tai lähelle:

Vaihe 2: Syötä kameran pystysuora näkökenttä.

Oikean pystysuuntaisen näkökentän määrittäminen on tärkeää tarkan kalibroinnin kannalta.
Seuraavassa taulukossa on esilaskettuja arvoja pystysuuntaiselle näkökentälle eri kennokokoja varten.

 

	

Focal Length(mm)

	

1

	

2

	

3

	

4

	

5

	

6

	

7

	

8

	

9

	

10

	

15

	

20

	

30

	

40

	

50




CCD Size (in)

	

CCD Height(mm)

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 

	

 




1/6"

	

1.73

	

82

	

47

	

32

	

24

	

20

	

16

	

14

	

12

	

11

	

10

	

7

	

 

	

 

	

 

	

 




1/4"

	

2.40

	

100

	

62

	

44

	

33

	

27

	

23

	

19

	

17

	

15

	

14

	

9

	

7

	

 

	

 

	

 




1/3.6"

	

3.00

	

113

	

74

	

53

	

41

	

33

	

28

	

24

	

21

	

19

	

12

	

11

	

9

	

6

	

 

	

 




1/3.2"

	

3.42

	

119

	

81

	

59

	

46

	

38

	

32

	

27

	

24

	

21

	

16

	

13

	

10

	

7

	

 

	

 




1/3"

	

3.60

	

122

	

84

	

62

	

48

	

40

	

33

	

29

	

25

	

23

	

20

	

14

	

10

	

7

	

5

	

 




1/2.7"

	

3.96

	

126

	

89

	

67

	

53

	

43

	

37

	

32

	

28

	

25

	

22

	

15

	

11

	

8

	

6

	

 




1/2"

	

4.80

	

135

	

100

	

77

	

62

	

51

	

44

	

38

	

33

	

30

	

27

	

18

	

14

	

9

	

7

	

5




1/1.8"

	

5.32

	

139

	

106

	

83

	

67

	

56

	

48

	

42

	

37

	

33

	

30

	

20

	

15

	

10

	

8

	

6




2/3"

	

6.60

	

 

	

118

	

95

	

79

	

67

	

58

	

50

	

45

	

40

	

37

	

25

	

19

	

13

	

9

	

8




1"

	

9.60

	

 

	

135

	

116

	

100

	

88

	

77

	

69

	

62

	

56

	

51

	

35

	

27

	

18

	

14

	

11




4/3"

	

13.50

	

 

	

 

	

132

	

119

	

107

	

97

	

88

	

80

	

74

	

68

	

48

	

37

	

25

	

19

	

15

Jos taulukko ei sisällä tarvittavia parametreja, pystysuora FOV voidaan arvioida tarkastelemalla kuvan ääripäitä ylhäällä ja alhaalla.
Huomaa, että ilman oikeaa pystysuuntaista FOV-arvoa ei välttämättä ole mahdollista saada jäljitelmiä vastaamaan eri kohdissa olevia henkilöitä.

Vaihe 3: Anna kameran korkeus

Jos kameran korkeus on tiedossa, kirjoita se. Jos korkeus ei ole tiedossa, arvioi se niin lähelle kuin mahdollista.

Vaihe 4: Säädä kallistuskulmaa ja kameran korkeutta

Säädä kameran kallistuskulmaa (ja tarvittaessa korkeutta), kunnes molemmat jäljitelmät ovat suunnilleen samankokoisia kuin oikea henkilö kyseisessä kohdassa kohtauksessa.
Muuta kallistuskulmaa napsauttamalla ja vetämällä maatasoa ja säädä kameran korkeutta hiiren pyörällä tai ohjauspaneelilla.
Tavoitteena on varmistaa, että ruudukon eri kohtiin sijoitetut jäljitelmät ovat samassa linjassa kohtauksessa olevien ihmisten tai ihmisten kokoisten kohteiden kanssa.
Kun parametreja on säädetty, kohteiden merkinnät heijastavat muutoksia ja luokittelevat kohteet sen mukaisesti.

Vaihe 5: Varmista asennus

Kun kohtaus on kalibroitu, vedä tai lisää jäljitelmiä eri kohtiin kohtauksessa ja tarkista, että ne näyttävät samankokoisilta ja -korkeuksisilta kuin oikea henkilö.

Varmista, että VCAcore-merkinnän ilmoittama korkeus ja pinta-ala näyttävät suunnilleen oikeilta.

Huomaa, että ohjauspaneelin Burnt-in -annotaatioasetuksia voidaan käyttää eri annotaatiotyyppien ottamiseen käyttöön ja poistamiseen käytöstä.

Toista vaihe 4, kunnes kalibrointi on hyväksyttävä.

Lisäkalibrointiparametrit

Lisäkalibrointiparametrien avulla maatasoa voidaan kääntää ja pyörittää vaikuttamatta kameran kalibrointiparametreihin.
Tämä voi olla hyödyllistä kalibrointiasetusten visualisoimiseksi, jos kohtausta panoroidaan tai vieritetään kameraan nähden.

Huomautus: laajennetut panorointi- ja rullausparametrit vaikuttavat vain 3D-pohjatason suuntaukseen, jotta se voidaan kohdistaa helpommin videokuvan kanssa, eivätkä ne vaikuta kalibrointiparametreihin.

Pagination
Previous page
VCA Alueet
Next page
VCA-luokitus