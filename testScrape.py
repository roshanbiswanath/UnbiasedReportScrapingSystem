from Sources.AbstractNewsSource import AbstractNewsSource
from Sources.TheHindu import TheHindu
from Sources.IndiaToday import IndiaToday
from Sources.NDTV import NDTV
from Sources.IndianExpress import IndianExpress
from Sources.News18 import News18
from Sources.DNAIndia import DNAIndia
from Sources.FirstPost import FirstPost
from Sources.OpIndia import OpIndia
from Sources.AlJazeera import AlJazeera
from IncompleteSources.TheQuint import TheQuint
from scrapeService import NewsScrapingSystem

scraping_system = NewsScrapingSystem()
# scraping_system.add_news_source(TheHindu())
# scraping_system.add_news_source(IndiaToday())
# scraping_system.add_news_source(NDTV())
# scraping_system.add_news_source(IndianExpress())
# scraping_system.add_news_source(News18())
# scraping_system.add_news_source(DNAIndia())
# scraping_system.add_news_source(FirstPost())
# scraping_system.add_news_source(OpIndia())
# scraping_system.add_news_source(AlJazeera())
# scraping_system.add_news_source(TheQuint())
scraping_system.scrape_news()