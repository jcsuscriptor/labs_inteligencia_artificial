import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#My Applications - https://developer.spotify.com
client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='soda stereo', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'], ' - ') #, t['release_date'])
    

 