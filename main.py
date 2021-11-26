from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def to_login():
    return redirect(url_for('auth.login'))


@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

@main.route('/orders')
def orders():
    return redirect(url_for('orders.orders'))

@main.route('/vip_customers')
def vip_customers():
    return redirect(url_for('customer.vip_customers'))


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/login')
# def login():
#     if request.user.is_authenticated():
#         pass
#     return render_template('login.html')

# @app.route('/menu', methods=['GET', 'POST'])
# def menu():
#     return "THIS IS MENU PAGE"


# @app.route('/orders', methods=['GET', 'POST'])
# def orders():
#     return "THIS IS ORDERS PAGE"


# @app.route('/vip_customer', methods=['GET', 'POST'])
# def vip_customer():
#     return "THIS IS VIP PAGE"


# if __name__ == '__main__':
#     main.run(debug=True)
