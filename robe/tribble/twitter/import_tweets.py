import tweepy
import time
from tribble.models import Words_India, Words_Global
import sys

consumer_key = 'MbiHzivAIk3vLkWj19zVcw1WI'
consumer_secret = 'ctZF0ZwAQrhWnn90qiMyBvdRPpO4YgCEX8n6QkGNqN4q1XDrok'

access_token = '3253361905-3uXheHOx2Si4DE0Rio46NM9iNKjcwXPLpRZTeIV'
access_token_secret = 'RIoJvqwIimHuVlL7IBmfuloPSBPla2khnpXHV4rZE0j03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def import_tweets():
	i=0
	prev = ['']
	#for j in range(0,24):
	#	time.sleep(60*60)
	try:
		location = api.trends_available()
		for loc in location:
			if loc['country'] == 'India':
				for out in api.trends_place(loc['woeid']):
					i += 1
					for name in out['trends']:
						w = name['name'].encode('utf-8')
						Words_India.objects.create(word_name=w,date_time=out['created_at'].split('T')[0],word_from=loc['country'])
					if i>1:
						break
			if loc['country'] not in prev and loc['country']!='India':
				prev += [loc['country']]
				for out in api.trends_place(loc['woeid']):
					i += 1
					for name in out['trends']:
						w = name['name'].encode('utf-8')
						Words_Global.objects.create(word_name=w,date_time=out['created_at'].split('T')[0],word_from=loc['country'])
					if i>13:
						break
			if i>15:
				break
	except tweepy.TweepError:
		pass