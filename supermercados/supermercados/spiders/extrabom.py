# extrabom/spiders/extrabom_spider.py
import scrapy

class ExtrabomSpider(scrapy.Spider):
    name = 'extrabom'
    allowed_domains = ['extrabom.com.br']
    
    # Lista de URLs das categorias
    start_urls = [
        'https://www.extrabom.com.br/c/mercearia/4/',
        'https://www.extrabom.com.br/c/pereciveis/12/',
        'https://www.extrabom.com.br/c/higiene-beleza/8/',
        'https://www.extrabom.com.br/receitas',
        'https://www.extrabom.com.br/c/limpeza/30/',
        'https://www.extrabom.com.br/c/bebidas/28/',
        'https://www.extrabom.com.br/c/hortifruti/1/',
        'https://www.extrabom.com.br/c/padaria/98/',
        'https://www.extrabom.com.br/c/carnes/14/',
    ]

    def parse(self, response):
        # Verifica se a página é uma categoria de produtos
        if 'c/' in response.url:
            for produto in response.css('.carousel__item'):
                yield {
                    'nome': produto.css('::attr(data-name)').get(),
                    'preco': produto.css('::attr(data-price)').get(),
                    'marca': produto.css('::attr(data-brand)').get(),
                    'categoria': produto.css('::attr(data-category)').get(),
                }

            # Navega para a próxima página, se existir
            next_page = response.css('a.next::attr(href)').get()
            if next_page:
                # A URL da próxima página pode ser relativa, então usamos response.urljoin
                yield response.follow(next_page, self.parse)