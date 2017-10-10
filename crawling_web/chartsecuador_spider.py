
 

import scrapy


class ChartsEcuadorSpider(scrapy.Spider):
    name = "ChartsEcuadorSpider"
    start_urls = [
        'https://chartsecuador.jimdo.com/top-25-artistas-ecuatorianos/',
    ]

    def parse(self, response):
        for item in response.css('#content_area .j-text'):
            
            artista = item.css('p span b::text').extract_first()
            if not artista:
                continue    
            
            #2 SP:
            #4 Value SP
            #6 SL:
            #8 value SL

            info = ''
            for texto in item.css('p span::text'):
                validar = texto.extract()
                if validar and not validar.strip().isspace():
                   info = info + ' ' + validar
       
            yield {
               'artista': artista,
               'cancion': item.css('p span::text').extract_first(),
               'info':info
            }
  