from Sources.AbstractNewsSource import AbstractNewsSource
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article

class TheHindu(AbstractNewsSource):
    """Class for The Hindu RSS Feed as a news source"""
    url = "https://www.thehindu.com/feeder/default.rss"

    def scrapeArticle(self, feedArticle) -> Article:
        response = requests.get(feedArticle.link)
        soup = BeautifulSoup(response.content, 'html.parser')
        mainTag = soup.find('div', class_='articlebodycontent')
        if mainTag is None:
            return None
        pTags = mainTag.find_all('p')
        content = ""
        for pTag in pTags:
            content += pTag.get_text()
        content = self.stripMultiline(content)
        # print(content)
        return Article(
            title=feedArticle.title,
            description=feedArticle.summary,
            url=feedArticle.link,
            content=content,
            published_at=feedArticle.published,
            source="The Hindu"
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
