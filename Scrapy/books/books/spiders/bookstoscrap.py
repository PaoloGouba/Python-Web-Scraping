from unittest import result
import scrapy

# what is yeld?

# exectution in command line, scrapy runspider spider_name.py 



# xpath selector
# ciblage --> //element/child element
# ex : //h1


class BookstoscrapSpider(scrapy.Spider):
    name = 'bookstoscrap'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        result = {
            # simple xpath selector
            #'balise_h1' : response.xpath('//h1'),
            
            # get text 
            #'title' : response.xpath('//head/title/text()').get()
            
            #'links' : response.xpath('//a/text()').getall()
            
            
            # attributes selectors
            
            #'alert' : response.xpath('//div[@role="alert"]/text()').get()
            
            
            # get more elements
            #'product_prices' : response.xpath('//p[@class="price_color"]/text()').getall()
            
            
            #get bloc informations
            
            
            
            
        }
        
        
        yield result
