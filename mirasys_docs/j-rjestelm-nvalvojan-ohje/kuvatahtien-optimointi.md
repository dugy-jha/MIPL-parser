# Moxa-asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/kuvatahtien-optimointi

Moxa-asetukset
Moxa PTZ -muokkauksen ottaminen käyttöön

System Managerin roolin ominaisuuksissa / VMS-palvelimien asetuksissa voidaan valita Moxa PTZ -asetusten muokkaus käyttäjäryhmälle. Jos Enable Moxa PTZ control (Ota käyttöön Moxa PTZ -ohjaus) -vaihtoehto ei ole valittuna, Moxa PTZ -asetukset näkyvät kameran asetuksissa, mutta niitä ei voi muuttaa.

Moxa PTZ -asetukset

Kamera-asetuksissa on käytettävissä ylimääräinen Moxa-asetukset-välilehti niille kameroille, joille on määritetty Moxa PTZ -ajurin asetukset tai jos Moxa-muokkaus on otettu käyttöön käyttäjien käyttäjäryhmässä.

Laite

Ota kameran Moxa PTZ -asetukset käyttöön.

Jos kamerassa ei ole PTZ-asetuksia, avaa laite- ja PTZ-ohjaus -välilehdet oletusarvoilla.

Jos kamerassa on Moxa PTZ -asetukset ja Enable (Ota käyttöön) ei ole valittuna, asetusten tallentaminen poistaa Moxa PTZ -asetukset kamerasta.

Osoite kirjoita MOXA-laitteen IP- tai DNS-osoite.

Portti-indeksi on sen MOXA-laitteen sarjaportin indeksi (1 - 255), johon PTZ-kamera on liitetty.

Timeout/ms on aikakatkaisu millisekunneissa MOXA-laitteen kanssa käytävää viestintää varten (oletusarvo on 5000 ms).

Protocol (protokolla) on PTZ-kameran viestintäprotokolla seuraavasta luettelosta:

{ "PelcoD", "BoschOSRD" } }

Oletusarvo on "PelcoD".

PTZ-ohjaus

Kameraindeksi - analogisen PTZ-kameran osoite, joka on asetettu kamerassa (yleensä se on laitteistohyppyjen avulla) (0 - 255).

Baudinopeus - sarjaportin baudinopeus bitteinä sekunnissa. MOXA tukee seuraavia baudinopeuksia:

{ 50, 75, 110, 134, 150, 300, 600, 1200, 2400, 4800, 6400, 7200, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600 }.

Oletusarvo on 38400 bps.

Databitit - (tavu) - arvo seuraavasta joukosta:

{5, 6, 7, 8 }

Oletusarvo on 8.

Stopbitti - (tavu) - arvo seuraavasta joukosta:

{ 1, 2 }

Oletusarvo on 1.

Pariteetti - arvo seuraavasta luettelosta:

{ "None" = 0, "Even" = 1, "Odd" = 2, "Mark" = 3, "Space" = 4 } }

Oletusarvo on "None".

Virtauksen ohjaus - arvo seuraavasta luettelosta:

{ "None" = 0, "RTS / CTS" = 1, "XON / XOFF" = 2, "Both" = 3 } }

Oletusarvo on "Ei mitään".




Pagination
Previous page
Lisäasetukset
Next page
Liikkeentunnistus