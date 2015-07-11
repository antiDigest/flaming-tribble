import tweepy
import time
from tribble.sentiment.get_related import MakeSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings
from scrapy.utils.trackref import iter_all

configure_logging()

consumer_key = 'MbiHzivAIk3vLkWj19zVcw1WI'
consumer_secret = 'ctZF0ZwAQrhWnn90qiMyBvdRPpO4YgCEX8n6QkGNqN4q1XDrok'

access_token = '3253361905-3uXheHOx2Si4DE0Rio46NM9iNKjcwXPLpRZTeIV'
access_token_secret = 'RIoJvqwIimHuVlL7IBmfuloPSBPla2khnpXHV4rZE0j03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def import_tweets_india():
	i=0
	prev = []
	#for j in range(0,24):
	#	time.sleep(60*60)
	#f = open('output.txt','a')
	dictionary = {}
	location = api.trends_available()
	for loc in location:
		if loc['country'] == 'India':
			prev += [loc['country']]
			for out in api.trends_place(loc['woeid']):
				i += 1
				for json in out['trends']:
					trend = json['name'].encode('utf-8')
					print trend, json['url'] 
					dictionary[trend] = [json['url'],loc['country']]
					process = Crawler(MakeSpider,settings = Settings(values={}, priority='project'))
					process.crawl(url=json['url'],country='India')
					if reactor.running: 
						reactor.stop()
					reactor.run()# the script will block here until the crawling is finished
					process.signals.connect(reactor.stop(), signal=signals.request_scheduled)
					

def import_tweets_global():
	i=0
	prev = []
	#for j in range(0,24):
	#	time.sleep(60*60)
	#f = open('output.txt','a')
	
	dictionary = {}
	location = api.trends_available()
	for loc in location:
		if loc['country'] != 'India' and loc['country'] not in prev:
			prev += [loc['country']]
			for out in api.trends_place(loc['woeid']):
				i += 1
				for json in out['trends']:
					trend = json['name'].encode('utf-8')
					print trend, json['url'] 
					dictionary[trend] = [json['url'],loc['country']]
					process = Crawler(MakeSpider,settings = Settings(values={}, priority='project'))
					process.crawl(url=json['url'],country='India')				
				
					if reactor.running: 
						reactor.stop()
					sentiment = reactor.run()# the script will block here until the crawling is finished
					process.signals.connect(reactor.stop(), signal=signals.request_scheduled)

