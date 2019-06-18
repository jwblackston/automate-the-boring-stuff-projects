#! python3
"""
Created on Mon Jun 17 16:26:15 2019

@author: walker
Purpose: To open all links to reviews of coffee shops in New Orleans or really any given city, but I live in NOLA so...
"""
import requests, sys, webbrowser, bs4
print('But first, coffee...')
res = requests.get('https://www.yelp.com/search?find_desc=Coffee+Shops&find_loc=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

linkRatings = soup.select('.r aria-label=' + ' '.join(sys.argv[1:]))