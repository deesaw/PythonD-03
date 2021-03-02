import psycopg2

conn = psycopg2.connect(database=db, user=user, password=password, host=host, port="5432")
cursor = conn.cursor()

cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
row = cursor.fetchone()    # returns first found record
# row = cursor.fetchall()  # returns all matched queries

conn.close()

print(row)