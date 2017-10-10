import tweepy
import json
from json import  JSONEncoder, JSONDecoder
import pickle
import pprint
import configuration

auth = tweepy.OAuthHandler(consumer_key=configuration.CONSUMER_KEY, consumer_secret=configuration.CONSUMER_SECRET)
auth.set_access_token(configuration.ACCESS_TOKEN_KEY, configuration.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


user = api.get_user('mercurioec')
print(user.id_str)
print(user) 
