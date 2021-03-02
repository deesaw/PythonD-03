import sqlite3
import xlrd

conn = sqlite3.connect("mymarks.db")#connecting to a database
cursor = conn.cursor()
# create a table
sql = """
CREATE TABLE marks(
student text,
english int,
maths int,
science int) 
               """
#cursor.execute(sql) #comment it if u r running more than once
print("Table Created")

wb = xlrd.open_workbook("marks.xlsx")
ws = wb.sheet_by_index(0)


def importxl(xlsheet,dbtable):
    data=[]
    for x in range(xlsheet.nrows):
       data.append(tuple(xlsheet.row_values(x)))
    
    sql = "INSERT INTO {} VALUES (?,?,?,?)".format(dbtable)
    cursor.executemany(sql, data)
    conn.commit()
    print("{} row(s) inserted".format(cursor.rowcount))

importxl(ws,"marks")

sql = "SELECT * FROM marks"
print ("listing of all the records in the table:")
for row in cursor.execute(sql):
    print (row)
 


conn.close()
