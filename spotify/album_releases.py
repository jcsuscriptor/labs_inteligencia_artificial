import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint

#Auth
client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

 
 
def saveData(data):
    with open('album_releases.json', 'w') as outfile:  
        json.dump(data, outfile)


#results = spotify.categories(country='EC')
results =  spotify.new_releases(country='EC')
saveData(results)