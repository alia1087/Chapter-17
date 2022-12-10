# import the requisite modules
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "books.db")


# establish a connection
connection = sqlite3.connect(db_path)

#create a cursor object
cursor = connection.cursor()

# query the database
res = cursor.execute("SELECT * FROM titles")

# get the data
data=res.fetchall()

# cursor description
desc=cursor.description

print(desc)

# get column names
names = list(map(lambda x: x[0],desc))
print('Column names ')

print(names)
print('\n')

# print the table columns


print('\t '.join([str(x) for x in names]))


# printing the data

for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')







