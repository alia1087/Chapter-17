# import the requisite modules
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "books.db")


# establish a connection
connection = sqlite3.connect(db_path)
#create a cursor object
cursor = connection.cursor()

# Select all authors last names from the authors table in descending order.
print("Authors last names in descending order")
res = cursor.execute("SELECT last FROM authors order by last desc")
# get the data
data=res.fetchall()
for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')


# "book titles from the titles table in ascending order.
print("book titles from the titles table in ascending order.\n")
res = cursor.execute("SELECT title FROM titles order by title asc")
# get the data
data=res.fetchall()
for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')


# books for a specific author. Include the title,copyright year and ISBN. Order the information alphabetically by title.
print(" books for a specific author. Include the title,copyright year and ISBN. Order the information alphabetically by title. \n")
res = cursor.execute("""
SELECT titles.title,titles.copyright,titles.edition,titles.isbn from titles 
inner join author_ISBN on author_ISBN.isbn = titles.isbn inner join authors on authors.id=author_ISBN.id where
authors.id=3 order by titles.title asc """)
# get the data
data=res.fetchall()
for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')


# Inserting a record in the authors table
print("Inserting a record in the authors table.\n")
res = cursor.execute("insert into authors (first,last)values('Henrik','Ibsen')")
res = cursor.execute("""select * from authors""")
# get the data
data=res.fetchall()
for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')


# Insert a new title for an author. Remember that the book must have an entry
#in the author_ISBN table and an entry in the titles table.
print(" Insert a new title for an author.")
res = cursor.execute("insert into titles (isbn,title,edition,copyright)values('0235404673','An Enenmy Of the People',1,'1883')")
res = cursor.execute("insert into author_ISBN (id,isbn)values(4,'0235404673')")


# book titles from the titles table in ascending order
print("book titles from the titles table in ascending order.")
res = cursor.execute("SELECT * FROM titles order by title asc")
# get the data
data=res.fetchall()
for row in data:
    print('\t'.join([str(x) for x in row])),
    print('')
print('\n')