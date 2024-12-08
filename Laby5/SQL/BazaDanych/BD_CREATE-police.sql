CREATE DATABASE [BD_Policja] COLLATE Polish_100_CI_AS_SC_UTF8;
GO
USE [BD_Policja];

CREATE TABLE Komenda_policji (
    ID INT PRIMARY KEY,
    Adres VARCHAR(60) NOT NULL,
    Telefon VARCHAR(15) CHECK (
        Telefon LIKE '+[0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]' OR  -- Format +XX XXX XXX XXX
        Telefon LIKE '[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]' OR               -- Format XXX XXX XXX
		Telefon LIKE '+[0-9][0-9] [0-9][0-9] [0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]'
    ) NOT NULL,
    Rejon VARCHAR(30) CHECK (
		ASCII(LEFT(Rejon, 1)) BETWEEN ASCII('A') AND ASCII('Z') 
		AND Rejon NOT LIKE '%[^a-¿A-¯]%'
	) NOT NULL,
);

CREATE TABLE Pojazd (
    Numer_rejestracyjny VARCHAR(8) PRIMARY KEY CHECK (Numer_rejestracyjny LIKE '[A-Z][A-Z] [0-9][0-9][0-9][0-9]'),
	Typ VARCHAR(20) CHECK (Typ IN ('Radiowóz', 'Motor','Helikopter','Skuter wodny')),
	Stan_techniczny VARCHAR(10) CHECK (Stan_techniczny IN ('zdatny', 'w naprawie', 'niezdatny')),
    Spalanie FLOAT CHECK (
        Spalanie >= 4.0 AND Spalanie <= 15.0 OR
        Spalanie >= 20.0 AND Spalanie <= 100.0
    ) NOT NULL, 
    Rok_produkcji INT CHECK (Rok_produkcji >= 2000 AND Rok_produkcji <= 2018) NOT NULL, 
    Przebyte_kilometry INT CHECK (Przebyte_kilometry >= 0 AND Przebyte_kilometry <= 200000) NOT NULL,
    Marka VARCHAR(10) CHECK(Marka NOT LIKE '%[^a-¿A-¯]%') NOT NULL,
    Model VARCHAR(25) NOT NULL
);

CREATE TABLE Patrol (
    ID INT PRIMARY KEY, 
	"Status" VARCHAR(10) CHECK ("Status" IN ('aktywny', 'zajêty', 'nieaktywny')), --"Status" bo Status to keyword sql
    "Data" DATE CHECK ("Data" <= GETDATE()),
    Numer_rejestracyjny_pojazdu VARCHAR(8) FOREIGN KEY REFERENCES Pojazd(Numer_rejestracyjny) NOT NULL,
	-- po poprawce
	ID_komendy INT FOREIGN KEY REFERENCES Komenda_policji(ID) NOT NULL
);

CREATE TABLE Policjant_danego_dnia ( --PROBLEM JAK OZNACZYC KLUCZE - jezeli pobieraja dane z excela
	PRIMARY KEY (Pesel, ID_patrolu),
    Pesel CHAR(11) CHECK(Pesel NOT LIKE '%[^0-9]%') NOT NULL, 
    ID_patrolu INT FOREIGN KEY REFERENCES Patrol(ID) NOT NULL 
);

CREATE TABLE Zdarzenie (
    DataCzas_rozpoczêcia DATETIME NOT NULL,  
    DataCzas_zakoñczenia DATETIME,
	CONSTRAINT Sprawdz_Daty_Zdarzenia CHECK (
			(DataCzas_rozpoczêcia IS NULL OR DataCzas_rozpoczêcia >= '1961-01-01') AND
			(DataCzas_zakoñczenia IS NULL OR DataCzas_zakoñczenia >= '1961-01-01') AND
			(DataCzas_rozpoczêcia <= DataCzas_zakoñczenia)),
    Lokalizacja VARCHAR(100), 
    Opis VARCHAR(3000),
	ID INT PRIMARY KEY
);

CREATE TABLE Trasa (
    ID INT PRIMARY KEY,
	ID_zdarzenia INT FOREIGN KEY REFERENCES Zdarzenie(ID) NOT NULL,
	-- po poprawce
	ID_patrolu INT FOREIGN KEY REFERENCES Patrol(ID) NOT NULL
);

CREATE TABLE Punkty (
	PRIMARY KEY (ID_trasy, Numer),
    Numer INT NOT NULL,
    ID_trasy INT FOREIGN KEY REFERENCES Trasa(ID) NOT NULL,
    Szerokoœæ FLOAT CHECK(Szerokoœæ >= -90.0 AND Szerokoœæ <= 90.0) NOT NULL,
    Wysokoœæ FLOAT CHECK(Wysokoœæ >= 0.0 AND Wysokoœæ <= 180.0) NOT NULL,
    Czas TIMESTAMP  CHECK (Czas < CURRENT_TIMESTAMP) NOT NULL
);
