from Sources.AbstractNewsSource import AbstractNewsSource
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article

class News18(AbstractNewsSource):
    """Class for News18 RSS Feed as a news source"""
    url = "https://www.news18.com/commonfeeds/v1/eng/rss/latest.xml"

    def scrapeArticle(self, feedArticle) -> Article:
        response = requests.get(feedArticle.link)
        soup = BeautifulSoup(response.content, 'html.parser')
        mainTag = soup.find('article', class_='articlecontent')
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
            description=feedArticle.description_1,
            url=feedArticle.link,
            content=content,
            published_at=feedArticle.published,
            source="News18",
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
