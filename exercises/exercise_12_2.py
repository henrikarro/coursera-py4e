import urllib.request, urllib.error
from bs4 import BeautifulSoup
import py4e_common

py4e_common.configure_proxies()


def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError as err:
            print(err)


# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the
# last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Lucas.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the
# last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: I
url = input('Enter URL: ')
count = input_int('Enter count: ')
position = input_int('Enter position: ')

for i in range(count + 1):
    print('Retrieving:', url)
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    links = [a_tag.get('href', None) for a_tag in soup('a')]
    if len(links) < position or links[position - 1] is None:
        print('There is no link at position', position)
        break
    url = links[position - 1]
