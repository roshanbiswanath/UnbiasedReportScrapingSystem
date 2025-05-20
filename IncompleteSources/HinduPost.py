from Sources.AbstractNewsSource import AbstractNewsSource
import requests
from bs4 import BeautifulSoup
import json
from DTO.Article import Article
from util.seleniumScrape import getDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""Currently Not Working because of Cloudflare Protection"""

class HinduPost(AbstractNewsSource):
    """Class for OpIndia Website as a news source"""
    url = "https://hindupost.in/all-articles/   "
    taretClass = "td-read-more"
    seleniumDriver = getDriver(True)

    def scrapeArticle(self, feedArticle) -> Article:
        response = requests.get(feedArticle)
        # if response.status_code != 200:
        #     print(f"Failed to fetch article: {feedArticle}")
        #     return None
        with open("response.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        # self.seleniumDriver.get(feedArticle)
        # self.seleniumDriver.implicitly_wait(10)
        # self.seleniumDriver.save_screenshot("newscreenshot.png")
        # title = self.seleniumDriver.find_element(By.CLASS_NAME, "tdb-title-text").text
        # description = self.seleniumDriver.find_element(By.CLASS_NAME, "tdb_single_subtitle").text
        # articleContainer = self.seleniumDriver.find_element(By.CLASS_NAME, "tdb_single_content")
        # paragraphs = articleContainer.find_elements(By.TAG_NAME, "p")
        # content = ""
        # for paragraph in paragraphs:
        #     content += paragraph.text + "\n"
        # content = self.stripMultiline(content)
        # return Article(
        #     title=title,
        #     description=description,
        #     url=feedArticle,
        #     content=content,
        #     published_at=None,
        #     source="OpIndia"
        # )

    def scrapeNews(self):
        self.seleniumDriver.get(self.url)
        self.seleniumDriver.implicitly_wait(60)
        self.seleniumDriver.save_screenshot("prevscreenshot.png")
        target_class_name = "td-read-more"
        element_present = EC.presence_of_element_located((By.CLASS_NAME, target_class_name))
        WebDriverWait(self.seleniumDriver, 3).until(element_present)
        articleDivs = self.seleniumDriver.find_elements(By.CLASS_NAME, "td-read-more")
        for articleDiv in articleDivs:
            link_element = articleDiv.find_element(By.TAG_NAME, "a")
            articleURL = link_element.get_attribute("href")
            if articleURL is None:
                continue
            article = self.scrapeArticle(articleURL)
            if article is None:
                continue
            print(article)
        # soup = BeautifulSoup(response.content, 'html.parser')


        # read_more_links = soup.find_all('a', attrs={'title': 'Read more'})
        # print(len(read_more_links))
        # feed = feedparser.parse(response.text)
        # for feedArticle in feed.entries:
        #     parsedArticle = self.scrapeArticle(feedArticle)
        #     if parsedArticle is None:
        #         continue
        #     self.storeScrapedArticle(parsedArticle)
        #     print("="*100)
