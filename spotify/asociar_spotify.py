import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import logging
import configuration

logger = logging.getLogger(__name__)

 


def getData():
    with open('../crawling_web/artistas_individuales.json') as data_file:    
        data = json.load(data_file)
    return data


def saveData(data):
    with open('artistas_spotify.json', 'w') as outfile:  
        json.dump(data, outfile)

def getArtist(data):
    artist = {}
    total = data['artists']['total']
    #if exit one result
    if total==1:
        item = data['artists']['items'][0]
        artist['spotify'] = item['external_urls']['spotify']
        artist['followers'] = item['followers']['total']
        artist['id'] = item['id']
        artist['images'] = item['images']
        artist['genres'] = item['genres']
        artist['name'] = item['name']
        artist['popularity'] = item['popularity']
        artist['uri'] =  item['uri']
    return artist

def getSpotifyInfo(name):
    #search artist for name
    results = spotifyAPI.search(q='artist:' + name, type='artist')
    return getArtist(results)

#main
spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)

data = getData() 

dataAsociada = []

for artista in data:
    dataSpotify = {}
    dataSpotify['nombre'] = artista['nombre']
    dataSpotify['url'] = artista['url']
    dataSpotify['spotifyInfo'] =  getSpotifyInfo(artista['nombre'])
    
    dataAsociada.append(dataSpotify)


saveData(dataAsociada)