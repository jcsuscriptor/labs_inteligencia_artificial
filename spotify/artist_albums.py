import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#Auth
client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

 
birdy_uri = "spotify:artist:0ZFREHdcfpfQdXwR8mGov4"

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])