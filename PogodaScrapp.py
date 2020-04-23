import re

import requests
from bs4 import BeautifulSoup

"""URL = "https://meteoprog.pl/pl/weather/Zabki/"

html_site = requests.get(URL)
html_site = html_site.text

soup = BeautifulSoup(html_site, "html.parser")

temp = soup('div', class_="icon-weather")
temp = temp[0]
weather_general = temp['title']

print(f"General weather forecast: {weather_general}")

temp_val = soup('div', class_="temp")
temp_0 = temp_val[0]
temp_today = temp_0.get_text()
temp_final = str(temp_today).strip()

print(f"Average temperature today will be: {temp_final}")

temp_feel = soup('div', class_="someTemp")
temp_feel0 = temp_feel[0].get_text()
temp_feel_final = str(temp_feel0).strip()

print(f"Temperature you will feel will be: {temp_feel0}")"""


URL = "https://pogoda.interia.pl/prognoza-dlugoterminowa-zabki,cId,39837"

html_doc = requests.get(URL)
html_doc2 = html_doc.text

soup = BeautifulSoup(html_doc2, "html.parser")
weather_all = soup('div', class_="weather-forecast-longterm-list-entry")

weather_today = weather_all[0]
today_day = weather_today('span', class_="day")[0].get_text()
today_date = weather_today('span', class_="date")[0].get_text()

print(f"{today_day}, {today_date}")

data_today = weather_today.find('div', class_=re.compile("top"))        # Wyszukiwanie po fragmencie nazwy klasy.
max_temp = data_today.find('span', class_=re.compile("temp")).get_text()
min_temp = data_today.find('span', class_=re.compile("lowtemp")).get_text()
clouds = data_today.find('span', class_=re.compile("phrase")).get_text()

print(f"Max day temperature: {max_temp}, Lowest day temperature: {min_temp}, and sky forecast is: {clouds}")


