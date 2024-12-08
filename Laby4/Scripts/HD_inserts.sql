USE Policja;

INSERT INTO Komenda VALUES (1,'ulica Strzelecka 53/46 Czersk','+48 602 674 697','Czersk',1);
INSERT INTO Komenda VALUES (13,'al. Andersa 651 Lêbork','531 199 305','Lêbork',1);
INSERT INTO Komenda VALUES (33,'al. Morelowa 597 S³upsk','+48 604 742 576','S³upsk',0);
INSERT INTO Komenda VALUES (48,'aleja G³owackiego 15/79 Kartuzy','+48 694 690 546','Kartuzy',1);

INSERT INTO Miejsce_zdarzenia VALUES ('P³oñsk','pl. Andersa 35','27');
INSERT INTO Miejsce_zdarzenia VALUES ('Toruñ','ul. Kasprowicza', '470');
INSERT INTO Miejsce_zdarzenia VALUES ('Wa³brzych','plac Rybacka','760');
INSERT INTO Miejsce_zdarzenia VALUES ('Gdañsk','al. Promienna 31','33');

INSERT INTO Opis_zdarzenia VALUES ('P³onie budynek, sprawca na miejscu');
INSERT INTO Opis_zdarzenia VALUES ('Pod³o¿ona bomba na stadionie');
INSERT INTO Opis_zdarzenia VALUES ('Strzelanina na ulicy, 3 ofiary, 5 rannych');
INSERT INTO Opis_zdarzenia VALUES ('Okradziony sklep');

INSERT INTO Pojazd VALUES ('XD 0255','Skuter wodny','zdatny','NISSAN','Qashqai','8.43','2015',1);
INSERT INTO Pojazd VALUES ('OQ 1101','Motor','zdatny','FORD','Kuga','6.74','2002',1);
INSERT INTO Pojazd VALUES ('SR 0640','Radiowóz','zdatny','MERCEDES','C-Class','6.89','2010',1);
INSERT INTO Pojazd VALUES ('PT 8140','Helikopter','w naprawie','Eurocopter','AW139','53.31','2003',1);

INSERT INTO "Data" VALUES (2018,3,'Marzec',21,1);
INSERT INTO "Data" VALUES (2022,5,'Maj',14,0);
INSERT INTO "Data" VALUES (2017,9,'Wrzesieñ',29,1);
INSERT INTO "Data" VALUES (2021,12,'Grudzieñ',5,0);

INSERT INTO Czas VALUES (22,57,31,'noc');
INSERT INTO Czas VALUES (12,48,00,'popo³udnie');
INSERT INTO Czas VALUES (9,05,29,'po³udnie');
INSERT INTO Czas VALUES (7,34,16,'ranek');

INSERT INTO Opis_awarii VALUES ('Silnik');
INSERT INTO Opis_awarii VALUES ('Opona');
INSERT INTO Opis_awarii VALUES ('Hamulce');
INSERT INTO Opis_awarii VALUES ('Zawieszenie');

INSERT INTO Patrol VALUES ('m³ody doros³y','kobieta','INSPEKTOR');
INSERT INTO Patrol VALUES ('doros³y','mê¿czyzna', 'NADKOMISARZ');
INSERT INTO Patrol VALUES ('m³ody doros³y','mê¿czyzna','ASPIRANT SZTABOWY');
INSERT INTO Patrol VALUES ('starszy doros³y','kobieta','GENERALNY INSPEKTOR');

INSERT INTO F_Dojazd_do_zdarzenia VALUES (1,4,1,1,1,3,3, 112,15,7);
INSERT INTO F_Dojazd_do_zdarzenia VALUES (2,3,2,1,2,3,4, 120,30,11);
INSERT INTO F_Dojazd_do_zdarzenia VALUES (3,2,3,2,3,4,4, 86,43,21);
INSERT INTO F_Dojazd_do_zdarzenia VALUES (4,1,4,3,4,2,2, 55,12,5);
INSERT INTO F_Dojazd_do_zdarzenia VALUES (1,3,1,4,1,1,1, 46,81,40);
INSERT INTO F_Dojazd_do_zdarzenia VALUES (2,2,2,4,2,1,1, 51,55,12);

INSERT INTO F_Awaria VALUES(1,4,1,1);
INSERT INTO F_Awaria VALUES(2,3,2,2);
INSERT INTO F_Awaria VALUES(3,2,3,3);
INSERT INTO F_Awaria VALUES(4,1,4,4);
