import scrapy

class SupermercadosBHSpider(scrapy.Spider):
    name = 'supermercadosbh'
    start_urls = ['https://www.supermercadosbh.com.br/serra-es/']

    def parse(self, response):
        for product in response.css('.product-item'):
            yield {
                'name': product.css('.product-name::text').get(),
                'price': product.css('.product-price::text').get(),
            }
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)