import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

 
client_credentials_manager = SpotifyClientCredentials(client_id = "efb1585a452d4930af31ca24ee893910",
                                   client_secret = "c28b1c21d3f54ffbbbdad1c33fc1d237")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

 


playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None