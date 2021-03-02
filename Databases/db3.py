"""this program shows how to connect to a MySQL database
and fetch multiple rows of data using fetchall"""
import MySQLdb
mydb = MySQLdb.connect("localhost","root","root","python" ) # connect to database
mycursor = mydb.cursor() # get a cursor
mycursor.execute("SELECT * from words")# run a query
print "%d, rows fetched" % mycursor.rowcount # cursor.rowcount gives the count of rows fetched
data = mycursor.fetchall()# Fetch all rows
#now data is a list of lists
#print it to check
print data
#let us print in a readable way
for i in data:
	print i[0],i[1]
mydb.close()# disconnect from server