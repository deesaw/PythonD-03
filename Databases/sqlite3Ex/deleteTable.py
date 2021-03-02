import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
DELETE FROM cars
WHERE Id = 3
"""
cursor.execute(sql)
conn.commit()
conn.close()
