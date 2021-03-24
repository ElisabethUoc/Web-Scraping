import requests
from bs4 import BeautifulSoup

url = 'https://www.hometogo.com/search/5460aea910151?adults=2&arrival=2021-06-01&duration=13'


def get_listings(search_page):
    answer = requests.get(search_page, timeout=5)
    content = answer.content
    soup = BeautifulSoup(content, 'html.parser')
    listings = soup.find_all('div', 'dne pb16 ph8')

    return listings

soup = BeautifulSoup(requests.get(url).content, 'html.parser')
soup.find_all('div', 'dne pb16 ph8')

print(soup.find_all('div', 'dne pb16 ph8'))