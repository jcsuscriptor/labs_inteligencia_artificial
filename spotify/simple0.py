import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#My Applications - https://developer.spotify.com
client_credentials_manager = SpotifyClientCredentials(client_id = "efb1585a452d4930af31ca24ee893910",
                                   client_secret = "c28b1c21d3f54ffbbbdad1c33fc1d237")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='soda stereo', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'], ' - ', t['release_date'])
    

 