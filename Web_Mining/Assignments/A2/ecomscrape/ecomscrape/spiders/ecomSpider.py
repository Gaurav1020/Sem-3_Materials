import scrapy
from ..items import EcomscrapeItem

class PostsSpider(scrapy.Spider):
    name= "posts"
    str=input("Enter the search: ")
    link="https://www.flipkart.com/search?q="+ str
    start_urls=[link]

    def parse(self, response):
        items= EcomscrapeItem()
        
        
        for p in response.css('div._4ddWXP'):

            Name= p.css('a.s1Q9rs::text').get()
            Price= p.css('a._8VNy32 div._25b18c div._30jeq3::text').get().split('\u20b9')[1]
            Images= p.css('img::attr(src)')[0].get()
            Discount=p.css('div._3Ay6Sb span::text').get().split(' ')[0]
            
            items['name'] = Name
            items['price'] = Price
            items['images'] = Images
            items['discount'] = Discount

            yield items
