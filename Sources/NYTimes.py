import requests
from bs4 import BeautifulSoup

from AbstractNewsSource import AbstractNewsSource

class NYTimes(AbstractNewsSource):
    """Class for New York Times news source"""

    def __init__(self, url):
        self.url = url

    def get_news_link(self):
        # Get the latest news link from NYTimes website
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the news link is in a div with id "latest-news"
        return soup.find('div', {'id': 'latest-news'}).find('a')['href']

    def scrape_news(self, link):
        # Scrape the news from the given link
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'class': 'headline'}).text.strip()
        content = soup.find('div', {'class': 'article-body'}).text.strip()
        return {
            "title": title,
            "content": content
        }
