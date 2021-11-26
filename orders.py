from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify

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