# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from datetime import datetime, timedelta

from flask import Flask, jsonify
import datetime as dt 
import pandas as pd 
from flask import request

# Create Database Connection
Base = automap_base()
# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Station = Base.classes.stations
Measurement = Base.classes.measurements

session = Session(engine)




# My Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"http://localhost:5000/prcp<br/>"
        f"http://localhost:5000/stations<br/>"
        f"http://localhost:5000/tobs<br/>"
        f"http://localhost:5000/start?date=yyyy-mm-dd<br/>"
        f"http://localhost:5000/start_end<br/>"
    )


#http://localhost:5000/prcp
@app.route("/prcp")
def prcp():
    # Find the dates
    Latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    start_date = pd.to_datetime(Latest_date[0]).date()- timedelta(days=365)

    # Query and select 'date' and 'prcp' for the last 12 months
    date_precipitation=(session.query(Measurement.date,Measurement.prcp)
    .filter(Measurement.date>=start_date)
    .order_by(Measurement.date.desc()).limit(10).all())
    dict_precipitation=dict(date_precipitation)
    return jsonify(dict_precipitation)

#http://localhost:5000/stations
@app.route("/stations")
def stations():
    # Return a JSON list of stations from the dataset
    station_list=session.query(Station.station).all()
    return jsonify(station_list)


#http://localhost:5000/tobs
@app.route("/tobs")
def tobs():
    #Return a JSON list of Temperature Observations (tobs) for the previous year
    Latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    start_date = pd.to_datetime(Latest_date[0]).date()- timedelta(days=365)
    
    # Query and select 'date' and 'prcp' for the last 12 months
    date_precipitation=(session.query(Measurement.tobs)
    .filter(Measurement.date>=start_date)
    .order_by(Measurement.date.desc()).limit(10).all())
    return jsonify(date_precipitation)


#http://localhost:5000/start?date=yyyy-mm-dd
@app.route("/start")
def start():
    # get the start date from URL variable
    start_date = request.args.get('date')
    #Return a JSON list of the minimum, average , and max temperature for all dates greater than and equal to the # 
    ldate=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    l=ldate[0]
    if start_date>l:
        print(f"There are no observations for your date. The latest date is {l}")
        return("There are no observations for your date.")
    else:
        temp=(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
              .filter(Measurement.date>=start_date).all())

    return jsonify(temp[0]) 



#http://localhost:5000/start_end?date=yyyy-mm-dd&yyyy-mm-dd
@app.route("/start_end")
def start_end():
    # get the start date from URL variable
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    #Return a JSON list of the minimum, average , and max temperature for all dates between two dates:

    if start_date > end_date:
        print("Wrong dates. Your start date is greater than end date.")
        return("Wrong dates. Your start date is greater than end date.")

    else:
        ldate=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
        l=ldate[0]
    if start_date>l:
        print("There are no observations for your dates.")
    else:
        temp=(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
            .filter(Measurement.date>=start_date)
            .filter(Measurement.date<=end_date).all())
        return jsonify(temp[0])




if __name__ == "__main__":
    app.run(debug=True)

