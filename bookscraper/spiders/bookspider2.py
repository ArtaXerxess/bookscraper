import scrapy


class Bookspider2Spider(scrapy.Spider):
    name = "bookspider2"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
