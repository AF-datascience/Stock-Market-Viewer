# setting out config variables if needed here: 
# setting out some base environment variables: 
import os

#create config class
class Config: 

    # setting out secret key for the app: 
    SECRET_KEY = '0495ab626e9fad339523510d51e148f67b1506dce278d9ce9135b90170b8ca8a'
    # grab api key from envs
    API_KEY = os.getenv('ALPHA_ADVANTAGE')