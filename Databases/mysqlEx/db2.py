"""this program shows how to insert rows into a MySQL database"""
import MySQLdb
mydb = MySQLdb.connect("localhost","root","root","python" ) # connect to database
mycursor = mydb.cursor() # get a cursor
sql = """insert into words(word) values('tiger')"""
try:
    mycursor.execute(sql)
    mydb.commit() # commit changes
except:
    mydb.rollback() # rollback in case of error
finally:
	mydb.close()# disconnect from server