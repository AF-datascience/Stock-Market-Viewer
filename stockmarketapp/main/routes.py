# This is the basic main routes for the home page 
from flask import render_template, Blueprint, current_app
import stockmarketapp
from stockmarketapp.main.utils import query_finazon

# creating a bleuprint - passing in the name like an instance 
main = Blueprint('main', __name__)

# setup the app routes 
# where a user will go to see different pages: 
@main.route("/", methods = ['GET', 'POST'])
@main.route("/home")
# render the template from the templates directory for the home page: 
def home(): 
    
    # we can query the data from our utils py file 
    # this will return the data from the ticker
    # we can pass this into our template as a first draft
    # example_data = query_yfinance()
    
    # new alpha advantage function: 
    # ticker_df = query_alpha_advantage('AAPL', api_key = current_app.config['API_KEY'])
    # # get ticker name
    # ticker_name = ticker_df['Meta Data']['2. Symbol']
    # # get close prices: 
    # ticker_dict = {}
    # for key, value in ticker_df['Time Series (Daily)'].items(): 
    #     ticker_dict[key] = value['4. close']
    
    # use finazon web query api code: 
    ticker_name, ticker_dates, ticker_values, temp_data = query_finazon(api_key=current_app.config['FINAZON_API_KEY'])
    
    
    # this renders some dummy data to the screen for now
    # we will change it later on: 
    # return render_template("home.html", ticker_dict = ticker_dict, ticker_name = ticker_name)
    return render_template("home.html", ticker_name = ticker_name, labels = ticker_dates, 
                           data = ticker_values, temp_data = temp_data)


# new route which has a linking feature 
# this will take a user to a page for that specific stock 
# they click "go to this stock button" 

@main.route("/stock/<name>", methods = ['GET'])
def go_to_stock(name):

    # use finazon web query api code: 
    ticker_name, ticker_dates, ticker_values, temp_data = query_finazon(api_key=current_app.config['FINAZON_API_KEY'])
    
    name = ticker_name 

