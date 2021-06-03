##################################Top 10 Team########################################
import requests
from bs4 import BeautifulSoup

URL = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('table', class_='table')
i = 0
for row in data[0].find('tbody').find_all('tr'):
    if i <=9:
        cells = row.find_all("td")
        rank = cells[0].get_text()
        team = cells[1].get_text()
        matches = cells[2].get_text()
        points = cells[3].get_text()
        rating = cells[4].get_text()
        print(rank, end='\n ')
        print(team, end='\n ')
        print(matches, end=' \n')
        print(points, end=' \n')
        print(rating, end=' \n')
        i += 1
    else:
        break

########################################Code for Top 10 Odi batsman###############################
import requests
from bs4 import BeautifulSoup

URL = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find("div", {"data-cricket-role": "batting"})
top_player = data.find('div', class_='rankings-block__top-player')
top_rank = top_player.find('div', class_='rankings-block__banner--pos').get_text()
top_rating = top_player.find('div', class_='rankings-block__banner--rating').get_text()
top_name = top_player.find('div', class_='rankings-block__banner--name').get_text()
top_county = top_player.find('div', class_='rankings-block__banner--nationality').get_text().split()[0]
print(top_rank, end='\n ')
print(top_rating, end='\n ')
print(top_name, end=' \n')
print(top_county, end=' \n')
i = 0
for row in data.find('tbody').find_all('tr'):
    if i <=8:
        rating = row.find('td', class_='table-body__cell u-text-right rating').get_text().strip()
        position = row.find('td', class_='table-body__cell--position').get_text().strip()
        name = row.find('td', class_='table-body__cell name').get_text().strip()
        team = row.find('span', class_='table-body__logo-text').get_text().strip()
        print(rating, end='\n ')
        print(position, end='\n ')
        print(name, end=' \n')
        print(team, end=' \n')
        i += 1
    else:
        break

#######################################Code for Top 10 Odi Bowler###############################
import requests
from bs4 import BeautifulSoup

URL = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find("div", {"data-cricket-role": "bowling"})
top_player = data.find('div', class_='rankings-block__top-player')
top_rank = top_player.find('div', class_='rankings-block__banner--pos').get_text()
top_rating = top_player.find('div', class_='rankings-block__banner--rating').get_text()
top_name = top_player.find('div', class_='rankings-block__banner--name').get_text()
top_county = top_player.find('div', class_='rankings-block__banner--nationality').get_text().split()[0]
print(top_rank, end='\n ')
print(top_rating, end='\n ')
print(top_name, end=' \n')
print(top_county, end=' \n')
i = 0
for row in data.find('tbody').find_all('tr'):
    if i <=8:
        rating = row.find('td', class_='table-body__cell u-text-right rating').get_text().strip()
        position = row.find('td', class_='table-body__cell--position').get_text().strip()
        name = row.find('td', class_='table-body__cell name').get_text().strip()
        team = row.find('span', class_='table-body__logo-text').get_text().strip()
        print(rating, end='\n ')
        print(position, end='\n ')
        print(name, end=' \n')
        print(team, end=' \n')
        i += 1
    else:
        break