# Printing Lists as Tabular Data
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

# Console colors - rick pythong package
# https://github.com/willmcgugan/rich

# Markdown tables - Github syntax
# https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables

import sqlite3
from tabulate import tabulate

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# read data
rows = cursor.execute('SELECT * FROM contacts').fetchall()

# get column names
field_names = [i[0] for i in cursor.description]

# print using tabulate
print(tabulate(rows, headers=field_names,tablefmt='github'))

# clean up
cursor.close()
connection.close()