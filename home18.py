import json
import sqlite3
import os


def film_finder(file_name):
    database = os.path.join(os.getcwd(), file_name)
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    find_name = """ SELECT * from film_data
                    where title like "B%"
                    order by rate desc
    """
    result = curs.execute(find_name)
    print(result.fetchall())


def length_finder(file_name):
    database = os.path.join(os.getcwd(), file_name)
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    find_name = """ SELECT * from film_data
                        order by length asc
        """
    result = curs.execute(find_name)
    print(result.fetchall())


def sql_to_json(file_name, json_name):
    database = os.path.join(os.getcwd(), file_name)
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    find_name = """ SELECT * from film_data
    """
    result = curs.execute(find_name)
    with open(json_name, "w") as js:
        json.dump(result.fetchall(), js, indent=2)


sql_to_json("film_data.db", "me_json.json")
length_finder("film_data.db")
film_finder("film_data.db")