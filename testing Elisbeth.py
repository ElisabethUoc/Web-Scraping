import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from IPython.display import IFrame

url = 'https://www.hometogo.com/search/5460aea910151?adults=2&arrival=2021-06-01&duration=13'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')


listings = soup.find_all('div', 'posr h100p w100p')

def get_listings(search_page):
    soup = BeautifulSoup(driver.page_source.content, 'html.parser')
    listings = soup.find_all('div', 'posr h100p w100p')
    return listings

RULES_SEARCH_PAGE = {
    'name': {'tag': 'div', 'class': 'text-medium fwb c-black lh18 ovh text-overflow'},
    'price': {'tag': 'span', 'class': 'fwb wsnw fz16'},
    'location': {'tag': 'span', 'class': 'c-gray-extra-dark text-small text-overflow'},
    'rating_n_reviews': {'tag': 'span', 'class': 'text-small c-accent-normal'},
}


def extract_element(listing_html, params):
    # 1. Find the right tag
    if 'class' in params:
        elements_found = listing_html.find_all(params['tag'], params['class'])
    else:
        elements_found = listing_html.find_all(params['tag'])
    # 2. Extract the right element
    tag_order = params.get('order', 0)
    element = elements_found[tag_order]
    # 3. Get text
    if 'get' in params:
        output = element.get(params['get'])
    else:
        output = element.get_text()
    return output




for feature in RULES_SEARCH_PAGE:
    try:
         print(f"{feature}: {extract_element(listings[0], RULES_SEARCH_PAGE[feature])}")
    except:
         print(f"{feature}: empty")
