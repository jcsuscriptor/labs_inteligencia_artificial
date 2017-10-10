import tweepy
import json
import re
import logging
import sys
import datetime


import configuration

logger = logging.getLogger(__name__)


def datetime_handler(obj):
    #https://stackoverflow.com/questions/35869985/datetime-datetime-is-not-json-serializable

    #Use ISO 8601
    #https://stackoverflow.com/questions/10286204/the-right-json-date-format
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Unknown type")

def getData():
    with open('../crawling_web/radio.ec.json') as data_file:    
        data = json.load(data_file)

    return data


def saveData(data):
    with open('medios_radio_info_twitter.json', 'w') as outfile:  
        json.dump(data, outfile, default=datetime_handler)


def getTwitterUserName(data):
    # Regular Expressions for url facebook. 
    exReg = r'@(.+)|(.+)'
    match  = re.match( exReg, data, re.M|re.I)
    if match:
       if match.group(1):
           return match.group(1)
       if match.group(2):
           return match.group(2)
    return None

def getInfoTwitter(userName):
    twitterInfo = {}

    if userName is None:
       return twitterInfo,None

    userSearch = getTwitterUserName(userName)
    try:

        response = twitterAPI.get_user(userSearch)
        twitterInfo['id'] = response.id
        twitterInfo['id_str'] = response.id_str
        twitterInfo['name'] = response.name
        twitterInfo['screen_name'] = response.screen_name
        twitterInfo['location'] = response.location
        twitterInfo['description'] = response.description
        twitterInfo['url'] = response.url
        twitterInfo['followers_count'] = response.followers_count
        twitterInfo['friends_count'] = response.friends_count
        twitterInfo['listed_count'] = response.listed_count
        twitterInfo['created_at'] = response.created_at
        twitterInfo['favourites_count'] = response.favourites_count
        twitterInfo['time_zone'] = response.time_zone
        twitterInfo['geo_enabled'] = response.geo_enabled
        twitterInfo['verified'] = response.verified
        twitterInfo['statuses_count'] = response.statuses_count
        twitterInfo['lang'] = response.lang
        return twitterInfo,None
    except tweepy.error.TweepError as ex:
        error = {}
        error['message'] = ex.reason 
        error['code'] = ex.api_code 
        return None,error
    
    except Exception as ex:
        logger.error( sys.exc_info())
        error = {}
        error['message'] = ex.message
        error['code'] = ex.code 
        return None,error
 

auth = tweepy.OAuthHandler(consumer_key=configuration.CONSUMER_KEY, consumer_secret=configuration.CONSUMER_SECRET)
auth.set_access_token(configuration.ACCESS_TOKEN_KEY, configuration.ACCESS_TOKEN_SECRET)

twitterAPI = tweepy.API(auth)

data = getData() 

dataAsociada = []

for item in data:
    dataItem = {}
    dataItem  = item

    twitterInfo,Error  = getInfoTwitter(item['Twitter'])
    if twitterInfo is not None:
        dataItem['twiiterInfo'] = twitterInfo
    if Error is not None:
        dataItem['error'] = Error

    dataAsociada.append(dataItem)


saveData(dataAsociada)