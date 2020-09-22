surf_app.py

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
surf_app = Flask(__name__)

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

surf_app

@surf_app.route('/')
def hello_world():
    return "Bruh this flask stuff"