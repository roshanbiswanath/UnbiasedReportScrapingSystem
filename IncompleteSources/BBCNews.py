from Sources.AbstractNewsSource import AbstractNewsSource
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article

"""Incomplete Code Snippet"""

class BBCNews(AbstractNewsSource):
    """Class for India Today RSS Feed as a news source"""
    url = "https://www.indiatoday.in/rss/home"

    def scrapeArticle(self, feedArticle) -> Article:
        urlSplit = feedArticle.link.split("/")
        if "story" in urlSplit and "www.indiatoday.in" in urlSplit:
            response = requests.get(feedArticle.link)
            soup = BeautifulSoup(response.content, 'html.parser')
            # print(soup.prettify())
            # print(feedArticle.link)
            mainTag = soup.find('div', class_='description')
            if( mainTag is None):
                return
            pTags = mainTag.find_all('p')
            # print(len(pTags))
            content = ""
            for pTag in pTags:
                content += pTag.get_text()
            content = self.stripMultiline(content)
            return Article(
                title=feedArticle.title,
                description=feedArticle.description,
                url=feedArticle.link,
                content=content,
                published_at=feedArticle.published,
                source="India Today"
            )
        else:
            return None

    def scrapeNews(self):
        response = requests.get(self.url)
        feed = feedparser.parse(response.text)
        for feedArticle in feed.entries:
            parsedArticle = self.scrapeArticle(feedArticle)
            if parsedArticle is None:
                continue
            self.storeScrapedArticle(parsedArticle)
            print("="*100)
