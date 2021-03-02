import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = "SELECT * FROM cars"
print ("listing of all the records in the table:")
for row in cursor.execute(sql):
    print (row)
 
print ("Results...")

cursor.execute(sql)
print(len(cursor.fetchmany(3)))
for id,carname,price in cursor.fetchall():
	print ("The car is {} and its price is {}".format(carname,price))

print('***********')
cursor.execute(sql)
print(cursor.fetchmany(3))
#for id,carname,price in t:
#	print ("The car is {} and its price is {}".format(carname,price))

   
conn.close()
'''
fetchmany(2)
fetchone()
fetchall()

'''