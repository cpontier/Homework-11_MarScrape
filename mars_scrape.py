
# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


def scrape():

news_url = 'https://mars.nasa.gov/news/'
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
weather_url = 'https://twitter.com/marswxreport?lang=en'
facts_url = 'http://space-facts.com/mars/'

#---------------------------------------
#-------------PULLING NEWS--------------
#---------------------------------------

html = requests.get(news_url)
soup = BeautifulSoup(html.text, 'html.parser')

news_title = soup.find("", {"class": "content_title"})
news_title = news_title.a.text
news_title = news_title.strip()
news_title

html = requests.get(news_url)
soup = BeautifulSoup(html.text, 'html.parser')

news_blurb = soup.find(class_='rollover_description_inner')
news_blurb = news_blurb.text.strip()
news_blurb

#---------------------------------------
#-----------SCRAPING IMAGES-------------
#---------------------------------------

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(image_url)
browser.click_link_by_id('full_image')

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
picture = soup.find('div', class_="fancybox-image")

html = requests.get(weather_url)
soup = BeautifulSoup(html.text, 'html.parser')

mydivs = soup.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
mydivs.text

fact_table = pd.read_html(facts_url)
fact_table

mars_stats_df = fact_table[0]
mars_stats_df

mars_stats_df.columns = ["Statistic","Value"]

mars_stats_df.set_index("Statistic", inplace=True)

mars_stats_df

cerberus_image_url = https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg
schiaparelli_image_url = https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg">
syrtis_major_image_url = https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg">
valles_marineris_image_url = https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg">

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_image_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_image_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_image_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_image_url},
]

