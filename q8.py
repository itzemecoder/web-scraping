# weather forecast for 7 days
import requests
from bs4 import BeautifulSoup

URL = 'https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196&unit=0&lg=english&FcstType=text&TextType=1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all("table")[1]
data = data.find("tr", {'valign': 'top'})
for row in data:
    print(row.get_text())

