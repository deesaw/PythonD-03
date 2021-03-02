import pymssql

conn = pymssql.connect(server=server, user=user, password=password, database=db)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(MemberID) as count FROM Members WHERE id = 1")
row = cursor.fetchone()  # returns first found record
# row = cursor.fetchall()  # returns all matched queries

conn.close()

print(row)