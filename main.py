import requests
from bs4 import BeautifulSoup


def scrape_page(page_url):
    """Extracts HTML from a webpage"""

    answer = requests.get(page_url)
    content = answer.content
    soup = BeautifulSoup(content, parser='lxml')

    return soup

# print(scrape_page("https://www.hometogo.com/"))
print(scrape_page("https://www.hometogo.com/").prettify())
