# Notes

Concepts: [`css selectors, xpath`](https://docs.scrapy.org/en/latest/topics/selectors.html) 

Using ipython shell , and venv as recommended in doccumentation



| File/Folder | Description | Explanation | Role |
| --- | --- | --- | --- |
| scrapy.cfg | Project configuration file | This file is used to configure settings for the Scrapy project, such as the project name and the location of the spider modules. It is typically located in the project's root directory. | Configuration |
| items.py | Defines the data structure for scraped items | In this file, you define the structure of the data items you want to extract from web pages. Each item represents a single piece of data and can include fields such as title, description, URL, etc. | Data Structure |
| middlewares.py | Custom middleware components | Middleware components are used to process requests and responses. In this file, you can define custom middleware to modify or intercept requests and responses, allowing you to customize the behavior of Scrapy's engine. | Customization |
| pipelines.py | Item pipeline implementation | Item pipelines are responsible for processing the extracted items. They perform tasks such as data validation, cleaning, and storage. In this file, you can define the logic and actions to be performed on the scraped items before they are stored or further processed. | Data Processing |
| settings.py | Configuration settings for the project | This file contains various settings for your Scrapy project. You can configure things like user-agent strings, concurrency settings, and pipeline activation. It provides a central place to customize the behavior and options of your Scrapy project. | Configuration |
| spiders/ | Directory containing spider modules | The `spiders` directory is where you store your spider modules. Each spider module is a Python file that defines how to scrape a particular website or set of websites. Each spider typically inherits from `scrapy.Spider` and contains the scraping logic for the target site(s). | Scraping Logic |



Create spider:

>scrapy genspider bookspider books.toscrape.com

Write Code : [bookspider.py](spiders\bookspider.py)

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