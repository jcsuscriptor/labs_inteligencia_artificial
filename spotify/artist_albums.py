import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configuration

spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)


 
birdy_uri = "spotify:artist:0ZFREHdcfpfQdXwR8mGov4"

results = spotifyAPI.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotifyAPI.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])