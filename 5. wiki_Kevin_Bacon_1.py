import requests
from bs4 import BeautifulSoup

html = requests.get('http://en.wikipedia.org/wiki/Kevon_Bacon')
bs = BeautifulSoup(html.text, 'html.parser')

for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
    if 'title' in link.attrs:
        print(link.attrs['title'])