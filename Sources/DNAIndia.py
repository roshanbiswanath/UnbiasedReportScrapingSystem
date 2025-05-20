from Sources.AbstractNewsSource import AbstractNewsSource
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article

class DNAIndia(AbstractNewsSource):
    """Class for DNA India RSS Feed as a news source"""
    url = "https://www.dnaindia.com/feeds/latest.xml"

    def scrapeArticle(self, feedArticle) -> Article:
        response = requests.get(feedArticle.link)
        soup = BeautifulSoup(response.content, 'html.parser')
        mainTag = soup.find('div', class_='article-description')
        if mainTag is None:
            return None
        pTags = mainTag.find_all('p')
        content = ""
        for pTag in pTags:
            content += pTag.get_text()
        # content = mainTag.get_text()
        content = self.stripMultiline(content)
        # print(content)
        return Article(
            title=feedArticle.title,
            description=feedArticle.description,
            url=feedArticle.link,
            content=content,
            published_at=feedArticle.published,
            source="DNA India",
        )

    def scrapeNews(self):
        response = requests.get(self.url)
        feed = feedparser.parse(response.text)
        for feedArticle in feed.entries:
            # print(feedArticle)
            parsedArticle = self.scrapeArticle(feedArticle)
            if parsedArticle is None:
                continue
            self.storeScrapedArticle(parsedArticle)
            print("="*100)
