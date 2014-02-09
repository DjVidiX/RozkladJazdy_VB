# Wszystkie linie
Select Nr_linii From Kursy Group By Nr_linii


# Linie dla podanego przystanku np. 6 (najpierw trzeba wyciagnac z nazwy id)
Select Nr_linii From Czasy Where ID_przystanku=6 GROUP BY Nr_linii


# Przystanki dla podanej linii np. 14
SELECT id_przystanku FROM Czasy WHERE Nr_linii=14

