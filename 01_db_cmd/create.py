import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

firstname = input('Enter first name: ')
lastname  = input('Enter last name: ')
email     = input('Enter email: ')

# write to table
cursor.execute(f"INSERT INTO contacts VALUES ('{firstname}', '{lastname}', '{email}')")

# commit changes
connection.commit()

# verify data
rows = cursor.execute('SELECT * FROM contacts').fetchall()
print(rows)

# clean up
cursor.close()
connection.close()