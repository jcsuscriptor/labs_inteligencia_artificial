from apiclient.discovery import build
from pprint import pprint

# arguments to be passed to build function
DEVELOPER_KEY = "DEVELOPER_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)


def video_channel(channel_id):

    # Call the videos.list method to retrieve video info
    result = youtube.channels().list(
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
    