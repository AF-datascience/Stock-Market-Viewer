# setting out the condition to run the app 
# create app using the function we define in init.py
from stockmarketapp import create_app

# pass in a default config at the moment: 
app = create_app()

# set the main name of the file to be ran: 
if __name__ == "__main__": 
    app.run(debug = True)