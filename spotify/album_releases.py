import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint
import configuration



def saveData(data):
    with open('album_releases.json', 'w') as outfile:  
        json.dump(data, outfile)


spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)

#results = spotify.categories(country='EC')
results =  spotifyAPI.new_releases(country='EC')
saveData(results)