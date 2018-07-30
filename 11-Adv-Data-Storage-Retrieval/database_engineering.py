
# coding: utf-8

# ## Step 2 - Database Engineering

# In[1]:


# Dependencies
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns
from pprint import pprint
from citipy import citipy
from random import uniform

# Imports the method used for connecting to DBs
from sqlalchemy import create_engine
# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float, select, func

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[ ]:


# Read CSV cleaned files
clean_measurements = pd.read_csv("Resources/clean_measurements.csv")
clean_stations = pd.read_csv("Resources/hawaii_stations.csv")
clean_measurements.head()


# In[ ]:


# Sets an object to utilize the default declarative base in SQL Alchemy
Base = declarative_base()

# Creates Classes which will serve as the anchor points for our Tables
class Measurement(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True)
    station = Column(String(255))
    date = Column(String(255))
    prcp = Column(Float)
    tobs = Column(Integer)

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station = Column(String(255))
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)


# In[ ]:


# Create Database Connection
# ----------------------------------
# Creates a connection to our DB using the MySQL Connect Engine
# engine = create_engine("mysql://k5xunpkmojyzse51:ifagg1gp7e2xyapi@ffn96u87j5ogvehy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/tq6h098h0ym00zp6")
engine = create_engine("sqlite:///hawaii.sqlite")
# Create a "Metadata" Layer That Abstracts our SQL Database
# ----------------------------------
# Create (if not already in existence) the tables associated with our classes.
Base.metadata.create_all(engine)

# Create a Session Object to Connect to DB
# ----------------------------------
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[ ]:


# Add Records to the Appropriate DB
# ----------------------------------
# Use the SQL ALchemy methods to run simple "INSERT" statements using the classes and objects 
for index, row in clean_measurements.iterrows():
    measurement_record=Measurement(station=row["station"],date=row["date"],prcp=row["prcp"],tobs=row["tobs"])
    session.add(measurement_record)
    session.commit()


# In[ ]:


# Add Records to the Appropriate DB
# ----------------------------------
# Use the SQL ALchemy methods to run simple "INSERT" statements using the classes and objects 
for index, row in clean_stations.iterrows():
    station_record=Station(station=row["station"],name=row["name"],latitude=row["latitude"],longitude=row["longitude"], elevation=row["elevation"])
    session.add(station_record)
    session.commit()


# In[ ]:


# Query the Station table to check if it's working
station_list = session.query(Station)
for station in station_list:
    print(station.name)


# In[ ]:


# Query the Measurement table to check if it's working
measurement_list = session.query(Measurement)
for measure in measurement_list:
    print(measure.station)

