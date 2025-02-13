from flask import Flask 
from stockmarketapp.config import Config

# create function app: 
def create_app(): 
    # create app
    app = Flask(__name__)

    # create config elements: 
    app.config.from_object(Config)
    # intiailise the blueprint instances 
    from stockmarketapp.main.routes import main 
    # register the blueprints: 
    app.register_blueprint(main)
    return app 
