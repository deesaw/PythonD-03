from mysql.connector import connection

cnx = connection.MySQLConnection(user='root', password='hello123',host='127.0.0.1',
                                 database='fkdemo')
mycursor=cnx.cursor()
data1=mycursor.execute("SELECT count(*) from categories")
data = mycursor.fetchone()
print( "There are {} records in my database".format(data))
cnx.close()
