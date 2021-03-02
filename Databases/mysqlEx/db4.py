"""this program shows how to connect to a MySQL database
and fetch multiple rows of data using fetchone"""
import sys
import MySQLdb

try:
	mydb = MySQLdb.connect("localhost","root","root","pytho" ) # connect to database
except MySQLdb.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	print "Check your connection string"
	sys.exit(1)

mycursor = mydb.cursor() # get a cursor
mycursor.execute("SELECT * from words")# run a query
	 
while (1):
    row = mycursor.fetchone ()
    if row == None:
      break
    print "%s, %s" % (row[0], row[1])
mydb.close()# disconnect from server