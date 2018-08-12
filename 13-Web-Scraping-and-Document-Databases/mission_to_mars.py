
# coding: utf-8

# # Mission to Mars

# ## Step 1 - Scraping

# In[1]:


# Dependencies
import pandas as pd
import requests
import pymongo
import os
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
from flask import Flask, render_template
from datetime import datetime


# ### NASA Mars News

# In[2]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')


# In[3]:


# results are returned news_title and news_p 
news_title = soup.find('div', class_="content_title")
news_p = soup.find('div', class_="rollover_description_inner")
news_title = news_title.a.text.strip()
news_p = news_p.text.strip()
print("news_title = " + news_title)
print('\n-----------------\n')
print("news_p = " + news_p)


# ### JPL Mars Space Images

# In[4]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'lxml')


# In[6]:


#browser.click_link_by_partial_href('/spaceimages/images/mediumsize/PIA17932_ip.jpg')
browser.click_link_by_id('full_image')


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'lxml')
featured_image = soup.find('img', class_='fancybox-image')
featured_image_url = 'https://www.jpl.nasa.gov'+featured_image['src']
browser.quit()
print(featured_image_url)


# ### Mars Weather

# In[8]:


# Retrieve page with the requests module
url='https://twitter.com/marswxreport?lang=en'
response=requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup=BeautifulSoup(response.text, 'lxml')
#find all tweets on the page
mars_tweets=soup.find_all('p', class_='js-tweet-text')
#since this page contains other tweets related to Mars weather, try to find the first tweet with 'Sol ' substring.
for tweet in mars_tweets:
    try:
        p_tweet=tweet.text
        if p_tweet.find('Sol ')!=-1:
            mars_weather=p_tweet
            print("mars_weather = " + mars_weather)
            break
    except AttributeError as e:
        print(e)


# ### Mars Facts

# In[9]:


# URL of page to be scraped
url = 'http://space-facts.com/mars/'


# In[10]:


tables = pd.read_html(url)
print(type(tables))
tables


# In[11]:


df = tables[0]
df.columns = ['Attribute','Value']
df.head(10)


# In[12]:


html_table = df.to_html()
html_table.replace('\n', '')


# ### Mars Hemispheres

# In[13]:


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')


# In[14]:


# results are returned as an iterable list
results = soup.find_all('a', class_="itemLink product-item")
link_texts = []
for result in results:
    link_text = result.find('h3').text.strip()
    link_texts.append(link_text)

link_texts


# In[15]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


full_image_link = []
for link in link_texts:
    browser.visit(url)
    browser.click_link_by_partial_text(link)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    featured_image = soup.find('img', class_='wide-image')
    featured_image_url = 'https://astrogeology.usgs.gov'+featured_image['src']
    full_image_link.append(featured_image_url)
full_image_link


# In[17]:


# Append a Dictionary 

hemisphere_image_urls =[
   {'title': link_texts[0], 'img_url': full_image_link[0]},
   {'title': link_texts[0], 'img_url': full_image_link[1]},
   {'title': link_texts[0], 'img_url': full_image_link[2]},
   {'title': link_texts[0], 'img_url': full_image_link[3]}
]

print(hemisphere_image_urls)

