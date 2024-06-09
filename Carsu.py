

import sqlite3


database = sqlite3.connect("cars.db")

cursor = database.cursor()


# cursor.execute('''CREATE TABLE cars (
#             brends TEXT,
#             model TEXT,
#             price INTEGER DEFAULT 0)
#             ''')

cursor.execute("INSERT INTO cars VALUES ('Toyota', 'Corolla', 34000)")
cursor.execute("INSERT INTO cars VALUES ('Toyota', 'Rav4', 27700)")
cursor.execute("INSERT INTO cars VALUES ('Toyota', 'Land Cruice', 85230)")

cursor.execute("INSERT INTO cars VALUES ('Volkswagen', 'Toureg', 70600)")
cursor.execute("INSERT INTO cars VALUES ('Volkswagen', 'Golf', 32320)")
cursor.execute("INSERT INTO cars VALUES ('Volkswagen', 'Tiguan', 40052)")

cursor.execute("INSERT INTO cars VALUES ('Ford', 'Mustang', 53100)")
cursor.execute("INSERT INTO cars VALUES ('Ford', 'Kuga', 31290)")
cursor.execute("INSERT INTO cars VALUES ('Ford', 'Ranger', 61760)")




database.commit()
database.close()
