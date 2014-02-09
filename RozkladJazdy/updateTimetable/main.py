__author__ = 'marek'

import lines_creator, kursy_creator, stops_creator, database_creator


def main():
    name = "database.db"
    database_creator.createDatabase(name)
    stops_creator.feedStops(name)
    kursy_creator.feedKursy(name)
    lines_creator.feedTimes(name)

if __name__ == "__main__":
    main()