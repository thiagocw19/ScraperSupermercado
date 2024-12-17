# Scrapers de Supermercados

Este projeto implementa dois scrapers utilizando a biblioteca Scrapy para coletar informações sobre produtos de diferentes categorias de dois supermercados: Carone e Extrabom. Os scrapers extraem dados como nome do produto, preço, marca e categoria.

## Funcionalidades

- Coleta informações de produtos de várias categorias dos sites Carone e Extrabom.
- Extrai dados como marca, nome do produto, preço atual e preço antigo (Carone) ou apenas preço e categoria (Extrabom).
- Suporta paginação para coletar produtos de várias páginas de uma categoria.

### Dependências

- **Scrapy**: A biblioteca principal utilizada para realizar o scraping.

Para instalar o Scrapy, você pode usar o seguinte comando:

```
pip install scrapy
```

### Para usar basta seguir os passos:

após implementar no vs code, digite no terminal:

``` cd supermercados ``` | necessário para entrar na pasta do projeto.


``` scrapy crawl carone -o dadosCarone.json -t json ``` | para pegar produtos do carone.

``` scrapy crawl extrabom -o dadosExtrabom.json -t json ``` | para pegar produtos do extrabom.

