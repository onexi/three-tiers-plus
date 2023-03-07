import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# enter row id to delete
email = input('Enter email: ')

# delete contact
cursor.execute(f"DELETE FROM contacts WHERE email = '{email}'")

# commit changes
connection.commit()

# verify data
rows = cursor.execute('SELECT * FROM contacts').fetchall()
print(rows)

# clean up
cursor.close()
connection.close()