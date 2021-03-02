"""this program shows how to connect to a MySQL database
and fetch multiple rows of data using fetchone"""
from mysql.connector import connection
mydb = connection.MySQLConnection(user='root', password='hello123',host='127.0.0.1',
                                 database='fkdemo') # connect to database
mycursor=mydb.cursor() # get a cursor
mycursor.execute("SELECT * from categories")# run a query
	 
while (1):
    row = mycursor.fetchone ()
    if row == None:
      break
    print("{}  {} ".format(row[0], row[1]))
mydb.close()# disconnect from server
