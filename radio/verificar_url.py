import urllib.request
import json
import datetime
import re


#Verificar url

'''
url_verified
	exist : boolean
	url_twitter : url
	exist_url_twitter: boolean 
'''

def getData():
    with open('../twitter/medios_radio_info_twitter.json') as data_file:    
        data = json.load(data_file)

    return data    

def datetime_handler(obj):
    #https://stackoverflow.com/questions/35869985/datetime-datetime-is-not-json-serializable

    #Use ISO 8601
    #https://stackoverflow.com/questions/10286204/the-right-json-date-format
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Unknown type")

def saveData(data):
    with open('radio_url_verificada.json', 'w') as outfile:  
        json.dump(data, outfile)

def verificarUrl(url):
    
    if url is None:
       return url,False
    
    exReg = r'(?:http|https)://'
    match  = re.match( exReg, url, re.M|re.I)
    if not match:
        url = 'http://'+url


    try:
    
        result = urllib.request.urlopen(url)
        return result.geturl() , True 

    except Exception as ex:
       
       return url,False


def getDataInfo(data):
    url = data['Sitio Web']
    url_twitter = None

    if 'twiiterInfo' in data and data['twiiterInfo'] is not None:
       if 'url' in data['twiiterInfo']:
           url_twitter =   data['twiiterInfo']['url']
    
    url,result = verificarUrl(url)
    url_verified = {}
    url_verified['exist'] = result
    url_verified['url_twitter'] = url_twitter
    
    url_T,resultT = verificarUrl(url_twitter)
    url_verified['url_twitter'] = url_T    
    url_verified['exist_url_twitter'] = resultT
   
    return url_verified,None


dataAsociada = []

data = getData()

for item in data:
    dataItem = {}
    dataItem  = item

    Info,Error  = getDataInfo(item)
    if Info is not None:
        dataItem['url_verified'] = Info
    if Error is not None:
        dataItem['error_url_verified'] = Error

    dataAsociada.append(dataItem)


saveData(dataAsociada)