import scrapy


class RadioEcSpider(scrapy.Spider):
    name = "RadioEc"
    
    start_urls = [
        'http://www.supercom.gob.ec/kw/informate-y-participa/directorio-de-medios/21-radiodifusoras',
    ]

    def parse(self, response):

        for item in response.css('div.entry-container div.span6'):
            yield {
                'titulo': item.css('h2.page-header a::text').extract_first(),
                'Direccion': item.css('div.spField.field_direccion::text').extract_first(),
                'Telefono': item.css('div.spField.field_telefono::text').extract_first(),
                'Fax': item.css('div.spField.field_fax::text').extract_first(),
                'Sitio Web': item.css('div.spField.field_sitio_web::text').extract_first(),
                'Email': item.css('div.spField.field_email::text').extract_first(),
                'Twitter': item.css('div.spField.field_twitter::text').extract_first(),
            }

            next_page = response.css('div.pagination.pagination-centered ul li:nth-last-child(2) a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)