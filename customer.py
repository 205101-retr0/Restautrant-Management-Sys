from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
import database

customer = Blueprint('customer', __name__)

@customer.route('/vip_customer', methods=['GET', 'POST'])
def vip_customer():
    return render_template('vip_cus.html')

@customer.route('/search_vip', methods=['POST'])
def search_vip():
    name = request.form['name']
    
    cur = database.connect_db()
    sql = 'SELECT * FROM customer WHERE name = ?'
    rows = cur.execute(sql, (name,)).fetchone()
    print(rows)
    
    if rows is None:
        flash('No such customer')
        return render_template('vip_cus.html')
    else:
        vip = rows[2]
        if vip == "Yes":
            flash("This customer is a Member") 
            return render_template('vip_cus.html')
        else:
            flash("This customer is NOT a Member")
            return render_template('vip_cus.html')
        
@customer.route('/add_vip', methods=['GET', 'POST'])
def add_vip():
    if request.method == 'GET':
        return render_template('add_cus.html')
    
    name = request.form['name']
    cphone = request.form['cphone']

    conn, cur = database.connect_db()
    
    sql = 'Insert into customer (c_phone, name, member) values (?, ?, ?)'
    
    cur.execute(sql, (cphone, name, "Yes"))
    conn.commit()
    
    flash("New VIP added")
    return render_template('add_cus.html')
    ## Do we make a new page for adding VIP?
    # or do we make something up right here?