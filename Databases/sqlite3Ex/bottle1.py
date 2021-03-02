#how to use bottle
from bottle import route, run, request, template,redirect
import os
import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
@route('/')
def hello():
    return "Hey I am bottle here how are you doing?"

@route('/env') #displays environment as table format
def env1():    
    output='<table border=1>'
    for x,y in os.environ.items(): #command to get the environment variables
        output=output +"<tr><td>"+ x +"</td><td>"+ y + "</td></tr>"
    return output + "</table>"

@route('/wish/<name>') #to this route we sending a dynamic name
def wish(name):
    return "Hello {} how are you doing today".format(name)


@route('/cars')
def cars():
    output='<table border=1>'
    tablerow="<tr><td>{}</td><td>{}</td></tr>"
    sql = "SELECT * FROM cars"
    
    for id,carname,price in cursor.execute(sql):
             output+=tablerow.format(carname,price)
    output+="</table>"
    
    #conn.close()
    return output

@route('/addcarsform')
def getcars():
	return 	"""
<html>
<form method=post action="http://localhost:8080/addcar">
<input type=text name=id>id<br>
<input type=text name=carname>carname<br>
<input type=text name=price>price<br>
<input type=submit>
</form>
</html>

	"""
@route('/addcar',method='POST')
def getbook1():
	id=request.forms.get('id')
	carname=request.forms.get('carname')
	price=request.forms.get('price')
	sql="INSERT INTO cars VALUES ({}, '{}','{}')".format(id,carname,price)
	cursor.execute(sql)
	conn.commit()
	redirect('/cars')
	


run(host='localhost', port=8080, debug=True)
