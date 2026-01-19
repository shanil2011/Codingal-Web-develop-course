from flask import Flask, flash, request, render_template, redirect, url_for
import sqlite3
import re

app = Flask(__name__)
app.secret_key = "Secret_key"

db_path = r'D:\Codingal Web develop course\python\Front end of user login Application\database.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, email TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginaction', methods=['POST'])
def loginaction():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/registrationaction', methods=['POST'])
def registrationaction():
    username = str(request.form['username'])
    password = str(request.form['password'])
    email = str(request.form['email'])

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash("User already exists")
        return redirect(url_for("index.html"))
    else:
        cursor.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
            (username, password, email)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("welcome.html"))
    
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=24011)