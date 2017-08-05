import sys
import facebook
import json
import re
import logging
import configuration

# create logger with 'spam_application'
logger = logging.getLogger(__name__)


graph = facebook.GraphAPI(access_token=configuration.ACCESS_TOKEN, version='2.9')

dataAsociadaFacebook = []


def getData():
    with open('../crawling_web/artistas_individuales.json') as data_file:    
        data = json.load(data_file)
    return data

def saveData(data):
    with open('artistas_facebook.json', 'w') as outfile:  
        json.dump(data, outfile)

def getFacebookId_forUrl(url):
    # Regular Expressions for url facebook. 
    exRegFacebook = r'https://www.facebook.com/(.*)/.*|https://www.facebook.com/(.*)'
    match  = re.match( exRegFacebook, url, re.M|re.I)
    if match:
       if match.group(1):
           return match.group(1)
       if match.group(2):
           return match.group(2)
    return None


def getFacebookInfo(url):
    if url is None:
        return None,None

    id = getFacebookId_forUrl(url)

    if id is None:
        return None,None
 
    
    try:
        page = graph.get_object(id=id, 
        fields='id,artists_we_like,hometown,influences,press_contact,record_label,band_interests,band_members,bio,emails,about,genre,current_location,contact_address,general_manager,booking_agent,birthday,awards,phone,username,website,release_date,is_verified,name,impressum,description')

        return page,None
    except facebook.GraphAPIError as ex:
        error = {}
        error['message'] = ex.message
        error['code'] = ex.code 
        return None,error

    except Exception as ex:
        logger.error( sys.exc_info())
        error = {}
        error['message'] = ex.message
        error['code'] = ex.code 
        return None,error
        

data = getData()

for artista in data:
    dataFacebook = {}
    dataFacebook['nombre'] = artista['nombre']
    dataFacebook['url'] = artista['url']
    dataFacebook['facebook'] = artista['facebook']
    facebookInfo,Error  = getFacebookInfo(dataFacebook['facebook']) 
    if facebookInfo is not None:
        dataFacebook['facebookInfo'] = facebookInfo
    if Error is not None:
        dataFacebook['error'] = Error
    
    dataAsociadaFacebook.append(dataFacebook)

#Save json
saveData(dataAsociadaFacebook)