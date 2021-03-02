import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# create a table
sql="""
CREATE TABLE books(
id int,
title text,
author text
 ) 
"""
cursor.execute(sql)
print("Table Created")
conn.close()












			   
#################################
import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# insert some data
cursor.execute("INSERT INTO books VALUES (1, 'Wings of Fire', \
 'Abdul Kalam')")
# save data to database
conn.commit()
# insert multiple records using the more secure "?" method
mybooks = [(2, 'My Experiments with Truth', 'M K Gandhi'),
          (3, 'Discovery of India', 'J Nehru'),
		  (4, 'My Experiments with Food', 'Ramesh S')]
cursor.executemany("INSERT INTO books VALUES (?,?,?)", mybooks)
conn.commit()
conn.close()






++++++++++++

import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
UPDATE books 
SET author = 'Jawaharlal Nehru' 
WHERE id = 3
"""
cursor.execute(sql)
conn.commit()






+++++++++++++++++++

import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
DELETE FROM books
WHERE id = 4
"""
cursor.execute(sql)
conn.commit()






++++++++++++++++

import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
print "listing of all the records in the table:"
for row in cursor.execute("SELECT * FROM books"):
    print row
 
print "Results"
sql = "SELECT * FROM books"
cursor.execute(sql)
for id,bookname,author in cursor.fetchall():
	print "The book {} was written by {}".format(bookname,author)
	
sql = "SELECT * FROM books where id = 2"
cursor.execute(sql)

print(cursor.fetchone())
conn.close()



