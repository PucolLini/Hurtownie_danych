USE HD_Policja;

INSERT INTO [HD_Policja].[dbo].[Miejsce_zdarzenia] (Miasto, Ulica, Numer)
SELECT 
    RIGHT(P.Lokalizacja, CHARINDEX(' ', REVERSE(P.Lokalizacja)) - 1) AS Miasto, 
    
    LEFT(P.Lokalizacja, 
        CHARINDEX(' ', P.Lokalizacja + ' ', CHARINDEX(' ', P.Lokalizacja) + 1) - 1) AS Ulica, 
    
	TRIM(
        CASE 
            -- Jeœli adres zawiera ukoœnik '/', bierzemy tylko numer przed ukoœnikiem
            WHEN CHARINDEX('/', P.Lokalizacja) > 0 THEN
				LEFT(SUBSTRING(P.Lokalizacja, 
                    PATINDEX('%[0-9]%', P.Lokalizacja), 
                    CHARINDEX('/', P.Lokalizacja) - PATINDEX('%[0-9]%', P.Lokalizacja)), 8) 
            -- Jeœli nie zawiera ukoœnika, bierzemy numer po pierwszej spacji
            ELSE 
                SUBSTRING(P.Lokalizacja, 
					PATINDEX('%[0-9]%', P.Lokalizacja), 
					CHARINDEX(' ', P.Lokalizacja + ' ', PATINDEX('%[0-9]%', P.Lokalizacja)) - PATINDEX('%[0-9]%', P.Lokalizacja))
        END
    ) AS Numer

FROM BD_Policja.dbo.Zdarzenie P;
