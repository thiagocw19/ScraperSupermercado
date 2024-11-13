import scrapy
import re

class CaroneSpider(scrapy.Spider):
    name = 'carone'
    start_urls = [
        'https://www.carone.com.br/alimentos',
        'https://www.carone.com.br/limpeza',
        'https://www.carone.com.br/adega',
        'https://www.carone.com.br/bebidas',
        'https://www.carone.com.br/frios-e-laticinios',
        'https://www.carone.com.br/carnes',
        'https://www.carone.com.br/congelados',
        'https://www.carone.com.br/hortifruti',
        'https://www.carone.com.br/utilidades',
        'https://www.carone.com.br/temperos-e-especiarias',
        'https://www.carone.com.br/infantil---bebe',
        'https://www.carone.com.br/bem-estar',
        'https://www.carone.com.br/bomboniere-e-doces',
        'https://www.carone.com.br/padaria-e-rotisseria',
        'https://www.carone.com.br/pet-shop',
        'https://www.carone.com.br/produtos-etnicos',
        'https://www.carone.com.br/higiene-e-beleza',
    ]

    def parse(self, response):
        # Seleciona todos os produtos na página
        products = response.css('li.utilidades, li.alimentos, li.limpeza, li.adega, li.bebidas, li.frios-e-laticinios, li.carnes, li.congelados, li.hortifruti, li.temperos-e-especiarias, li.infantil---bebe, li.bem-estar, li.bomboniere-e-doces, li.padaria-e-ritisseria, li.pet-shop, li.produtos-etnicos, li.higiene-e-beleza')

        if not products:
            self.log(f'Nenhum produto encontrado em {response.url}')
            return

        # Coleta produtos da página da categoria
        for product in products:
            brand = product.css('.product-brand::text').get()
            name = product.css('.product-name a::text').get()

            # Extraindo preços usando regex se estiverem comentados
            product_html = product.get()

            old_price_match = re.search(r'R\$[\s]*([\d,.]+)', product_html)
            best_price_match = re.search(r'R\$[\s]*([\d,.]+)', product_html)

            # Verificando se os preços estão presentes
            old_price = old_price_match.group(1) if old_price_match else None
            best_price = best_price_match.group(1) if best_price_match else None

            yield {
                'Marca': brand.strip() if brand else 'Marca não disponível',
                'Nome': name.strip() if name else 'Nome não disponível',
                'Preco': best_price,
                'Preço_Antigo': old_price,
            }

        # Paginando se houver mais produtos na categoria
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
        else:
            self.log(f'Não há mais páginas para {response.url}')