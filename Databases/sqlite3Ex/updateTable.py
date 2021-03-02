#update
import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
sql = """
UPDATE cars 
SET Carname = 'Maruthi' 
WHERE Id = 3
"""
print('Table updated')
cursor.execute(sql)
conn.commit()
