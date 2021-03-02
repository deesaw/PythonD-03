import sqlite3

conn = sqlite3.connect("mytaskbase.db")
cursor = conn.cursor()
sql="select * from tasks"
cursor.execute(sql)

for row in cursor.fetchall():
	print(row)



conn.close()

