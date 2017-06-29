
import requests
import pprint

payload = {}
r = requests.get('https://api.acrcloud.com/v1/monitor-streams/11578/results?access_key=8cc7fd4dab415952bfddd8b47e5e7cb5&limit=5')

pprint.pprint(r.json())