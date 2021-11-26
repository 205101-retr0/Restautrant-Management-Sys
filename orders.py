from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify

orders = Blueprint('orders', __name__)

@orders.route('/bill', methods=['GET', 'POST'])
def billing():
    if request.method == 'POST':
        items = request.form.getlist('items')
        quantity = request.form.getlist('item-quantity')
        print(items, quantity)
        ## Make a dictionary of all the orders, their quantities and their prices from items
        dict_to_send ={}
        # for item in items:
        #     menu = item.split('_')[0]
        #     price = item.split('_')[1]
        #     dict_to_send[menu]=price
            
        items = {
            "name" : "tapiceria",
            "price":   "120",
            "quantity": "1",
        }
        
    return render_template('bill.html', items=items)