UPDATE Pojazd
SET Spalanie = Spalanie + 1.5
WHERE Przebyte_kilometry > 70000;

UPDATE Patrol
SET "Status" = 'nieaktywny'
WHERE ID>=0 AND ID<=5;

UPDATE Komenda_policji
SET Telefon = '666 123 456'
WHERE ID = 0;  

UPDATE Komenda_policji
SET Telefon = '+48 111 222 333'
WHERE ID = 1; 

UPDATE Komenda_policji
SET Telefon = '+48 444 555 666'
WHERE ID = 2; 

UPDATE Komenda_policji
SET Telefon = '777 888 999'
WHERE ID = 3; 

UPDATE Komenda_policji
SET Telefon = '+48 987 654 321'
WHERE ID = 4; 
