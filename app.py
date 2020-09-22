app.py
# from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello world"

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite://hawaii.sqlite")
# create engine allows us to ACCESS and QUERY our SQLite database file.

# reflect the databaase into our classes
Base = automap_base()

# reflect our tables using .prepare() Python Flask function
Base.prepare(engine, reflect=True)

# With database reflected, we can save our references to each table.(same ones from notebook)
# We'll create a variable for each of the classes so that we can reflect them later.

Measurement = Base.classes.measurement
Station = Base.classes.station

# create a *session link* from Python to our database
session = Session(engine)

# Next, need to define our app for our Flask application.

## SET UP FLASK ## still 9.5.1

# To define our flask app, add the following. This creates a Flask application called "app"
app = Flask(__name__)

# note the __name__ variable here. SPECIAL TYPE OF VARIABLE in PYTHON. 
# It's value depends on WHERE and HOW the code is run.
# for example: if we want to import our app.py (this file) into another Python file
# named *example.py* the variable __name__ would be set to *example*

#         Below is how it would look to run *app* (which is app = Flask(__name__))
#         in file called *example.py*
#                            ****EXAMPLE****
# import app

# print("example __name__ = %s", __name__)

# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")


# when we run *app* in the this file: surf_app.py (where it was created) 
# # the __name__ variable will be set to __main__ 
# # this indicates that we're not using any other file to run the code.

app

# @app.route('/')
# def hello_world():
#     return "Bruh this flask stuff"

#### 9.5.2 #### Create the WELCOME ROUTE ####

# Important: all your routes should go after the: app = Flask(__name__) line of code.

#defining Welcome Route (aka: root)
@app.route("/")

# Now our ROOT, or welcome route, is set up. Next step is to add the routing info for
# each of the other routes.  
# 1st, we'll create a *function* and our return statement will have f-strings
# as a reference to all of the other routes.  This ensures the investors know have to nav.
# 
# # create function: welcome() with a return statement. then add routes w/ f-strings
# 
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
# note: when creating routes, use the naming convention: /api/v1.0/ followed by name of route.
# this convention signfies that it's version 1 of our application.