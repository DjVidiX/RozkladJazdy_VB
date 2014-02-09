# -*- encoding: UTF-8 -*-
import random

import sqlite3

__author__ = 'marek'

def feedTimes(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    data = [[2, 5, 23], [9, 5, 30], [14, 9, 25], [16, 6, 25]]

    counter = 0
    for line in data:
        stop_list = []
        time_list = []
        local_counter = 0
        stop_list.append(line[1])
        stop_list.append(line[2])
        for i in range(15):
            counter += 1
            local_counter += random.randint(1,3)
            stop = random.randint(1,59)
            while stop in stop_list:
                stop = random.randint(1,59)

            stop_list.append(stop)
            time = local_counter
            time_list.append(time)
            values = (counter, line[0], line[1], stop, time)
            cursor.execute("INSERT INTO Czasy VALUES (?, ?, ?, ?, ?)", values)

        counter += 1
        final_time = time+1
        cursor.execute("INSERT INTO Czasy VALUES (?, ?, ?, ?, ?)", (counter, line[0], line[1], line[2], final_time))

        stop_list.reverse()
        local_counter = 0
        for myStop in stop_list:
            if myStop == line [2]:
                continue
            counter += 1
            local_counter += random.randint(1,3)

            values = (counter, line[0], line[2], myStop, local_counter)
            cursor.execute("INSERT INTO Czasy VALUES (?, ?, ?, ?, ?)", values)
    
    conn.commit()

if __name__ == "__main__":
    feedTimes()
