import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint

#Auth
client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def saveData(data):
    with open('artist_related_artists.json', 'w') as outfile:  
        json.dump(data, outfile)
 
artist_id = "spotify:artist:3Of13uTPqUVwBPz8gpz5kN"
results =  spotify.artist_related_artists(artist_id)
saveData(results)