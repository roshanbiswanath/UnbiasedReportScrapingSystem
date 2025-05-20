from Sources.AbstractNewsSource import AbstractNewsSource
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article

class OpIndia(AbstractNewsSource):
    """Class for OpIndia RSS Feed as a news source"""
    url = "https://www.opindia.com/feed/"

    def scrapeArticle(self, feedArticle) -> Article:
        # response = requests.get(feedArticle.link)
        soup = BeautifulSoup(feedArticle.content[0].value, 'html.parser')
        # mainTag = soup.find('div', class_='art-content')
        # if mainTag is None:
        #     return None
        # pTags = mainTag.find_all('p')
        content = ""
        # for pTag in pTags:
        #     content += pTag.get_text()
        content = soup.get_text()
        content = self.stripMultiline(content)
        # print(content)
        return Article(
            title=feedArticle.title,
            url=feedArticle.link,
            content=content,
            published_at=feedArticle.published,
            source="OpIndia"
        )

    def scrapeNews(self):
        response = requests.get(self.url)
        feed = feedparser.parse(response.text)
        for feedArticle in feed.entries:
            # print(feedArticle)
            # with open("response.json", "w", encoding="utf-8") as f:
            #     f.write(json.dumps(feedArticle, indent=4))
            # with open("response.html", "w", encoding="utf-8") as f:
            #     f.write(feedArticle.content[0].value)
            parsedArticle = self.scrapeArticle(feedArticle)
            if parsedArticle is None:
                continue
            self.storeScrapedArticle(parsedArticle)
            print("="*100)
