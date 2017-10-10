import scrapy

class TelevisionSpider(scrapy.Spider):
    name = 'Television'
    start_urls = ['http://www.supercom.gob.ec/es/informate-y-participa/directorio-de-medios/22-television',
    'http://www.supercom.gob.ec/es/informate-y-participa/directorio-de-medios/22-television?site=2',
    'http://www.supercom.gob.ec/es/informate-y-participa/directorio-de-medios/22-television?site=3',
    'http://www.supercom.gob.ec/es/informate-y-participa/directorio-de-medios/22-television?site=4',
    'http://www.supercom.gob.ec/es/informate-y-participa/directorio-de-medios/22-television?site=5']

    def parse(self, response):

        for tv in response.css('div.entry-container div.span6'):
            yield {
                'titulo': tv.css('h2.page-header a::text').extract_first(),
                'Direccion': tv.css('div.spField.field_direccion::text').extract_first(),
                'Telefono': tv.css('div.spField.field_telefono::text').extract_first(),
                'Fax': tv.css('div.spField.field_fax::text').extract_first(),
                'Sitio Web': tv.css('div.spField.field_sitio_web::text').extract_first(),
                'Email': tv.css('div.spField.field_email::text').extract_first(),
                'Twitter': tv.css('div.spField.field_twitter::text').extract_first(),
            }