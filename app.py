from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = '3.82.101.125'
app.config['MYSQL_USER'] = 'support'
app.config['MYSQL_PASSWORD'] = 'sistemas20.'
app.config['MYSQL_DB'] = 'BDAlbum' #db_album
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM album')
    data=cur.fetchall()
    return render_template('index.html', albums = data)
