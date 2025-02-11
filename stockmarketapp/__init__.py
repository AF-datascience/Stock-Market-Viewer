from flask import Flask 

# create function app: 
def create_app(): 
    app = Flask(__name__)

    # intiailise the blueprint instances 
    from stockmarketapp.main.routes import main 
    # register the blueprints: 
    app.register_blueprint(main)
    return app 
