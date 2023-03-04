from __future__ import division, unicode_literals 
import codecs
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup as bs
# Importing the HTTP library
import requests as request
# Importing Trans
import googletrans 
from googletrans import *
translator = googletrans.Translator()

  
# Requesting for the website
web = request.get('https://exurbplan.github.io/Scrap-Archfiend/www.classcentral.com/about.html')
soup = bs(web,'xlml')
print(soup)


target = soup.find_all(text)
print(target)


# -------------------------------------------------------------------------

# Creating a BeautifulSoup object and specifying the parser
#soup = bs(web, 'lxml')
#print(soup)
# for data in f.soup.get_text:
#    data = translator(data, 'hi')



# Index trans