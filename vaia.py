#!/usr/bin/env python
import tweepy, sys, time, requests, random
#from our keys module (keys.py), import the keys dictionary
from keys import keys

 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
print("Welcome to VaiaTemer")



#precisamos de uma lista de vaias para randomizar, adicionar mais a vontade
vaias = ("buuuuuuu", "buuuuuuuuuuuuu", "buu", "primeiramente, buuuuuuu", "fooooooora", "fooooooooooooooooooora")

        

	
#escolhendo quem responder
toReply = "MichelTemer" 

#puxando tweets
tweets = api.user_timeline(screen_name = toReply, count=200)


#loop principal da brincadeira
for tweet in tweets:
	api.update_status(status=random.choice(vaias)+ " #ForaTemer @" + toReply, in_reply_to_status_id = tweet.id)
	print("Vaia vaiada")
	time.sleep(random.randint(120,180))

