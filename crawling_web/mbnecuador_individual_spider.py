import scrapy
import json

class ArtistaItem(scrapy.Item):
    id = scrapy.Field()
    nombre = scrapy.Field()
    url = scrapy.Field()
    video = scrapy.Field()
    facebook = scrapy.Field()
    twitter = scrapy.Field()
    youtube = scrapy.Field()
    instagram = scrapy.Field()
   

class MbnecuadorIndividualSpider(scrapy.Spider):
    name = "MbnecuadorIndividual"
    
   
    def start_requests(self):
        with open('artistas.json') as data_file:    
            data = json.load(data_file)
        
        for artista in data:
            yield scrapy.Request(url=artista['url'], callback=self.parse)
    
    '''
    def start_requests(self):
        urls = [
            'http://mbnecuador.com/mbnecuador/releases/acacia/',
            'http://mbnecuador.com/mbnecuador/releases/armando-chiliquinga-2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''
    def parse(self, response):

        #Formato 1
       
        item = dict(
            nombre = response.css('h1.page-title::text').extract_first(),
            url = response.request.url,
            video = response.xpath('//iframe[contains(@src,"youtube.com")]/@src').extract_first(),
            facebook = response.xpath('//article/p/a[contains(@href,"facebook.com")]/@href').extract_first(),
            twitter = response.xpath('//article/p/a[contains(@href,"twitter.com")]/@href').extract_first(),
            youtube = response.xpath('//article/p/a[contains(@href,"youtube.com")]/@href').extract_first(),
            instagram  = response.xpath('//article/p/a[contains(@href,"instagram.com")]/@href').extract_first(),

        )

        #item = ArtistaItem()
        
        #item['nombre'] = response.css('h1.page-title::text').extract_first(),
        #item['url'] = response.request.url,
        #item['video'] = response.xpath('//iframe[contains(@src,"youtube.com")]/@src').extract_first(),
        #item['facebook'] = response.xpath('//article/p/a[contains(@href,"facebook.com")]/@href').extract_first(),
        #item['twitter'] = response.xpath('//article/p/a[contains(@href,"twitter.com")]/@href').extract_first(),
        #item['youtube'] = response.xpath('//article/p/a[contains(@href,"youtube.com")]/@href').extract_first(),
        #item['instagram'] = response.xpath('//article/p/a[contains(@href,"instagram.com")]/@href').extract_first(),

        #Validar opcion 2, si redes sociales no se logo
        if item['facebook'] is  None and item['twitter'] is  None and item['youtube'] is  None and item['instagram'] is  None:
           item['facebook'] = response.xpath('//article/p/span/a[contains(@href,"facebook.com")]/@href').extract_first()
           item['twitter'] = response.xpath('//article/p/span/a[contains(@href,"twitter.com")]/@href').extract_first()
           item['youtube'] = response.xpath('//article/p/span/a[contains(@href,"youtube.com")]/@href').extract_first()
           item['instagram'] = response.xpath('//article/p/span/a[contains(@href,"instagram.com")]/@href').extract_first()


        return item 