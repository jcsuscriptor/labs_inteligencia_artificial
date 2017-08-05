# shows artist info for a URN or URL

import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'soda stereo'

client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)
pprint.pprint(result)