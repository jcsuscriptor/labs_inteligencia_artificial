from apiclient.discovery import build
import json
from pprint import pprint
import logging
import re

# arguments to be passed to build function
DEVELOPER_KEY = "DEVELOPER_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)


# Regular Expressions for url field youtube. User or Channel
exRegUser = r'https://www.youtube.com/user/(.*)'
exRegChannel = r'https://www.youtube.com/channel/(.*)'


dataAsociadaYoutube = []


logging.info('Get File')

def youtube_video_details(video_id):

    # Call the videos.list method to retrieve video info
    result = youtube.videos().list(
        id = video_id,
        part = "snippet" #id,snippet,contentDetails,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    if result is not None and len(result['items']) > 0:
        video['title'] = result['items'][0]['snippet']['title']
        #video['tags'] = result['items'][0]['snippet']['tags']
        video['descr'] = result['items'][0]['snippet']['description']
        video['channelId'] = result['items'][0]['snippet']['channelId']
        if 'contentDetails' in result['items'][0]:
            video['content'] = result['items'][0]['contentDetails']
        if 'statistics' in result['items'][0]:
            video['stats'] = result['items'][0]['statistics']
    
    return video

def youtube_video_channel(channel_id):

    # Call the videos.list method to retrieve video info
    resultChannel = youtube.channels().list(
        id = channel_id,
        part = "id,snippet,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    if resultChannel is not None and len(resultChannel['items']) > 0:
        video['channelId'] = resultChannel['items'][0]['id']
        video['title'] = resultChannel['items'][0]['snippet']['title']
        video['description'] = resultChannel['items'][0]['snippet']['description']
        video['stats'] = resultChannel['items'][0]['statistics']

    return video

def youtube_video_channel_forUsername(userName):

    # Call the videos.list method to retrieve video info
    resultChannel = youtube.channels().list(
        forUsername = userName,
        part = "id,snippet,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    if resultChannel is not None and len(resultChannel['items']) > 0:
        video['channelId'] = resultChannel['items'][0]['id']
        video['title'] = resultChannel['items'][0]['snippet']['title']
        if 'country' in resultChannel['items'][0]['snippet']:
            video['country'] = resultChannel['items'][0]['snippet']['country']
        video['description'] = resultChannel['items'][0]['snippet']['description']
        video['stats'] = resultChannel['items'][0]['statistics']

    return video

def getData():
    with open('../crawling_web/artistas_individuales.json') as data_file:    
        data = json.load(data_file)

    return data

def saveData(data):
    with open('artistas_youtube.json', 'w') as outfile:  
        json.dump(data, outfile)


data = getData()

 
for artista in data:
    dataYoutube = {}
    dataYoutube['nombre'] = artista['nombre']
    dataYoutube['url'] = artista['url']
    dataYoutube['youtube'] = artista['youtube']

    _videoData = artista['video'] 
    
  
    #If youtube is  None, get chanelId from video
    if dataYoutube['youtube'] is None and _videoData  is not None: 
        #video: http://www.youtube.com/embed/3cEQC_RW1bo 
        video_id = _videoData.split("/")[-1]
        result = youtube_video_details(video_id)
        if result is not None and 'channelId' in result:
            #https://www.youtube.com/channel/UCEm3eGhDH2W02i1VHVB4Iww
            #logging.debug('channelId: ' + result['channelId'])
            dataYoutube['youtube'] = "https://www.youtube.com/channel/" + result['channelId']
    
    #Si url youtube, es el user.
    #https://www.youtube.com/user/JorgeLuisPeralta
   
    if dataYoutube['youtube'] is not None:
        
        matchUrlUser = re.match( exRegUser, dataYoutube['youtube'], re.M|re.I) 
        if matchUrlUser:
            dataYoutube['youtube.user'] = dataYoutube['youtube']
            userNameYoutube =  matchUrlUser.group(1)
            channelInfo = youtube_video_channel_forUsername(userNameYoutube)    
        
            dataYoutube['channelInfo'] = channelInfo
            dataYoutube['youtube'] = "https://www.youtube.com/channel/" + channelInfo['channelId']
        else:
            #Get Info Youtube Channel
            #https://www.youtube.com/channel/UCEm3eGhDH2W02i1VHVB4Iww
            channel_id = dataYoutube['youtube'].split("/")[-1]
            channelInfo = youtube_video_channel(channel_id)    
            dataYoutube['channelInfo'] = channelInfo
    
    dataAsociadaYoutube.append(dataYoutube)

#Save json
saveData(dataAsociadaYoutube)