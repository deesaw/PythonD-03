"""this program shows how to connect to a MySQL database
and fetch multiple rows of data using fetchall"""
from mysql.connector import connection
mydb = connection.MySQLConnection(user='root', password='hello123',host='127.0.0.1',
                                 database='fkdemo') # connect to database
mycursor=mydb.cursor() # get a cursor

mycursor.execute("SELECT * from categories")# run a query
data = mycursor.fetchall()
print(data)
#let us print in a readable way
for i in data:
	print( i[0],i[1])
mydb.close()# disconnect from server
