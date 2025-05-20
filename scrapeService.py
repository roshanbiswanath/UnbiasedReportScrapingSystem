from Sources.TheHindu import TheHindu
from Sources.IndiaToday import IndiaToday
from Sources.NDTV import NDTV
from Sources.IndianExpress import IndianExpress
from Sources.News18 import News18
from Sources.DNAIndia import DNAIndia
from Sources.FirstPost import FirstPost
from Sources.OpIndia import OpIndia
from Sources.AlJazeera import AlJazeera
import schedule
import time

class NewsScrapingSystem:
    """Class for news scraping system"""

    def __init__(self):
        self.news_sources = []

    def add_news_source(self, source):
        self.news_sources.append(source)

    def scrape_news(self):
        for source in self.news_sources:
            # link = source.get_news_link()
            print(f"Scraping news from {source.__class__.__name__} at {time.ctime()}")
            news_data = source.scrapeNews()
            print(news_data)


if __name__ == "__main__":
    scraping_system = NewsScrapingSystem()
    scraping_system.add_news_source(IndiaToday())
    scraping_system.add_news_source(TheHindu())
    scraping_system.add_news_source(NDTV())
    scraping_system.add_news_source(IndianExpress())
    scraping_system.add_news_source(News18())
    scraping_system.add_news_source(DNAIndia())
    scraping_system.add_news_source(FirstPost())
    scraping_system.add_news_source(OpIndia())
    scraping_system.add_news_source(AlJazeera())

    # Schedule the job
    schedule.every().hour.do(scraping_system.scrape_news)
    # You can change the interval as needed, e.g.:
    # schedule.every(10).minutes.do(scraping_system.scrape_news)
    # schedule.every().day.at("10:30").do(scraping_system.scrape_news)

    print("News scraping service started. Press Ctrl+C to exit.")
    # Initial scrape
    scraping_system.scrape_news()

    while True:
        schedule.run_pending()
        time.sleep(1)
