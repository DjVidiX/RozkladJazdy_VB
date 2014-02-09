__author__ = 'marek'

import sqlite3

def createDatabase(name):
    conn = sqlite3.connect(name)

    cursor = conn.cursor()

    stops_delete = "DROP TABLE IF EXISTS Przystanek"
    stops="""CREATE TABLE Przystanek(
                Id INTEGER PRIMARY KEY,
                nazwa TEXT
            );"""

    kursy_delete = "DROP TABLE IF EXISTS Kursy"
    kursy = """CREATE TABLE Kursy (
                Id INTEGER PRIMARY KEY,
                Nr_linii INTEGER,
                Godzina_odjazdu_DR TEXT,
                Godzina_odjazdu_S TEXT,
                Godzina_odjazdu_N TEXT,
                Poczatkowy_przystanek INTEGER,
                Koncowy_przystanek INTEGER,
                FOREIGN KEY(Poczatkowy_przystanek) REFERENCES Przystanek(Id),
                FOREIGN KEY(Koncowy_przystanek) REFERENCES Przystanek(Id)
            );"""

    linie_delete = "DROP TABLE IF EXISTS Czasy"
    linie = """CREATE TABLE Czasy (
                Id INTEGER PRIMARY KEY,
                Nr_linii INTEGER,
                Bazowa_stacja INTEGER,
                ID_przystanku INTEGER,
                Czas INTEGER,
                FOREIGN KEY(Bazowa_stacja) REFERENCES Przystanek(Id),
                FOREIGN KEY(ID_przystanku) REFERENCES Przystanek(Id)
            );"""

    cursor.execute(stops_delete)
    cursor.execute(stops)
    cursor.execute(kursy_delete)
    cursor.execute(kursy)
    cursor.execute(linie_delete)
    cursor.execute(linie)

    conn.commit()

if __name__ == "__main__":
    createDatabase()


