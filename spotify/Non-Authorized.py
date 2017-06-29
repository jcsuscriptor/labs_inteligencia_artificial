
#
# requests.exceptions.HTTPError: 401 Client Error: 
# Unauthorized for url: https://ai.spotify.com/v1/search?q=artist%3Asoda+stereo&limit=10&offset=0&type=artist
#
# Informacion del error:
# https://developer.spotify.com/news-stories/2017/01/27/removing-unauthenticated-calls-to-the-web-api/

import spotipy
name = "soda stereo"
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)