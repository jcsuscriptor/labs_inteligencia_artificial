import twitter
import configuration

api = twitter.Api(consumer_key=configuration.CONSUMER_KEY,
                  consumer_secret=configuration.CONSUMER_SECRET,
                  access_token_key=configuration.ACCESS_TOKEN_KEY,
                  access_token_secret=configuration.ACCESS_TOKEN_SECRET)

#print(api.VerifyCredentials())

followers = api.GetFollowers()
print(followers)

response = api.GetFollowerIDs(None, 'RadioCatolicaC')
#print(response)