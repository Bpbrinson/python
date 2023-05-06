#!/bin/python

from flask import Flask, render_template
import pymysql

app = Flask(__name__)

app.config['DATABASE_HOST'] = 'finance.c2kupgap5up8.us-east-1.rds.amazonaws.com'
app.config['DATABASE_NAME'] = 'finance'
app.config['DATABASE_USER'] = 'Brandon'
app.config['DATABASE_PASSWORD'] = 'PfjRn7jk7598'
app.config['DATABASE_PORT'] = 3306

def connect_to_database():
    conn = pymysql.connect(
        host=app.config['DATABASE_HOST'],
        database=app.config['DATABASE_NAME'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        port=app.config['DATABASE_PORT'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/finance.html')
def finance():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM financial_data')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('finance.html', data=data)

@app.route('/aspirations.html')
def aspirations():
    return render_template('aspirations.html')

app.run(host="0.0.0.0", port=8080)

