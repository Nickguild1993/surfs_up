

# name of the file 
    # 1. ) python app.py -> most typical
    # 2. ) FLASK_APP=app.py - less obvious, but usuable for sure.

    # __name__ -> variable (string)
        # __name__ = "__main__" (1. refers to up above)
        # __name__ = $FLASK_APP

# to run a flask app
# app.run()

# COMMENTED OUT my_app to run the 9.5.1 work for module. 
# my_app = Flask(__name__)

# *app* is just what you set to. if change it my_app = Flask(__name__) then it would be my_app.run()

# if __name__=="__main__":
#     print("Hello there")
    # app.run(debug=True)



# SETUP FLASK WEATHER APP

import datetime as dt 
import numpy as np 
import pandas as pd 

# Add the SQLalchemy dependencies 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# add code to import dependncies that we need for Flask.

from flask import Flask, jsonify

# SETUP THE DATABASE (still 9.5.1)

#setting up our database engine for the Flask application in much the same way
# for climate_analysis.ipynb

engine = create_engine("sqlite:///hawaii.sqlite")
# the create_engine() function allows us to access and query our SQLite database file.

#reflect the database into our classes.

Base = automap_base()

# just like before, we're going to REFLECT our tables.

Base.prepare(engine, reflect=True)

# with database REFLECTED, we can save our references to each table. Create a variable for each of the classes
# so we can reference them later.

Measurement = Base.classes.measurement 

Station = Base.classes.station 

# Finally, create a session link from Python to our database

session = Session(engine)

# Next, we need to define our app for our Flask application.

# SET UP FLASK!!!!

# the following code creates a Flask application called "app"

app = Flask(__name__)

# 9.5.2 ########### 9.5.2 ########### CREATE THE WELCOME ROUTE ######### 9.5.2 ######

# want our welcome route to be the "root" which in our case is pretty much the homepage.

# Remember the google example.  if you google "surfer" the search options for "image", "videos", "news" etc.
# are the different "routes" you can take. Here, the Google Homepage is the ROOT.

# IMPORTANT: All routes should go after app = Flask(__name__) or it won't run right.

# welcome route defined below:
@app.route("/")

# welcome route is now set up.  Next: add the routing informaiton for each of the other routes.
# to do so, we'll CREATE A FUNCTION, and return statement will have F-STRINGS as a reference to all the other routes.

# create FUNCTION: welcome() with a return statement.
#def weclome():
#   return
######### Add the precipitation, stations, tobs, and temp routes for this module into our return statement. use f-strings

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

### ran it in the command line with: flask run 

########## 9.5.3 - PRECIPITATION ROUTE ####### 9.5.3 ####### 9.5.3 ############ 9.5.3 #########

# this route is for the precipitation analysis. this route will occur searately form the welcome route ***
# WHEN MAKING NEW ROUTES- ALWAYS ALIGN CODE TO THE LEFT TO AVOID ERRORS.

@app.route("/api/v1.0/precipitation")

# next, create the precipitation() FUNCTION ||||| Note: .\ signifies you want to cont. query on next line. ****

# firstly, want to add the code that calculates the date one year ago from the most recent data in Db.

## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# secondly, write a query to get the data and precipitation for the previous year.

## precipitation = session.query(Measurement.date, Measurement.prcp).\
## filter(Measurement.date >= prev_year).all()

# finally, create a DICTIONARY w/ the date as the KEY and the precipitation as the VALUE.
# to do this, we will "jsonify" our DICTIONARY.
# Jsonify() is a FUNCTION that converts the DICTIONARY to a JSON file.
# using a JSON file b/c we're dealing with APIs. when we're done modifying the data,
# we can PUSH the data back to a web interface, like FLASK.
# we'll use jsonify() to format our results into a JSON structured file.

## precip = {date: prcp for date, prcp in precipitation}
## return jsonify(precip)

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# worked! used: flask run in CMD Line (in surfs_up file) and then have to add: api/v1.0/precipitation to -->
# the end of http://127.0.0.1:5000/ 


######### STATION ROUTE ###### 9.5.4 ###### STATION ROUTE ###### 9.5.4 #########

# we simply want to return a list of stations for this route.
# Begin by defining the route and route name.  ***** REMEMBER: this code should occur OUTSIDE of prev. route
# and also have NO INDENTATION.

@app.route("/api/v1.0/stations")

# with our route defeined, we can create new FUNCTION called: stations()
## def stations(): return

# next, need to create a query that will allows us to get all the stations in our Db.
## results = session.query(Station.station).all()

# next (THIS IS NEW) we want to start by UNRAVELING our results into a one-dim. array.
# We will use the FUNCTION np.ravel() with *results* as our parameter.
## looks like: stations = np.ravel(results)

# next (AGAIN, THIS IS NEW) convert our UNRAVELED *results* into a LIST.
# do this using the LIST FUNCTION, which is list()
## looks like: stations = list(np.ravel(results))

# finally: we'll jsonify the list and return it as a JSON.
## looks like: jsonify(stations = stations)

#### Notice: In order to return our LIST as a JSOn, we did stations = stations.
#### this formats our list into JSON.

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

# Worked! did the following: flask run in CMD LINE (surfs_up) c & p'd the http://localhost:5000/ 
# then added: the api/v1.0/stations


##### 9.5.5 ##### ##### 9.5.5 ########## 9.5.5 ##### MONTHLY TEMPERATURE ROUTE ##### 9.5.5 #####

# Goal of this route: Return the temperature observations for the previous year.

@app.route("/api/v1.0/tobs")

# next: create FUNCTION called: temp_monthly()
## def temp_monthly(): return 

# next:  calculate the date one year ago from teh late date in Db. (already did this above, just re use)
## prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# next: Query the primary station for all temperature observations (tobs) from previous year.
## results = session.query(Measurement.tobs).\
## filter(Measurement.station == "USC00519281").\
## filter(Measurement.date >= prev_year).all()

# next: UNRAVEL the *results* into a one-dim array. 
## looks like: temps = np.ravel(results)

# next: CONVERT that array into a list.
## temps = list(np.ravel(results))

# FINALLY: Jsonify our *TEMPS* list and return it.
## return jsonify(temps = temps)

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps = temps)

#### WORKS! again, same as above: flask run (from surfs_up) in CMD LINE.  c & p address + api/v1.0/tobs

######### 9.5.6 ######### ######### 9.5.6 ######### STATISTICS ROUTE ####### ######### 9.5.6 #########

# Little bit different that prior routes- have to provide BOTH a STARTING and ENDING date.

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# FIRST: Create FUNCTION called: stats()
## def stats(): return

# Next: Need to add parameters to our stats() FUNCTION: a *start* parameter and a *end* parameter.
# for now, set both of them to None.
## def stats(start = None, end = None):

# Next: (with function declared now) create query to select the MINIMUM, AVERAGE, and MAXIMUM TEMPs 
# from our SQLite database.  begin by CREATING a LIST called: sel
## sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# Next: B/c we need to determine the STARTING and ENDING date, add an: *if-not* statement
## if not end:
## results = session.query(*sel).\
## filter(Measurement.date >= start).\
## filter(Measurement.date <= end).all()
## temps = list(np.ravel(results))
## return jsonify(temps = temps)

# ****TAKE NOTICE: of the ASTERISK (*) in the query next to the *set* LIST. 
# ***** what this does: the ASTERISK is used to indicate that there will be *multiple* results for query->
# ***** results from query will be: minimum, average, maximum temperatures.

# Now: need to calculate the TEMP MIN, AVERAGE, MAX with the START and END dates.
# We'll use the *sel* LIST, which is simply the data points we need to collect.

# def stats():
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs),
#     func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#         filter(Measurement.date >= start).\
#         filter(Measurement.date <= end).all()
#         temps = list(np.ravel(results))
#     return jsonify(temps=temps)


###### TRYING TO DEBUG ######
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps = temps)           

    if not end: 
            results = session.query(*sel).\
            filter(Measurement.date <= start).all()
            temps = list(np.ravel(results))
    return jsonify(temps)

    