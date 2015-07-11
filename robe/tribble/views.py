from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from graphos.renderers import flot
from graphos.sources.model import SimpleDataSource
from .models import Words_Global, Words_India
from tribble.twitter import import_tweets
import time
import thread
from django.core.exceptions import ObjectDoesNotExist
from tribble.sentiment.get_related import MakeSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, Crawler
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings
from scrapy.utils.trackref import iter_all
from .forms import SelectForm

configure_logging()

data =  [
        ['Year', 'facebook', 'twitter', 'youtube'],
        [2004, 1000, 400, 893],
        [2005, 1170, 460, 837],
        [2006, 660, 1120, 327],
        [2007, 1030, 540, 1900]
    ]
	

def home(request):
	return render(request,'index.html')

def search(request, value):
	
	word = Words_India.objects.all().order_by('-id')[:50]

	words_g = Words_Global.objects.all().order_by('-id')[:50]

	if value !='India':
		word = words_g
	else:
		print 'Form return invalid'

	return render(request,'search.html',{'word':word} )

def getchart():
	print '__init__'
	chart = flot.LineChart(SimpleDataSource(data=data))
	return chart

def stats(request):
	return render(request,'stats.html',{'chart':getchart()})
	
def fetch(request):
	import_tweets.import_tweets_india()
	words_i = Words_India.objects.all().order_by('-id')[:50]
	
	urls = []
	k = Words_India.objects.all()
	for i in k:
		urls += i.url

	# thread.start_new_thread(crawlThread, (urls,'India', ) )

	import_tweets.import_tweets_global()
	# sentiment.getSenti()
	try:
	    words_g = Words_Global.objects.all().order_by('-id')[:50]
	except ObjectDoesNotExist:
   	    print("Entry doesn't exist.")

   	urls = []
	k = Words_Global.objects.all()
	for i in k:
		urls += i.url

	# thread.start_new_thread(crawlThread, (urls,'global', ) )

	return render(request,'search.html',{'wordg':words_g,'wordi':words_i})

def crawlThread(url, country):
	process = Crawler(MakeSpider,settings = Settings(values={}, priority='project'))
	process.crawl(url=url,country=country)
	reactor.run()# the script will block here until the crawling is finished
	process.signals.connect(reactor.stop(), signal=signals.request_scheduled)

def noRedundant(request):
	words_g = Words_Global.objects.all()
	for word in words_g:
		wn = word.word_name
		wf = word.word_from
		ws = word.sentiment
		wd = word.date_time
		wu = word.url
		deleter = Words_Global.objects.filter(word_name=wn)
		for i in deleter:
			#print i.word_name
			i.delete()
		Words_Global.objects.create(word_name=wn,word_from=wf,sentiment=ws,date_time=wd, url=wu)

	words_g = Words_India.objects.all()
	for word in words_g:
		wn = word.word_name
		wf = word.word_from
		ws = word.sentiment
		wd = word.date_time
		wu = word.url
		deleter = Words_India.objects.filter(word_name=wn)
		for i in deleter:
			#print i.word_name
			i.delete()
		Words_India.objects.create(word_name=wn,word_from=wf,sentiment=ws,date_time=wd, url=wu)
	words_i = Words_India.objects.all().order_by('-id')[:50]

	return render(request,'search.html',{'word':words_i})