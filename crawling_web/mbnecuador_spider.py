import scrapy


class MbnecuadorSpider(scrapy.Spider):
    name = "Mbnecuador"
    
    start_urls = [
        'http://mbnecuador.com/mbnecuador/releases-2/',
    ]

    def parse(self, response):
        for artista in response.css('article.col-1-4'):
            yield {
                'nombre': artista.css('footer h2 a::text').extract_first(),
                'url': artista.css('footer h2 a::attr(href)').extract_first(),
                'categoria': artista.css('footer div.cat a::text').extract_first(),
                'categoria_url': artista.css('footer div.cat a::attr(href)').extract_first(),
                'imagen': artista.css('img::attr(src)').extract_first(),
            }

            next_page = response.css('div.wp-pagenavi a.nav-next::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)