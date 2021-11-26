from flask import Flask

def create_app():
    ## Configure Flask app
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'md5(something)'

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from customer import customer as customers_blueprint
    app.register_blueprint(customers_blueprint)
    
    from orders import orders as orders_blueprint
    app.register_blueprint(orders_blueprint)
        
    return app

app = create_app()

app.run(debug=True)