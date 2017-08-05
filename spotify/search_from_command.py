# shows artist info for a URN or URL

import spotipy
import sys
import pprint
import configuration 

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'soda stereo'

 
spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)

result = spotifyAPI.search(search_str)
pprint.pprint(result)