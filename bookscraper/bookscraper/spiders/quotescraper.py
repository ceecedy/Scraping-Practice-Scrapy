import scrapy
from bookscraper.items import QuoteItem

class QuotescraperSpider(scrapy.Spider):
    name = "quotescraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    
    def parse(self, response):
        # get the general tag to scrape
        quotes = response.css('div.quote')
        
        for quote in quotes:
            # general quote
            quote_text = quote.css('span.text::text').get()
            # quote owner 
            author = quote.css('small.author::text').get()
            # tags
            tags = quote.css('div.tags a.tag::text').getall()

            # Check if values are not None before yielding
            if quote_text is not None and author is not None:
                # Use the QuoteItem to structure the scraped data
                item = QuoteItem(
                    quote=quote_text.strip(),
                    author=author.strip(),
                    tags=tags,
                )
            yield item
            
        next_page = response.css('li.next a ::attr(href)').get()
        # checking if next_page is existing. 
        if next_page is not None:
            next_page_url = 'https://quotes.toscrape.com' + next_page
        yield response.follow(next_page_url, callback = self.parse)
        
        


        
