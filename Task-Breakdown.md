# Basic Flask App Layout 
1. Create Python environment for this project and git repo
2. Create general flask app layout structure
3. Create application factory for Flask app

# Basic Landing Page 
1. Create public landing page 
    1. create home.html template and routes
2. Find a way to get financial ticker data 
    1. From an API 
    2. From a Python package 
3. Create function that grabs ticker data for a hardcoded ticker symbol e.g. AAPL is Apple Inc. Set default Time period as 3 months of daily ticker data.
4. Create a visual chart for the returned data
5. Create a table for the returned data 
6. Create a way so that a user can select a share and it follows through to a page designed for that page only e.g. they click on AAPL and it loads a page dedicated to AAPL and not the home page.

# Basic User Account Management
1. Create Database Models for users 
2. Generate a register, login  and logout pages 
    1. Create routes for handling these requests
3. Manage user access so that logged in users can see Favourites template page - but non-logged in users cannot see this page. 
4. Create user forgot password and reset email/password management. 
5. Create a way for a user to delete their account. 
    1. Re route deleted user to register page/home page.

# Favourites Page Features
1. Create a way for a user to add a returned ticker information to their favourites.
    1. Might need to make a new database model to store this information relationship as it is a one-to-many relationship - one user can have many favourites. 
2. Add a way for a user to remove stocks from their favourites page. 
3. Favourites Page to have a Square Pie Chart to show favourites performance. 
4. Allow a linking feature that lets a user click on Pie Chart to follow through to a particular stocks information e.g. click on AAPL it goes to page with information on AAPL. 

The above is the functional MVP and the remainder below is nice to have processes.

# Notifications from Favourites Page 
1. Create a notifications bell when the values for their favourite shares drop or rise below a certain amount % each days close e.g. 5%. 
    1. Should really have this notification as a email. 
    2. Could also make it a popup modal. 
2. Add some more financial ticker information formulas, like P/E ratio, Free Cash Flow as charts for a particular stock. 
3. Add some news articles relating to the shares flowing across the page like a real time news article website. 
4. There should be a performance over time metric for their favourites page from the inception of making this stock a favourite. 
5. There should be a page of super investors
6. You should be able to see your portfolio compared to a super investor. 

# Testing 
The app should be tested to show demonstratable experience of unit testing. 

# Deployment 
The app should be hosted and deployed on a cloud instance. Along with the database. For dev purposes the app is made in initial stages with offline SQLite3 databases. 

# Styling 
HTML, CSS and JavaScript should be learnt for how to do basic styling or bootstrap to ensure that the app looks quite nice. 
