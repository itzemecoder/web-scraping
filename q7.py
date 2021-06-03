# Amazon scrapping
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/best-mobile-under-20000/s?k=best+mobile+under+20000'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all("div", {'data-component-type': 's-search-result'})
for row in data:
    prd_img = row.find('span', {'data-component-type':'s-product-image'}).find('a').attrs['href']
    prd_name = row.find('span', class_="a-size-medium a-color-base a-text-normal").get_text()
    price = row.find('span', class_='a-price').find_all('span')[0].get_text()
    rating = row.find('div', class_='a-section a-spacing-none a-spacing-top-micro').find_all('span')[0].attrs['aria-label']
    print(prd_img)
    print(prd_name)
    print(price)
    print(rating)

