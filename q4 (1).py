# Book Reviews and Details
import requests
from bs4 import BeautifulSoup

URL = 'https://bookpage.com/reviews'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find("div", class_='bp-well')
i = 0
for row in data.find_all('div', class_='flex-article-content'):
    if i<=4:
        book_name = row.find('a').get_text()
        cells = row.find_all('p')
        author_name = cells[0].get_text()
        genre = cells[1].get_text()
        URL = 'https://bookpage.com/' + row.find('a').attrs['href']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        reviews = soup.find('div', class_='article-body').get_text()
        print(book_name)
        print(author_name)
        print(genre)
        print(reviews)
    else:
        break
