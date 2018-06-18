
# coding: utf-8

# In[5]:


# Dependencies
import requests
import pandas as pd
import json
from pprint import pprint
from citipy import citipy
from random import uniform
import matplotlib.pyplot as plt

# Google developer API key
from apikeys import api_key as gkey


# In[6]:


# geocoordinates

def newpoint():
    return uniform(-90.0,90.0), uniform(-180.0,180.0)

coordinates = []
points = (newpoint() for x in range(10))
for point in points:
    coordinates.append(point)
    
coordinates


# In[7]:


cities = []
for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities.append((citipy.nearest_city(lat, lon).city_name))
    
cities


# In[8]:


# list for response results
lat = []
temp = []
humidity = []
clouds = []
wind = []

api_params = {
    'appid': gkey,
    'units': 'imperial',
}

# Build URL
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Get weather information in JSON format
for city in cities:
#    print(city)
    api_params['q']=city
    weather_response = requests.get(base_url, params=api_params).json()
    
    lat.append(weather_response['coord']['lat'])
    temp.append(weather_response['main']['temp'])
    humidity.append(weather_response['main']['humidity'])
    clouds.append(weather_response['clouds']['all'])
    wind.append(weather_response['wind']['speed'])


# build a dataframe from the cities, lat, Temperature, Humidity (%), Cloudiness (%),Wind Speed (mph) lists
weather_data = {"City": cities, "Latitude": lat, "Temperature (F)": temp, "Humidity (%)": humidity, "Cloudiness (%)": clouds, "Wind Speed (mph)": wind}
df_weather_data = pd.DataFrame(weather_data)
df_weather_data.head()


# In[11]:


# Build a scatter plot for each data type
plt.scatter(df_weather_data["Latitude"], df_weather_data["Temperature (F)"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature vs. Latitude in World Cities")
plt.ylabel("Temperature (Fahrenheit)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities.png")

# Show plot
plt.show()

