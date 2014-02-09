# -*- encoding: UTF-8 -*-

import sqlite3

__author__ = 'marek'

def feedStops(name):
    conn = sqlite3.connect(name)

    cursor = conn.cursor()
    
    data = [u"Górczyn", u"Sielska", u"Krauthofera", u"Głogowska/Hetmańska", u"Rynek Łazarski", u"Park Wilsona", u"Dworzec Zachodni", u"Most Dworcowy", u"Most Teatralny", u"Słowiańska", u"Aleje Solidarności", u"Lechicka/Poznań Plaza", u"Kurpińskiego", u"Szymanowskiego", u"Os. Sobieskiego", u"Dębiec", u"Wspólna", u"HCP", u"Traugutta", u"Pamiątkowa", u"Kosińskiego", u"Rynek Wildecki", u"Różana", u"Półwiejska", u"AWF", u"Łąkowa", u"Pl. Wiosny Ludów", u"Marcinkowskiego", u"Plac Wolności", u"Fredry", u"Most Teatralny", u"Rynek Jeżycki", u"Polna", u"Żeromskiego", u"Ogrody", u"Fredry", u"Gwarna", u"Marcinkowskiego", u"Wrocławska", u"Pl. Bernardyński", u"Most św. Rocha", u"Politechnika", u"Kórnicka", u"Polanka", u"os. Tysiąclecia", u"Os. Lecha", u"Piaśnicka/Rynek", u"Piaśnicka/Kurlandzka", u"Szwedzka", u"Szwajcarska", u"Franowo", u"Dębiec", u"Wspólna", u"HCP", u"Traugutta", u"Pamiątkowa", u"Kosińskiego", u"Rynek Wildecki", u"Różana", u"Półwiejska", u"AWF", u"Łąkowa", u"Pl. Wiosny Ludów", u"Marcinkowskiego", u"Plac Wolności", u"Fredry", u"Most Teatralny", u"Poznańska", u"Wielkopolska", u"Klin", u"Nad Wierzbakiem", u"Sołacz", u"Uniwersytet Przyrodniczy", u"Bonin", u"św. Leonarda", u"Wrzoska", u"Szpital Lutycka", u"Piątkowska"]

    stops_set = set(data)
    stops = list(stops_set)
    stops.sort()

    counter = 0
    for stop in stops:
        counter += 1
        value = (counter, stop)
        cursor.execute("INSERT INTO Przystanek VALUES (?, ?)", value)

    conn.commit()

if __name__ == "__main__":
    feedStops()
