import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# enter row id to update
firstname = input('Enter first name: ')
lastname  = input('Enter last name: ')
email     = input('Enter email: ')

# update contact
cursor.execute(f"UPDATE contacts SET firstname = '{firstname}', lastname = '{lastname}' WHERE email = '{email}'")

# commit changes
connection.commit()

# verify data
rows = cursor.execute('SELECT * FROM contacts').fetchall()
print(rows)

# clean up
cursor.close()
connection.close()