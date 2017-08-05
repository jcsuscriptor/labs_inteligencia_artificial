
import requests
import pprint

payload = {}
r = requests.get('https://api.acrcloud.com/v1/monitor-streams/11578/results?access_key=ACCESS_KEY&limit=5')

pprint.pprint(r.json())