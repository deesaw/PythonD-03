

from mysql.connector import connection

DB_NAME = 'pydbE1x'
cnx = connection.MySQLConnection(user='root', password='hello123',host='127.0.0.1')
mycursor=cnx.cursor()

mycursor.execute("create database {}".format(DB_NAME))



