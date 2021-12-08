import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import py4e_common

py4e_common.configure_proxies()

while True:
    try:
        url = input('Enter URL: ')
        html = urllib.request.urlopen(url).read()
        break
    except (ValueError, urllib.error.URLError) as err:
        print(err)

soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# print(soup)
