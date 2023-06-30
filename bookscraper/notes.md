# Notes

Concepts: [`css selectors, xpath`](https://docs.scrapy.org/en/latest/topics/selectors.html) 

Using ipython shell , and venv as recommended in doccumentation

Create spider:

>scrapy genspider bookspider books.toscrape.com

Write Code : [Spider.py](spiders\bookspider.py)

Crawl and Save output:

>scrapy crawl bookspider -o books.csv

or

>scrapy crawl bookspider -o books.json

Maybe Scrapy is ez... 

### Using Scrapy Shell

>fetch('https://books.toscrape.com')

>response

>response.css('article.product_pod')

>books = response.css('article.product_pod')

>book = books[0] # first book

>book.css('h3 a::text').get()

>book.css('.product_price .product_color::text').get()

>book.css('h3 a').attrib['href'] # href attribute, link to the book

>response.css('li.next a ::attr(href)').get()

#### Product page

on inspect element one can also use  right_click > copy > copy Selector

>fetch('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

>response.css('.product_page h1::text').get()

>response.css('.product_page p::text').get() # price

>response.css('.product_page p::text').getall()[-1] # product's detailed description

or

>response.css('#content_inner > article > p::text').get() product's detailed description

>response.css('#default > div > div > ul > li:nth-child(3) > a::text').get()  

>response.css('#content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating::attr(class)').get()