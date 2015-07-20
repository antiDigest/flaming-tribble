import tweepy
import time
import thread
from tribble.models import Words_India, Words_Global
from tribble.twitter.sentiment import *
from graphos.sources.model import SimpleDataSource
from graphos.renderers import gchart
import sys
from robe.settings import BASE_DIR
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key = 'MbiHzivAIk3vLkWj19zVcw1WI'
consumer_secret = 'ctZF0ZwAQrhWnn90qiMyBvdRPpO4YgCEX8n6QkGNqN4q1XDrok'

access_token = '3253361905-3uXheHOx2Si4DE0Rio46NM9iNKjcwXPLpRZTeIV'
access_token_secret = 'RIoJvqwIimHuVlL7IBmfuloPSBPla2khnpXHV4rZE0j03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

country = os.path.join(BASE_DIR,'countries.txt')

with open(country,'r') as f:
    english = f.read().split('\n')

def import_tweets_india():
    i=0
    prev = []
    try:
        location = api.trends_available()
        for loc in location:
            if loc['country'] == 'India':
                prev += [loc['country']]
                # try:
                for out in api.trends_place(loc['woeid']):
                    i += 1
                    for json in out['trends']:
                        trend = json['name'].encode('utf-8')
                        Words_India.objects.create(word_name=trend,word_from=loc['country'])
                    
    except tweepy.TweepError:
        pass        

def import_tweets_global():
    i=0
    prev = []
    try:
        location = api.trends_available()
        for loc in location:
            if loc['country'] != 'India' and loc['country'] not in prev and loc['country'] not in english:
                prev += [loc['country']]
                # try:
                for out in api.trends_place(loc['woeid']):
                    i += 1
                    for json in out['trends']:
                        trend = json['name'].encode('utf-8')
                        Words_Global.objects.create(word_name=trend,word_from=loc['country'])
                    
    except tweepy.TweepError:
        pass    
   