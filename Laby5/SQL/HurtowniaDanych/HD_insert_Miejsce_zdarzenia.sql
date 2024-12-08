USE HD_Policja;

INSERT INTO [HD_Policja].[dbo].[Miejsce_zdarzenia] (Miasto, Ulica, Numer)
SELECT 
    RIGHT(P.Lokalizacja, CHARINDEX(' ', REVERSE(P.Lokalizacja)) - 1) AS Miasto, 
    
    LEFT(P.Lokalizacja, 
        CHARINDEX(' ', P.Lokalizacja + ' ', CHARINDEX(' ', P.Lokalizacja) + 1) - 1) AS Ulica, 
    
	TRIM(
        CASE 
            -- Je�li adres zawiera uko�nik '/', bierzemy tylko numer przed uko�nikiem
            WHEN CHARINDEX('/', P.Lokalizacja) > 0 THEN
				LEFT(SUBSTRING(P.Lokalizacja, 
                    PATINDEX('%[0-9]%', P.Lokalizacja), 
                    CHARINDEX('/', P.Lokalizacja) - PATINDEX('%[0-9]%', P.Lokalizacja)), 8) 
            -- Je�li nie zawiera uko�nika, bierzemy numer po pierwszej spacji
            ELSE 
                SUBSTRING(P.Lokalizacja, 
					PATINDEX('%[0-9]%', P.Lokalizacja), 
					CHARINDEX(' ', P.Lokalizacja + ' ', PATINDEX('%[0-9]%', P.Lokalizacja)) - PATINDEX('%[0-9]%', P.Lokalizacja))
        END
    ) AS Numer

FROM BD_Policja.dbo.Zdarzenie P;
