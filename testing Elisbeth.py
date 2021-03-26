import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from IPython.display import IFrame

url = 'https://www.hometogo.com/search/5460aea910151?adults=2&arrival=2021-06-01&duration=13'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
