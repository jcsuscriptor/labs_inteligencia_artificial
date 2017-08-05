from apiclient.discovery import build
from pprint import pprint
import configuration


# creating youtube resource object for interacting with API
youtubeAPI = build(configuration.YOUTUBE_API_SERVICE_NAME, configuration.YOUTUBE_API_VERSION,
                developerKey=configuration.DEVELOPER_KEY)


def video_channel(channel_id):

    # Call the videos.list method to retrieve video info
    result = youtubeAPI.channels().list(
        id = channel_id,
        part = "snippet,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    video['title'] = result['items'][0]['snippet']['title']
    video['description'] = result['items'][0]['snippet']['description']
    video['stats'] = result['items'][0]['statistics']

    return video
    
 

if __name__ == "__main__":
    channel_id = "UCnQse6wRmpArT6zle6MT8CA"
    
    channelInfo = video_channel(channel_id)
     
    pprint(channelInfo)
    