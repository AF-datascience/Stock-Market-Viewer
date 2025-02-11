# utility functions
# designed for querying the data from the yfinance package
# and also for any other functions that we make: 

import yfinance as yf 

# function to query yfinance package 
# take in a ticker - set default to Apple: 
def query_yfinance(ticker = "AAPL", period = "3mo"): 
    # get the ticket data: 
    dat = yf.Ticker(ticker)
    # return 3 months worth of close data: 
    dat = dat.history(period = period)['Close']

    return dat

