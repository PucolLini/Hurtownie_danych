USE HD_Policja;

INSERT INTO [HD_Policja].[dbo].[Komenda] (Numer_komendy, Adres, Telefon, Rejon, Is_current)
SELECT 
    P.ID, 
    P.Adres, 
    CAST(P.Telefon AS VARCHAR(16)) AS Telefon,
    P.Rejon, 
	1 AS Is_current
FROM BD_Policja.dbo.Komenda_policji P;
