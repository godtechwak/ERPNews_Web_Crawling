import requests
from bs4 import BeautifulSoup
from pprint import pprint

html = requests.get('https://search.naver.com/search.naver?query=날씨')
parsingData = BeautifulSoup(html.text, 'html.parser')
result = parsingData.find('div', {'class':'weather_box'})

address = result.find('span', {'class':'btn_select'}).text
temperature = result.find('span', {'class':'todaytemp'}).text 
cast = result.find('p', {'class':'cast_txt'}).text
rain = result.find('span', {'class':'rainfall'}).text
rain = rain.replace('강수량', '')

print('현재 위치 : ' + address)
print('현재 온도 : ' + temperature + '℃')
print('날씨      : ' + cast)
print('강수량    : ' + rain)