#!/bin/python

from flask import Flask, render_template, request, redirect, url_for
import pymysql
from datetime import datetime

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

@app.route('/budget.html')
def budget():
    return render_template('budget.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    date = request.form['date']
    boa_checking = float(request.form['boa_checking'])
    boa_savings_vacation = float(request.form['boa_savings_vacation'])
    boa_savings_apt = float(request.form['boa_savings_apt'])
    boa_credit = float(request.form['boa_credit'])
    boa_statement = float(request.form['boa_statement'])
    amex_credit = float(request.form['amex_credit'])
    amex_statement = float(request.form['amex_statement'])
    capital_one_venture_x = float(request.form['capital_one_venture_x'])
    capital_one_venture_x_statement = float(request.form['capital_one_venture_x_statement'])
    capital_one_savor = float(request.form['capital_one_savor'])
    capital_one_savor_statement = float(request.form['capital_one_savor_statement'])
    total_credit_debt = float(request.form['total_credit_debt'])
    total_amount = float(request.form['total_amount'])
    etrade = float(request.form['etrade'])

    connection = connect_to_database()

    cursor = connection.cursor()
    sql = "INSERT INTO financial_data (date, boa_checking, boa_savings_vacation, boa_savings_apt, boa_credit, boa_statement, amex_credit, amex_statement, capital_one_venture_x, capital_one_venture_x_statement, capital_one_savor, capital_one_savor_statement, total_credit_debt, total_amount, etrade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (date, boa_checking, boa_savings_vacation, boa_savings_apt, boa_credit, boa_statement, amex_credit, amex_statement, capital_one_venture_x, capital_one_venture_x_statement, capital_one_savor, capital_one_savor_statement, total_credit_debt, total_amount, etrade))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('finance'))

@app.route('/food_form', methods=['POST'])
def food_form():
    date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    meal = request.form['meal']
    food = request.form['food']
    amount = float(request.form['amount'])
    card_used = request.form['card_used']

    connection = connect_to_database()

    cursor = connection.cursor()
    sql = "INSERT INTO food_data (date, meal, food, amount, card_used) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (date, meal, food, amount, card_used))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('budget'))


@app.route('/view')
def finance():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM food_data')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('budget.html', data=data)


app.run(host="0.0.0.0", port=8080)

