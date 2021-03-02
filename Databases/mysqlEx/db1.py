"""this program shows how to connect to a MySQL database"""
import MySQLdb
# connect to database
mydb = MySQLdb.connect("localhost","user","pass","dbname" )
# get a cursor
mycursor = mydb.cursor()
# run a query
mycursor.execute("SELECT count(*) from words")
# Fetch a single row using fetchone() method.
data = mycursor.fetchone()
print "There are {} words in my database".format( data)
mydb.close()# disconnect from server