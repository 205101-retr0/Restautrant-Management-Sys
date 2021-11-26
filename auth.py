from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import database

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    conn, cur = database.connect_db()
    sql = 'SELECT * FROM employees WHERE username = ?'
    rows = cur.execute(sql, (username,)).fetchone()
    
    if rows is None:
        return render_template('login.html', output='Invalid username')
    else:
        passwd = rows[2]
        if check_password_hash(passwd, password):
            # return render_template('index.html', output='Welcome {}'.format(user))
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html', output='Invalid password')
    