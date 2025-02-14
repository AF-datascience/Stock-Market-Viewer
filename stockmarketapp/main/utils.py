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
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={api_key}'
    #get request back
    r = requests.get(url)
    # get the data : 
    data = r.json()

    return data

# quyery the new finazon website api 
# this has a rate limit of 800 calls which shoul dbe enough 
# for this project: 

def query_finazon(ticker = "AAPL", api_key = None): 

    # generate url for API request; 
     # generate url for API request: 
    url = f'https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&apikey={api_key}&dp=2&start_date=2010-01-01'
    #get request back
    r = requests.get(url)
    # get the data: 
    data = r.json()
    # format the data into something useful for the flask app
    ticker_name = data['meta']['symbol']
    # ticker data in datetime format: close prices
    ticker_dates = [] 
    ticker_values = []
    for value in data['values']: 
            ticker_dates.append(value['datetime'])
            ticker_values.append(value['close'])

    # reverse the dates as these are most recent -> oldest: 
    ticker_dates.reverse()
    ticker_values.reverse()

    # define plot data: 

    return ticker_name, ticker_dates, ticker_values