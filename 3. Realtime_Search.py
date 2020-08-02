import requests
from bs4 import BeautifulSoup
from pprint import pprint

html = requests.get('https://search.naver.com/search.naver?&where=news&query=날씨')
parsingdata = BeautifulSoup(html.text, 'html.parser')
result = parsingdata.find('div', {'class':'realtime_srch _aside_news_tab'})
recently = result.find('ol', {'class':'lst_realtime_srch _tab_area'})

recently = recently.text.replace('NEW', '\n')

print(recently)