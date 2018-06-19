
# coding: utf-8

# # Analysis
# 
# ### Observed Trend 1:
# Cities loacated close to latitude 0 (equator) have the highest temprature and as you get farther from    equator temperature decreases. Please note that these tempretaure are collected in the hottest period of the year and conclusively the temperature range is less than if we had collected data in winter or spring.
# 
# ### Observed Trend 2: 
# Cities loacated close to latitude 0 (equator) have a higher humidity which is probably due to higher water evaporation rate. Also it looks for the cities in the southern hemisphere the farthest ones from equator have higher humidity.
# 
# ### Observed Trend 3: 
# Laditude does not seem to have a correlation to wind speed and cloudiness.

# In[1]:


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


# In[2]:


# geocoordinates

def newpoint1():
    return uniform(-90.0,0), uniform(-180.0,180.0)

def newpoint2():
    return uniform(0,90), uniform(-180.0,180.0)

coordinates = []
points = (newpoint1() for x in range(300))
for point in points:
    coordinates.append(point)

points = (newpoint2() for x in range(300))
for point in points:
    coordinates.append(point)
    


# In[3]:


cities = []
for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities.append((citipy.nearest_city(lat, lon).city_name))
    


# In[4]:


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
    # Adding "null" value for the cities which don't have value by "try" and "except"
    try:
        api_params['q']=city
        weather_response = requests.get(base_url, params=api_params).json()
    
        lat.append(weather_response['coord']['lat'])
        temp.append(weather_response['main']['temp_max'])
        humidity.append(weather_response['main']['humidity'])
        clouds.append(weather_response['clouds']['all'])
        wind.append(weather_response['wind']['speed'])
    except:
        lat.append('null')
        temp.append('null')
        humidity.append('null')
        clouds.append('null')
        wind.append('null')



# build a dataframe from the cities, lat, Temperature, Humidity (%), Cloudiness (%),Wind Speed (mph) lists
weather_data = {"City": cities, "Latitude": lat, "Max Temperature (F)": temp, "Humidity (%)": humidity, 
                "Cloudiness (%)": clouds, "Wind Speed (mph)": wind}
df_weather_data = pd.DataFrame(weather_data)
df_weather_data.head()


# In[5]:


# Removing the null value rows from the dataframe
df_weather_data = df_weather_data[df_weather_data.Latitude!='null']
df_weather_data['City'].count()


# In[6]:


# Build the Temperature scatter plot for dataframe
plt.figure(figsize= (12,5))
plt.scatter(df_weather_data["Latitude"], df_weather_data["Max Temperature (F)"], marker="o")

# Incorporate the other graph properties
plt.ylim(-100,150)
plt.xlim(-80,100)
plt.title("City Latitude vs. Max Temperature (06/18/2018)")
plt.ylabel("Max Temperature (Fahrenheit)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CityLatitudevsMaxTemperature.png")

# Show plot
plt.show()


# In[7]:


# Build the Humidity scatter plot for dataframe
plt.figure(figsize= (12,5))
plt.scatter(df_weather_data["Latitude"], df_weather_data["Humidity (%)"], marker="o")

# Incorporate the other graph properties
plt.ylim(-20,120)
plt.xlim(-80,100)
plt.title("City Latitude vs. Humidity (06/18/2018)")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CityLatitudevsHumidity.png")

# Show plot
plt.show()


# In[8]:


# Build the Cloudiness scatter plot for dataframe
plt.figure(figsize= (12,5))
plt.scatter(df_weather_data["Latitude"], df_weather_data["Cloudiness (%)"], marker="o")

# Incorporate the other graph properties
plt.ylim(-20,120)
plt.xlim(-80,100)
plt.title("City Latitude vs. Cloudiness (06/18/2018)")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CityLatitudevsCloudiness.png")

# Show plot
plt.show()


# In[9]:


# Build the Wind Speed scatter plot for dataframe
plt.figure(figsize= (12,5))
plt.scatter(df_weather_data["Latitude"], df_weather_data["Wind Speed (mph)"], marker="o")

# Incorporate the other graph properties
plt.ylim(-5,40)
plt.xlim(-80,100)
plt.title("City Latitude vs. Wind Speed (06/18/2018)")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CityLatitudevsWindSpeed.png")

# Show plot
plt.show()

