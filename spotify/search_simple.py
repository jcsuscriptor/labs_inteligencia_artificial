import spotipy
import configuration 

spotifyAPI = spotipy.Spotify(client_credentials_manager=configuration.client_credentials_manager)

results = spotifyAPI.search(q='soda stereo', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'], ' - ') #, t['release_date'])
    

 