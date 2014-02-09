__author__ = 'marek'
# -*- encoding: UTF-8 -*-

import sqlite3
import random

__author__ = 'marek'

def feedKursy(name):
    conn = sqlite3.connect(name)

    cursor = conn.cursor()

    ids = [[5,30, 9], [5,23, 2], [9,25, 14], [6,25, 16]]

    counter = 0
    for id in ids:
        for i in range(10):
            counter += 1
            time = random.randint(0,1).__str__() + random.randint(0,9).__str__() + ":" + random.randint(0,5).__str__()  + random.randint(0,9).__str__()
            time2 = random.randint(0,1).__str__() + random.randint(0,9).__str__() + ":" + random.randint(0,5).__str__()  + random.randint(0,9).__str__()
            time3 = random.randint(0,1).__str__() + random.randint(0,9).__str__() + ":" + random.randint(0,5).__str__()  + random.randint(0,9).__str__()
            p = random.randint(0,1)
            values = (counter, id[2], time, time2, time3, id[p], id[1-p])
            cursor.execute("INSERT INTO Kursy VALUES (?, ?, ?, ?, ?, ?, ?)", values)

    conn.commit()

if __name__ == "__main__":
    feedKursy()
