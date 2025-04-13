from Sources.IndiaToday import IndiaToday

class NewsScrapingSystem:
    """Class for news scraping system"""

    def __init__(self):
        self.news_sources = []

    def add_news_source(self, source):
        self.news_sources.append(source)

    def scrape_news(self):
        for source in self.news_sources:
            # link = source.get_news_link()
            print(f"Scraping news from {source.__class__.__name__}")
            news_data = source.scrapeNews()
            print(news_data)


if __name__ == "__main__":
    scraping_system = NewsScrapingSystem()
    scraping_system.add_news_source(IndiaToday())
    scraping_system.scrape_news()
