import tweepy
from secrets import * #contains authemtication information for twitter

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

for friend in api.friends():
   print(friend.name)