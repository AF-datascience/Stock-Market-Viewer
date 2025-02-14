# This script is just to develop some code chunks 
# this logic does go into the application 
# but it's more for a testing space e.g. checking functions etc
from utils import query_alpha_advantage
# import api query 
df = query_alpha_advantage()
# construct new dict
new_dict = {}
# get the name of the Ticker
# ticker_name = df['Meta Data']['2. Symbol']
# get the close prices: 

for key, value in df['Time Series (Daily)'].items():
    # these are the dates and close prices
    new_dict[key] = value['4. close']


print([type(k) for k in new_dict.keys()])
