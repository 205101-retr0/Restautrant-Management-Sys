from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify
import database

orders = Blueprint('orders', __name__)

@orders.route('/bill', methods=['POST'])
def billing():
    if request.method == 'POST':
        items = request.form.getlist('items')
        quantity = request.form.getlist('item-quantity')
        print(items, quantity)
        i=0
        ## Make a dictionary of all the orders, their quantities and their prices from items
        dict_to_send ={}
        
        ## Figure out the logic here
        
        for i, j in zip(items, quantity):
            # print(i)
            if j == '':
                continue
            else:
                dict_to_send[i] = int(j)
        print(dict_to_send)
        
    return render_template('bill.html', items=dict_to_send)

# Make a verify function to verify if the customer is a member

@orders.route('/verify_vip', methods=['POST'])
def verify_vip():
    cphone = request.form['cphone']
    conn, cur = database.connect_db()
    sql = 'SELECT member FROM customer where c_phone = ?'
    # excute the sql command
    rows = cur.execute(sql, (cphone,)).fetchone()
    
    if rows == None:
        flash("Not a member")
        return render_template('menu.html')
    
    if rows[0] == "Yes":
        flash('Eligible for discount of 20%') 
        return render_template('menu.html')
    else:
        flash('Not eligible for discount')
        return render_template('menu.html')
