
# coding: utf-8

# ## Step 1 - Data Engineering

# In[1]:


# Dependencies
import requests
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from random import uniform


# In[2]:


# Read CSV file
measurements = pd.read_csv("Resources/hawaii_measurements.csv")
stations = pd.read_csv("Resources/hawaii_stations.csv")


# In[3]:


# Count the number of nulls
measurements['prcp'].isnull().values.sum()


# In[4]:


# Creat a clean dataframe after dropping the null cells: 
clean_measurements = measurements[np.isfinite(measurements['prcp'])]


# In[5]:


# Write the dataframe to CSV file
clean_measurements.to_csv('Resources/clean_measurements.csv', sep=',')

