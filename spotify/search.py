# shows artist info for a URN or URL

import spotipy
import sys
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'soda stereo'

client_credentials_manager = SpotifyClientCredentials(client_id = "efb1585a452d4930af31ca24ee893910",
                                   client_secret = "c28b1c21d3f54ffbbbdad1c33fc1d237")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)
pprint.pprint(result)