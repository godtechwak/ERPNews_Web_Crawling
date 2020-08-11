import requests
from bs4 import BeautifulSoup
import re

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
html = requests.get('https://search.zdnet.co.kr/?kwd=ERP', headers = headers).text
bs = BeautifulSoup(html, 'html.parser')
ERP_Info1 = bs.find('section', {'class' : 'news_box'}).findAll({"h3"})
num = 1
for i in ERP_Info1:
    i = i.text.replace("<h3>", "")
    print('{}위 {}'.format(num, i))
    num += 1
    if num == 11:
        break


