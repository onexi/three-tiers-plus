import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# read data
rows = cursor.execute('SELECT * FROM contacts').fetchall()
print(rows)