# utility functions
# designed for querying the data from the yfinance package
# and also for any other functions that we make: 

import yfinance as yf 
import requests

# function to query yfinance package 
# take in a ticker - set default to Apple: 
def query_yfinance(ticker = "AAPL", period = "3mo"): 
    # get the ticket data: 
    dat = yf.Ticker(ticker)
    # return 3 months worth of close data: 
    dat = dat.history(period = period)['Close']

    return dat

# functiont to query the alpha advantage API 
# API is rate limited at 25 class a day 
# maybe make a decorator that captures this info later? 

def query_alpha_advantage(ticker = "AAPL", api_key = None): 
    # generate url for API request: 
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}'
    #get request back
    r = requests.get(url)
    # get the data : 
    data = r.json()

    return data