import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint
import configuration

 
spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)

def saveData(data):
    with open('artist_related_artists.json', 'w') as outfile:  
        json.dump(data, outfile)
 
artist_id = "spotify:artist:3Of13uTPqUVwBPz8gpz5kN"
results =  spotifyAPI.artist_related_artists(artist_id)
saveData(results)