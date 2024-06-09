

import sqlite3

database = sqlite3.connect("articles.db")

cursor = database.cursor()

# cursor.execute(''' CREATE TABLE articles(
#             title TEXT,
#             author TEXT,
#             views INTEGER)
#             ''')

# cursor.execute("INSERT INTO articles VALUES ('Про користь тараканів', 'Yevhen Goly', 10500)")
# cursor.execute("INSERT INTO articles VALUES ('Про користь розводення корів в квартирі', 'Max Chornobuk', 51)")
# cursor.execute("INSERT INTO articles VALUES ('Про користь дружби з картопляною імперією', 'Yevheniy Buryak', 501)")
# cursor.execute("INSERT INTO articles VALUES ('Про користь влаштування локального апокаліпсисів', 'Khrystyna Gannoshyna', 3500)")

cursor.execute("SELECT * FROM articles")

data = cursor.fetchall()
print(data)


cursor.execute("SELECT * FROM articles")
data = cursor.fetchmany(2)
print(data)

cursor.execute("SELECT * FROM articles")
data = cursor.fetchone()
print(data)

print (f'Стаття "{data[0]}", автор - {data[1]}, переглядів - {data[2]}')

cursor.execute("SELECT title FROM articles")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT author FROM articles")
data = cursor.fetchall()
print(data)
cursor.execute("SELECT title, views FROM articles")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT rowid, title FROM articles")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT title, views FROM articles")
data = cursor.fetchmany(2)[0][0]
print(data)

cursor.execute("SELECT title, views FROM articles WHERE views < 10000")
data =  cursor.fetchall()
print(data)

cursor.execute("SELECT title, author FROM articles WHERE views > 3000")
data =  cursor.fetchall()
print("\n Статті з великою кількість переглядів")
for article in data:
    print (f"Назва - {article[0]}, автор - {article[1]}")


# cursor.execute("DELETE FROM articles WHERE views < 3000")
# cursor.execute("SELECT * FROM articles")
# data =  cursor.fetchall()
# print(data)
#
#
# cursor.execute("DELETE FROM articles ")
# cursor.execute("SELECT * FROM articles")
# data =  cursor.fetchall()
# print(data)


cursor.execute("UPDATE articles SET author = 'Ivan Shamrikov' WHERE author = 'Khrystyna Gannoshyna' ")
cursor.execute("SELECT * FROM articles")
data = cursor.fetchall()
print(data)


# database.commit()
database.close()