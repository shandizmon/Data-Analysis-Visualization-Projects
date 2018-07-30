
# coding: utf-8

# ## Step 3 - Climate Analysis and Exploration

# In[1]:


# Dependencies
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from datetime import datetime, timedelta
import numpy as np
from pprint import pprint
from citipy import citipy
from random import uniform

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float, select, func
from sqlalchemy.ext.automap import automap_base

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[2]:


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


# ### Precipitation Analysis
# * Design a query to retrieve the last 12 months of precipitation data.
# 
# * Select only the `date` and `prcp` values.
# 
# * Load the query results into a Pandas DataFrame and set the index to the date column.
# 
# * Plot the results using the DataFrame `plot` method.
# 
# * Use Pandas to print the summary statistics for the precipitation data.

# In[3]:


# Find the dates
Latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
start_date = pd.to_datetime(Latest_date[0]).date()- timedelta(days=365)
print(start_date)


# In[4]:


# Query and select 'date' and 'prcp' for the last 12 months
date_precipitation=(session.query(Measurement.date,Measurement.prcp)
.filter(Measurement.date>=start_date)
.order_by(Measurement.date.desc()).all())


# In[5]:


# Load the query results into a DataFrame and set the date column as an index
df_date_precipitation=pd.DataFrame(date_precipitation, columns=['date','precipitation'])
df_date_precipitation.set_index('date', inplace=True)
df_date_precipitation.head()


# In[6]:


# Plot the results using the DataFrame plot method
df_date_precipitation.plot(figsize=(15,10))
plt.title("Precipitation over the last 12 months")
plt.ylabel("Precipitation")
plt.xlabel("Date")
plt.savefig("precip.png")
plt.show()


# In[7]:


#print the summary statistics for the precipitation data
df_date_precipitation.describe()


# ### Station Analysis
# 
# * Design a query to calculate the total number of stations.
# 
# * Design a query to find the most active stations.
# 
# * List the stations and observation counts in descending order
# 
# * Which station has the highest number of observations?
# 
# * Design a query to retrieve the last 12 months of temperature observation data (tobs).
# 
# * Filter by the station with the highest number of observations.
# 
# * Plot the results as a histogram with `bins=12`.
