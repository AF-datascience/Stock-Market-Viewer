# This is the basic main routes for the home page 
from flask import render_template, Blueprint, current_app
import stockmarketapp
from stockmarketapp.main.utils import query_yfinance, query_alpha_advantage
import requests

# creating a bleuprint - passing in the name like an instance 
main = Blueprint('main', __name__)

# setup the app routes 
# where a user will go to see different pages: 
@main.route("/")
@main.route("/home")
# render the template from the templates directory for the home page: 
def home(): 
    
    # we can query the data from our utils py file 
    # this will return the data from the ticker
    # we can pass this into our template as a first draft
    # example_data = query_yfinance()
    
    # new alpha advantage function: 
    example_data = query_alpha_advantage('AAPL', api_key = current_app.config['API_KEY'])
    
    
    # this renders some dummy data to the screen for now
    # we will change it later on: 
    return render_template("home.html", example_data =example_data)

