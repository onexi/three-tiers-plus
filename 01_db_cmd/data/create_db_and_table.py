import sqlite3
import os

# check if db exists
if os.path.exists("contacts.db"):
    os.remove("contacts.db")

# connect to db
connection = sqlite3.connect("contacts.db")

#  create db cursor
cursor = connection.cursor()

# create table
rows = cursor.execute('''
    CREATE TABLE contacts(
        firstname, 
        lastname, 
        email)
''')

# verify table creation
rows = cursor.execute('SELECT name FROM sqlite_master').fetchall()
print(rows)

