import urllib.request
import json

def exist(url):

    try:
        result = urllib.request.urlopen(url)
        url = result.geturl()
        print(type(url))
        print(url)
        print(result.info())

        
    except Exception as ex:
        print('Problem: '+ url)
        #print(ex.message)
        print(ex)

exist('www.radiocatolicacuenca.com.ec')
exist('http://www.radiocatolicacuenca.com.ec')
exist('http://www.jmradio.net')
exist('http://www.radioelmercurio.com.ec')
exist('https://www.radioelmercurio.com.ec')
exist('http://www.radioesplendid.com.ec')
exist('http://t.co/KTvOnJjDck')

 

 

    

   