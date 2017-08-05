import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configuration
import pprint


spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)


def getData():
    with open('../crawling_web/artistas_individuales.json') as data_file:    
        data = json.load(data_file)
    return data


def saveData(data):
    with open('artistas_spotify_labs.json', 'w') as outfile:  
        json.dump(data, outfile)

def getArtist(data):
    artist = {}
    total = results['artists']['total']
    #if exit one result
    if total==1:
        item = results['artists']['items'][0]
        artist['spotify'] = item['external_urls']['spotify']
        artist['followers'] = item['followers']['total']
        artist['id'] = item['id']
        artist['images'] = item['images']
        artist['name'] = item['name']
        artist['popularity'] = item['popularity']
        artist['uri'] =  item['uri']
    return artist

data = getData() 

dataSave = []

index = 0
while index < 5 and index < len(data):
    #print(index, data[index])
    name = data[index]['nombre']
    results = spotifyAPI.search(q='artist:' + name, type='artist')
    artist = getArtist(results)
    dataSave.append(results)
    dataSave.append(artist)

    index += 1

saveData(dataSave)