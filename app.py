import mysql.connector as mysql
from tabulate import tabulate
from flask import Flask, render_template, request

app = Flask(__name__)
HOST = 'localhost'
DATABASE = 'appTest1'
USER = 'app1.0.0'
PASSWORD = ''

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print('db connection successful')
cursor = db_connection.cursor()



@app.route("/", methods=['POST' , 'GET'])
def index():
    if request.method =='POST':
        user_details = []
        username = request.form['username']
        password = request.form['password']

        def create_username(user_details):
            user_details.append(username)
            user_details.append(password)
        create_username(user_details)
        print(user_details)
        print('successfully added to list')

        sql_statement = "insert into users (username, password) values (%s,%s)"
        cursor.execute (sql_statement,user_details)
        db_connection.commit()
        print('user successfully added')
    return render_template('index.html')

@app.route('/button/')
def button():
    return 'it works'

if __name__ == '__main__':
    app.run(debug=True)
