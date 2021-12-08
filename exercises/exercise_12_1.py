import urllib.request, urllib.error
from bs4 import BeautifulSoup
import py4e_common

py4e_common.configure_proxies()

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1420776.html (Sum ends with 43)
while True:
    try:
        url = input('Enter URL: ')
        html = urllib.request.urlopen(url).read()
        break;
    except (ValueError, urllib.error.URLError) as err:
        print(err)

soup = BeautifulSoup(html, 'html.parser')

num_comments = [int(span_tag.contents[0]) for span_tag in soup('span')]
print(sum(num_comments))
