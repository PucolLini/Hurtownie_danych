DECLARE @startDate DATE = '2022-01-01'
DECLARE @endDate DATE = '2022-03-31'

CREATE TABLE #TempDates (Data DATE)

WHILE @startDate <= @endDate
BEGIN
	INSERT INTO #TempDates (Data)
	VALUES (@startDate)

	SET @startDate = DATEADD(DAY, 1, @startDate)
END

INSERT INTO [HD_Policja].[dbo].[Data](Rok, Numer_miesi¹ca, Nazwa_miesi¹ca, Dzieñ, Czy_dzieñ_roboczy)
SELECT
	YEAR(Data) AS Rok,
    MONTH(Data) AS Numer_miesi¹ca,
	CASE MONTH(Data)
	    WHEN 1 THEN N'Styczeñ'
        WHEN 2 THEN N'Luty'
        WHEN 3 THEN N'Marzec'
        WHEN 4 THEN N'Kwiecieñ'
        WHEN 5 THEN N'Maj'
        WHEN 6 THEN N'Czerwiec'
        WHEN 7 THEN N'Lipiec'
        WHEN 8 THEN N'Sierpieñ'
        WHEN 9 THEN N'Wrzesieñ'
        WHEN 10 THEN N'PaŸdziernik'
        WHEN 11 THEN N'Listopad'
        WHEN 12 THEN N'Grudzieñ'
	END AS Nazwa_miesi¹ca,
	DAY(Data) AS Dzieñ,
	CASE DATEPART(WEEKDAY, Data)
        WHEN 1 THEN 0 -- Niedziela
        WHEN 7 THEN 0 -- Sobota
		ELSE 1
    END AS Czy_dzieñ_roboczy
FROM #TempDates

DROP TABLE #TempDates