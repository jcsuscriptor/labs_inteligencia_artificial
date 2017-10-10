import scrapy
import json
import re
import logging

logger = logging.getLogger(__name__)

  



def getUrl(item):
    url = None
    if item['url_verified']['exist'] or item['url_verified']['exist_url_twitter']:
        if item['url_verified']['exist']:               
            url =  item['Sitio Web']
        else:
            url =  item['url_verified']['url_twitter']
    
    if url:
        exReg = r'(?:http|https)://'
        match  = re.match( exReg, url, re.M|re.I)
        if not match:
            url = 'http://'+url

    return url


class RadioAudioSpider(scrapy.Spider):
    name = "Radio Audio"

  
   
    def start_requests(self):
        with open('../radio/radio_url_verificada.json') as data_file:    
            data = json.load(data_file)
        
        for radio in data:
            url = getUrl(radio)
            if url is not None:
                yield scrapy.Request(url=url, callback=self.parse)
    

    '''
    start_urls = [
        'http://armoniasuperfm.com/',
    ]
    '''

  
    def playerHtml(self,response):
        player = {}
        #1
        amazingaudioplayer =  response.css('*.amazingaudioplayer-source')
        if amazingaudioplayer:
           player['player'] = 'amazingaudioplayer'
           player['stream'] = amazingaudioplayer.css('::attr(data-src)').extract_first()

        #2 https://www.muses.org/
        muses = response.xpath('//script[contains(@src,"https://hosted.muses.org/mrp.js")]/@src')
        if muses:
           player['player'] = 'muses.org' 
           player['stream'] = response.css('script').re('\s*MRP.insert\(\W*\'url\'\s*:\s*\'(.+)\'')


        return player

    def parse(self, response):
       
        data = dict(
            title = response.css('title::text').extract_first(),
            url = response.request.url 
        )
 
        #1
        player = self.playerHtml(response)
        if player:
            data['stream'] = player

        yield  data  
    

        flashradio = response.css('script').re_first(r'\$\(".*"\).flashradio\(.*settings:\s+"(.*)".*\)')
        if flashradio:
            next_page = response.urljoin(flashradio)
            yield scrapy.Request(next_page, callback=self.parse)

        #Buscar otra forma
        #Add iframe
        #for item in response.css('iframe::attr(src)'):
        #    next_page = item.extract()
        #    if next_page is not None:
        #        next_page = response.urljoin(next_page)
        #        yield scrapy.Request(next_page, callback=self.parse)
