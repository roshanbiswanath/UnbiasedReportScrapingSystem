from abc import ABC, abstractmethod
from util.mongoConn import getClient
from DTO.Article import Article

class AbstractNewsSource(ABC):
    """Abstract class for news sources"""

    def __init__(self):
        # self.url = url
        mongoClient = getClient()
        self.db = mongoClient["reportDB"]
        pass

    def stripMultiline(self, text):
        lines = text.splitlines()
        stripped_lines = [line.strip() for line in lines if line.strip()]
        return "\n".join(stripped_lines)

    def isArticlePresent(self, article: Article) -> bool:
        article = self.db["scrapedArticles"].find_one({"url": article.url})
        if article is not None:
            print(article["title"])
            print("Article already present in DB")
            return True
        else:
            print("Article not present in DB")
            return False
    
    def storeScrapedArticle(self, article: Article):
        if(not self.isArticlePresent(article)):
            self.db["scrapedArticles"].insert_one(article.model_dump())
            print("Inserted article into DB")
    
    @abstractmethod
    def scrapeArticle(self, feedArticle):
        pass

    @abstractmethod
    def scrapeNews(self):
        pass
