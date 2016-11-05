import sqlite3

with sqlite3.connect("sample.db") as connection:
        c = connection.cursor()
        c.execute('INSERT INTO posts VALUES("Good", "I`m good.")')
        c.execute('INSERT INTO posts VALUES("Good", "I`m well.")')