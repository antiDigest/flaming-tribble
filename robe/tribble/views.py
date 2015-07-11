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
from django.core.exceptions import ObjectDoesNotExist


data =  [
        ['Year', 'facebook', 'twitter', 'youtube'],
        [2004, 1000, 400, 893],
        [2005, 1170, 460, 837],
        [2006, 660, 1120, 327],
        [2007, 1030, 540, 1900]
    ]
	

def home(request):
	return render(request,'index.html')

def search(request):
   	try:
	    words_g = Words_Global.objects.all().order_by('-id')[:50]
	except ObjectDoesNotExist:
   	    print("Entry doesn't exist.")

	return render(request,'search.html',{'word':words_g})

def getchart():
	print '__init__'
	chart = flot.LineChart(SimpleDataSource(data=data))
	return chart

def stats(request):
	return render(request,'stats.html',{'chart':getchart()})
	
def fetch(request):
	import_tweets.import_tweets_india()
	words_g = Words_India.objects.all().order_by('-id')[:50]
	
	return render(request,'search.html',{'word':words_g})

def fetch_global(request):
	import_tweets.import_tweets_global()
	# sentiment.getSenti()
	try:
	    words_g = Words_Global.objects.all().order_by('-id')[:50]
	except ObjectDoesNotExist:
   	    print("Entry doesn't exist.")

	return render(request,'search.html',{'word':words_g})

def noRedundant(request):
	words_g = Words_Global.objects.all()
	for word in words_g:
		wn = word.word_name
		wf = word.word_from
		ws = word.sentiment
		wd = word.date_time
		deleter = Words_Global.objects.filter(word_name=wn)
		for i in deleter:
			#print i.word_name
			i.delete()
		Words_Global.objects.create(word_name=wn,word_from=wf,sentiment=ws,date_time=wd)
	words_g = Words_Global.objects.all().order_by('-id')[:50]

	return render(request,'search.html',{'word':words_g})