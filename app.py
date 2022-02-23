import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
if __name__ == '__main__':
    app.run()
#--------------------------------------------------
#### Database Setup ####
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
#--------------------------------------------------
#### Flask Setup ####
app = Flask(__name__)
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')
if __name__ == '__main__':
    app.run()
#---------------------------------------------------
#### Precipitation Route ####
@app.route("/api/v1.0/precipitation")
def precipitation():
# ### Return the precipitation for last year ###
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

if __name__ == '__main__':
    app.run()
#---------------------------------------------------
#### Station Route ####
@app.route("/api/v1.0/stations")
def stations():
    """ Return a list of stations """
    results = session.query(Station.station).all()

    stations = list(np.ravel(results))

    return jsonify(stations=stations) # { stations: []}

if __name__ == '__main__':
    app.run()
#---------------------------------------------------
#### Monthly Temperature Route (temperature observations) ####
@ app.route("/api/v1.0/tobs")
def temp_monthly():
    """ Retrun the temp observation for previous year """
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()

# unravel results into 1D list and convert to a python list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == '__main__':
    app.run()
#---------------------------------------------------
#### Statistics Route ####

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# calculate TMIN TAVG TMAX with start
    if not end:
        results = session.query(*sel).\
            fileter(Measurement.date >= start).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# calculate TMIN TAVG TMAX with start and stop 
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))
    return jsonify(temps=temps) 

if __name__ == '__main__':
    app.run()

