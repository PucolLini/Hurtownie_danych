CREATE DATABASE Policja
GO

USE Policja

CREATE TABLE Komenda (
	ID_komendy INTEGER IDENTITY(1,1) PRIMARY KEY,
	Numer_komendy INTEGER NOT NULL,
	Adres VARCHAR(128) NOT NULL,
	Telefon VARCHAR(16) NOT NULL,
	Rejon VARCHAR(32) NOT NULL,
	Is_current BIT NOT NULL
)
GO

CREATE TABLE Miejsce_zdarzenia (
	ID_miejsca INTEGER IDENTITY(1,1) PRIMARY KEY,
	Miasto VARCHAR(32) NOT NULL,
	Ulica VARCHAR(128) NOT NULL,
	Numer VARCHAR(8)
)
GO

CREATE TABLE Opis_zdarzenia (
	ID_zdarzenia INTEGER IDENTITY(1,1) PRIMARY KEY,
	Opis VARCHAR(128) NOT NULL
)
GO

CREATE TABLE Pojazd (
	ID_pojazdu INTEGER IDENTITY(1,1) PRIMARY KEY,
	Nr_rejestracyjny VARCHAR(8) NOT NULL,
	Typ VARCHAR(16) NOT NULL,
	Stan_techniczny VARCHAR(16) NOT NULL,
	Marka VARCHAR(16) NOT NULL,
	Model VARCHAR(32) NOT NULL,
	Spalanie VARCHAR(8) NOT NULL,
	Rok_produkcji VARCHAR(4) NOT NULL,
	Is_current BIT NOT NULL
)
GO

CREATE TABLE "Data" (
	ID_data INTEGER IDENTITY(1,1) PRIMARY KEY,
	Rok INTEGER NOT NULL,
	Numer_miesi¹ca INTEGER NOT NULL,
	Nazwa_miesi¹ca VARCHAR(16) NOT NULL,
	Dzieñ INTEGER NOT NULL,
	Czy_dzieñ_roboczy BIT NOT NULL
)
GO

CREATE TABLE Czas (
	ID_czas INTEGER IDENTITY(1,1) PRIMARY KEY,
	Godzina INTEGER NOT NULL,
	Minuta INTEGER NOT NULL,
	Sekunda INTEGER NOT NULL,
	Pora_dnia VARCHAR(16) NOT NULL
)
GO

CREATE TABLE Opis_awarii (
	ID_opis_awarii INTEGER IDENTITY(1,1) PRIMARY KEY,
	Typ_awarii VARCHAR(16) NOT NULL
)
GO

CREATE TABLE Patrol (
	ID_patrolu INTEGER IDENTITY(1,1) PRIMARY KEY,
	Kategoria_wieku_kierowcy VARCHAR(16) NOT NULL,
	P³eæ_kierowcy VARCHAR(16) NOT NULL,
	Ranga_kierowcy VARCHAR(32) NOT NULL
)
GO

CREATE TABLE F_Dojazd_do_zdarzenia (
	ID_komendy INTEGER FOREIGN KEY REFERENCES Komenda,
	ID_pojazdu INTEGER FOREIGN KEY REFERENCES Pojazd,
	ID_miejsca INTEGER FOREIGN KEY REFERENCES Miejsce_zdarzenia,
	ID_zdarzenia INTEGER FOREIGN KEY REFERENCES Opis_zdarzenia,
	ID_patrolu INTEGER FOREIGN KEY REFERENCES Patrol,
	ID_czas INTEGER FOREIGN KEY REFERENCES Czas,
	ID_data INTEGER FOREIGN KEY REFERENCES "Data",
	Numer_trasy INTEGER NOT NULL,
	Czas_dotarcia INTEGER NOT NULL,
	D³ugoœæ_trasy INTEGER NOT NULL,
	--Liczba_dojazdów INTEGER NOT NULL,

	CONSTRAINT Dojazd_composite_pk PRIMARY KEY (
		ID_komendy,
		ID_pojazdu,
		ID_miejsca,
		ID_zdarzenia,
		ID_patrolu,
		ID_data,
		ID_czas,
		Numer_trasy
	)
)
GO

CREATE TABLE F_Awaria (
	ID_pojazdu INTEGER FOREIGN KEY REFERENCES Pojazd,
	ID_data INTEGER FOREIGN KEY REFERENCES "Data",
	ID_czas INTEGER FOREIGN KEY REFERENCES Czas,
	ID_opis_awarii INTEGER FOREIGN KEY REFERENCES Opis_awarii,
	--Przewidywany_czas_naprawy INTEGER NOT NULL,
	--Koszt_naprawy INTEGER NOT NULL,

	CONSTRAINT Awaria_composite_pk PRIMARY KEY (
		ID_pojazdu,
		ID_data,
		ID_czas,
		ID_opis_awarii
	)
)
GO
