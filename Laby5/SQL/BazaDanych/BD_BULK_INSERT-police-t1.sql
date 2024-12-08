DELETE FROM Komenda_policji
DELETE FROM Pojazd
DELETE FROM Patrol
DELETE FROM Policjant_danego_dnia
DELETE FROM Zdarzenie
DELETE FROM Trasa
DELETE FROM Punkty
GO

USE [BD_Policja];

BULK INSERT dbo.Komenda_policji FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Komenda_policji.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Pojazd FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Pojazd.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Patrol FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Patrol.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Policjant_danego_dnia FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Policjant_danego_dnia.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Zdarzenie FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Zdarzenie.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Trasa FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Trasa.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)

BULK INSERT dbo.Punkty FROM 'C:/Users/Karina/Desktop/STUDIA/SEM5/Hurtownie_danych/Laby/Laby2/GeneratedOutput1/Punkty.bulk' WITH (CODEPAGE = '65001', FIELDTERMINATOR='|', ROWTERMINATOR = '\n', FIRSTROW = 2)





