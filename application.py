from flask import Flask, url_for, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'brolty'
mysql = MySQL(app)

todo_list = []

@app.route('/', methods= ['POST', 'GET'])
def index():
    cur = mysql.connection.cursor()
    #cur.execute('''CREATE TABLE example (id INT, name VARCHAR(20))''')
    #cur.execute('''INSERT INTO example VALUES (1, 'Anthony')''')
    #cur.execute('''INSERT INTO example VALUES (2, 'Rodrigo')''')
    #mysql.connection.commit()
    if request.method == 'POST':
        if request.form['submit_btn'] == 'add_item':
            activity = request.form.get('activity')
            if activity:
                todo_list.append(activity)
        elif request.form['submit_btn'] == 'undo':
            if todo_list:
                todo_list.pop()
        elif request.form['submit_btn'] == 'clear_form':
            todo_list.clear()
    return render_template('index.html', todo_list=todo_list)
