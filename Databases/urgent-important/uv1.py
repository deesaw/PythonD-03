import sqlite3
conn = sqlite3.connect("mytaskbase.db")
cursor = conn.cursor()
# create a table
sql="""
CREATE TABLE TASKS(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
					TASK TEXT,
					URGENT TEXT,
					IMPORTANT TEXT,
					TS DATE,
					STATUS TEXT) 
"""
cursor.execute(sql)
print("Table Created")
conn.close()
