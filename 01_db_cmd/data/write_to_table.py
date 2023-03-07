import sqlite3
import os

# connect to db
connection = sqlite3.connect("contacts.db")

#  create db cursor
cursor = connection.cursor()

# write data to tables
cursor.execute('''
    INSERT INTO contacts VALUES
        ('peter', 'parker', 'peter@mit.edu'),
        ('bruce', 'wayne', 'bruce@mit.edu'),
        ('diana', 'prince', 'diana@mit.edu')
''')

# commit changes
connection.commit()

# verify data
rows = cursor.execute('SELECT * FROM contacts').fetchall()
print(rows)