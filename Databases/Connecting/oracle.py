import cx_Oracle

dsn_tns = cx_Oracle.makedsn('server', 'port', service_name='service_name')
conn = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

c = conn.cursor()
c.execute('select count(*) from TABLE_NAME')

for row in c:
   print(row)
conn.close()