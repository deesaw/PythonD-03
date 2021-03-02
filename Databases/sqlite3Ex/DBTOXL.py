#Database Assignment from data table to xls
import sqlite3
import xlwt

#Reading
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = """
SELECT * from cars
"""
cars = cursor.execute(sql)

#Exporting to xls

wb = xlwt.Workbook()
sheet1 = wb.add_sheet('carsDetails')

for row, data in enumerate(cars):  
    print(row, data)
    for col, cellvalue in enumerate(data):
        sheet1.write(row, col, cellvalue)    
wb.save('car.xls')
conn.close()
