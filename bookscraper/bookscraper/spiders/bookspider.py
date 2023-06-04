import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield {
                'name': book.css('h3 a::text').get(),
                'price': book.css('.product_price .price_color::text').get(),
                'url': book.css('h3 a').attrib['href'],
            }

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            """
            indicate the full url for next page, 
            tells scrapy to go to next_page_url, 
            callback is what gets executed when response comes back from the url
            which is run self.parse function
            it will continue until next_page returns None
            """
            next_page_url = 'https://books.toscrape.com/' + next_page
            yield response.follow(next_page_url, callback=self.parse)
