
# coding: utf-8

# ## Step 3 - Climate Analysis and Exploration

# In[8]:


# Dependencies
import requests
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
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
from sqlalchemy.ext.automap import automap_base

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[12]:


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


# In[10]:


result = (session
          .query(Measurement)
          .count())
result


# ### Precipitation Analysis

# In[ ]:


engine.execute('SELECT 'date', 'prcp'  FROM dow LIMIT 5').fetchall()


# In[ ]:


# Reflect Database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)
Dow = Base.classes.dow

