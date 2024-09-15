import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css("h3 a ::attr(href)").get()
            if "catalogue/" in relative_url:
                book_url = "https://books.toscrape.com/" + relative_url
            else:
                book_url = "https://books.toscrape.com/catalogue/" + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)
        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        table_rows = response.css("table tr")
        yield {
            "Title": response.css(".product_main h1::text").get(),
            "Price excl tax": table_rows[2].css("td ::text").get(),
            "Price incl tax": table_rows[3].css("td ::text").get(),
            "Tax": table_rows[4].css("td ::text").get(),
            "Availability": table_rows[5].css("td ::text").get(),
            "Stars": response.css("p.star-rating").attrib["class"],
            "Category": response.css(
                "#default > div > div > ul > li:nth-child(3) > a::text"
            ).get(),
            "Product description": response.css(
                "#content_inner > article > p::text"
            ).get(),
            "Price": response.css("p.price_color ::text").get(),
        }
