USE HD_Policja;

INSERT INTO [HD_Policja].[dbo].[Pojazd] (Nr_rejestracyjny, Typ, Stan_techniczny, Marka, Model, Spalanie, Rok_produkcji, Is_current)
SELECT 
    P.Numer_rejestracyjny, 
    P.Typ, 
    P.Stan_techniczny,
    P.Marka, 
    P.Model,
    CASE 
        WHEN P.Spalanie >= 4 AND P.Spalanie < 10 THEN 'ma³e'
        WHEN P.Spalanie >= 10 AND P.Spalanie < 20 THEN 'œrednie'
        WHEN P.Spalanie >= 20 AND P.Spalanie <= 100 THEN 'du¿e'
        ELSE 'inne'
    END AS Spalanie,
    CAST(P.Rok_produkcji AS VARCHAR(4)) AS Rok_produkcji, 
	1 AS Is_current
FROM BD_Policja.dbo.Pojazd P;
