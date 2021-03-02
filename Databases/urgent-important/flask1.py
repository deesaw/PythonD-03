from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wish/<username>')
def wish(username):
    return "Hello " + username

@app.route('/book/<int:book_id>')
def show_post(book_id):
    # show the book with the given id, the id is an integer
    return str(book_id)
	
@app.route('/tasks/')
def get_tasks():
	import sqlite3
	conn = sqlite3.connect("mytaskbase.db")
	cursor = conn.cursor()
	sql="select * from tasks"
	cursor.execute(sql)
	output=""
	for row in cursor.fetchall():
		output+=str(row)
	conn.close()
	return output
	
@app.route('/addtaskform/')
def print_task_add_form():
	html="""
<html>
<form method=post action="http://127.0.0.1:5000/addtask">
<input type=text name=task> Task<br>
<input type=checkbox name=important> Important<br>
<input type=checkbox name=urgent> Urgent<br>
<input type=submit>
</form>
</html>
	"""
	return html

@app.route('/addtask',methods=['POST'])
def add_task():
	task=request.form.get("task")
	imp="Yes" if request.form.get("important") else "No"
	urg="Yes" if request.form.get("urgent") else "No"
		
	import sqlite3
	import datetime
	conn = sqlite3.connect("mytaskbase.db")
	cursor = conn.cursor()
	now=datetime.datetime.now()
	sql="""
	INSERT INTO tasks(TASK,URGENT,IMPORTANT,TS) VALUES ("{}","{}","{}",'{}')""".format(task,urg,imp,str(now))

	cursor.execute(sql)
	# save data to database
	conn.commit()
	return redirect(url_for('task_list'))


@app.route('/tasklist/')
def task_list():
	import sqlite3
	conn = sqlite3.connect("mytaskbase.db")
	cursor = conn.cursor()
	sql="select * from tasks"
	cursor.execute(sql)
	output="<table border=1>"
	output+="<tr><td>Task</td><td>Urgent</td><td>Important</td></tr>"
	for tid,task,urg,imp,ts,status in cursor.fetchall():
		output+="<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(task,urg,imp)
	conn.close()
	output+="</table>"
	return output

@app.route('/taskmatrix/')
def task_matrix():
	import sqlite3
	conn = sqlite3.connect("mytaskbase.db")
	cursor = conn.cursor()
	sql="select task from tasks where urgent='Yes' and important='Yes'"
	cursor.execute(sql)
	urg_yes_imp_yes=""
	for task in cursor.fetchall():
			urg_yes_imp_yes+=task[0]+"<br>"
	
	sql="select task from tasks where urgent='Yes' and important='No'"
	cursor.execute(sql)
	urg_yes_imp_no=""
	for task in cursor.fetchall():
			urg_yes_imp_no+=task[0]+"<br>"
	
	sql="select task from tasks where urgent='No' and important='Yes'"
	cursor.execute(sql)
	urg_no_imp_yes=""
	for task in cursor.fetchall():
			urg_no_imp_yes+=task[0]+"<br>"
	
	sql="select task from tasks where urgent='No' and important='No'"
	cursor.execute(sql)
	urg_no_imp_no=""
	for task in cursor.fetchall():
			urg_no_imp_no+=task[0]+"<br>"
	conn.close()
	html="""
	<table border=1>
	<tr>
	<td>Important-Urgent<br>{}</td>
	<td>Important-Not Urgent<br>{}</td>
	</tr>
	<tr>
	<td>Not Important-Urgent<br>{}</td>
	<td>Not Important-Not Urgent<br>{}</td>
	</tr>
	</table>
	""".format(urg_yes_imp_yes,urg_no_imp_yes,urg_yes_imp_no,urg_no_imp_no)
	return html
