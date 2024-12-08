DECLARE @startDate DATE = '2022-01-01'
DECLARE @endDate DATE = '2022-03-31'

CREATE TABLE #TempDates (Data DATE)

WHILE @startDate <= @endDate
BEGIN
	INSERT INTO #TempDates (Data)
	VALUES (@startDate)

	SET @startDate = DATEADD(DAY, 1, @startDate)
END

INSERT INTO [HD_Policja].[dbo].[Data](Rok, Numer_miesi�ca, Nazwa_miesi�ca, Dzie�, Czy_dzie�_roboczy)
SELECT
	YEAR(Data) AS Rok,
    MONTH(Data) AS Numer_miesi�ca,
	CASE MONTH(Data)
	    WHEN 1 THEN N'Stycze�'
        WHEN 2 THEN N'Luty'
        WHEN 3 THEN N'Marzec'
        WHEN 4 THEN N'Kwiecie�'
        WHEN 5 THEN N'Maj'
        WHEN 6 THEN N'Czerwiec'
        WHEN 7 THEN N'Lipiec'
        WHEN 8 THEN N'Sierpie�'
        WHEN 9 THEN N'Wrzesie�'
        WHEN 10 THEN N'Pa�dziernik'
        WHEN 11 THEN N'Listopad'
        WHEN 12 THEN N'Grudzie�'
	END AS Nazwa_miesi�ca,
	DAY(Data) AS Dzie�,
	CASE DATEPART(WEEKDAY, Data)
        WHEN 1 THEN 0 -- Niedziela
        WHEN 7 THEN 0 -- Sobota
		ELSE 1
    END AS Czy_dzie�_roboczy
FROM #TempDates

DROP TABLE #TempDates