
def scrape():

    # Dependencies
    import pandas as pd
    import requests
    import pymongo
    import os
    from splinter import Browser
    from splinter.exceptions import ElementDoesNotExist
    from bs4 import BeautifulSoup

    # 1- Scrape mars news
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    news_title = soup.find('div', class_="content_title")
    news_p = soup.find('div', class_="rollover_description_inner")
    news_title = news_title.a.text.strip()
    news_p = news_p.text.strip()
    
    # 2- JPL Mars Space Images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    browser.click_link_by_id('full_image')
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    featured_image = soup.find('img', class_='fancybox-image')
    featured_image_url = 'https://www.jpl.nasa.gov'+featured_image['src']
    browser.quit()
    
    # 3- Mars weather
    url='https://twitter.com/marswxreport?lang=en'
    response=requests.get(url)
    soup=BeautifulSoup(response.text, 'lxml')
    mars_tweets=soup.find_all('p', class_='js-tweet-text')
    for tweet in mars_tweets:
        try:
            p_tweet=tweet.text
            if p_tweet.find('Sol ')!=-1:
                mars_weather=p_tweet
                break
        except AttributeError as e:
            print(e)
            
    # 4- Mars facts
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Attribute','Value']
    html_table = df.to_html()
    mars_facts = html_table.replace('\n', '')
    
    # 5- Scrape Mars Hemispheres data
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('a', class_="itemLink product-item")
    link_texts = []
    for result in results:
        link_text = result.find('h3').text.strip()
        link_texts.append(link_text)
  

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    full_image_link = []
    for link in link_texts:
        browser.visit(url)
        browser.click_link_by_partial_text(link)
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')

        featured_image = soup.find('img', class_='wide-image')
        featured_image_url1 = 'https://astrogeology.usgs.gov'+featured_image['src']
        full_image_link.append(featured_image_url1)
        
    hemisphere_image_urls =[
        {'title': link_texts[0], 'img_url': full_image_link[0]},
        {'title': link_texts[0], 'img_url': full_image_link[1]},
        {'title': link_texts[0], 'img_url': full_image_link[2]},
        {'title': link_texts[0], 'img_url': full_image_link[3]}
    ]
    browser.quit()
    
    # Create dictionary including all the scraped data
    myDict={'news_title':news_title,'news_p':news_p, 'featured_image_url': featured_image_url, 'mars_weather':mars_weather,
            'mars_facts':mars_facts, 'hemisphere_image_urls':hemisphere_image_urls}
    print(myDict)
    
    # Insert dictionary into MongoDB
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test"]
    mycol = mydb["mars"]

    # Code to insert a new row
    #x = mycol.insert_one(myDict)

    #code to update the current collection
    mycol.update({}, myDict, upsert=True)
