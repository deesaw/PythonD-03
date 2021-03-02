import sqlite3
import datetime
conn = sqlite3.connect("mytaskbase.db")
cursor = conn.cursor()
now=datetime.datetime.now()
sql="""
INSERT INTO tasks(TASK,URGENT,IMPORTANT,TS) VALUES ("Buy a book",'No','Yes','{}')""".format(str(now))
print(sql)
cursor.execute(sql)
# save data to database
conn.commit()
print("Record Inserted")

print(cursor.execute("select count(*) from tasks").fetchone()[0])

conn.close()
