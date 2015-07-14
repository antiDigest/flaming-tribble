from django.shortcuts import render
from django.http import Http404
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
from tribble.forms import SearchForm
from django.core.exceptions import ObjectDoesNotExist
from graphos.renderers import gchart
from tribble.twitter.sentiment import *
import tweepy

classifier = trainClassifier()

data =  [
        ['Name', 'Percent'],
        ['facebook', 33],
        ['youtube', 43],
        ['twitter', 54],
    ]

data2 =  [
        ['Year', 'facebook', 'Twitter', 'Youtube'],
        [2004, 33, 897, 98],
        [2005, 3332, 89, 982],
        [2006, 332, 711, 928],
    ]

consumer_key = 'MbiHzivAIk3vLkWj19zVcw1WI'
consumer_secret = 'ctZF0ZwAQrhWnn90qiMyBvdRPpO4YgCEX8n6QkGNqN4q1XDrok'

access_token = '3253361905-3uXheHOx2Si4DE0Rio46NM9iNKjcwXPLpRZTeIV'
access_token_secret = 'RIoJvqwIimHuVlL7IBmfuloPSBPla2khnpXHV4rZE0j03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def home(request):
    return render(request,'index.html')

def trend(request, value):
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['name']
            qtext = query.split()
            
            word = []
            for i in qtext:
                words = Words_India.objects.filter(word_name__contains=i)
                word += [k for k in words]
            
            words_g = []
            for i in qtext:
                words = Words_Global.objects.filter(word_name__contains=i)
                words_g += [k for k in words]
            
        if value !='India':
            word = words_g
        return render(request,'trending.html',{'word':word,'form':form,'value':value,'query':query} )
    else:
        form = SearchForm()
        word = Words_India.objects.all()[:50]

        words_g = Words_Global.objects.all()[:50]

        if value !='India':
            word = words_g

        return render(request,'trending.html',{'word':word,'form':form,'value':value} )

def getchart():
    chart = gchart.PieChart(SimpleDataSource(data=data))
    return chart

def stats(request):
    chart2 = gchart.LineChart(SimpleDataSource(data=data2))
    return render(request,'statistics.html',{'chart':getchart(), 'charti':chart2})
    
def fetch(request):
    import_tweets.import_tweets_india()
    words_i = Words_India.objects.all().order_by('-id')[:50]

    import_tweets.import_tweets_global()

    return render(request,'trending.html',{'word':words_i,'form':SearchForm()})

def noRedundant(request):
    print 'Removing global ...'
    wi = Words_Global.objects.all()
    
    for i in wi:
        if Words_India.objects.filter(word_name=i.word_name,onlydate=i.onlydate,senti_flag=i.senti_flag).count() > 1:
            i.delete()

    print 'Removing Indian ...'
    wi = Words_India.objects.all()
    
    for i in wi:
        if Words_India.objects.filter(word_name=i.word_name,onlydate=i.onlydate,senti_flag=i.senti_flag).count() > 1:
            i.delete()
            
    words_i = Words_India.objects.all()[:50]

    form = SearchForm()

    return render(request,'trending.html',{'word':words_i,'form':form, 'value':'India'})

def search(request, value):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return render(request,'search.html',{'query':query,'form':form, 'value':'India'})
    else:
        query = request.GET.get('query')
        searches = api.search(query,lang="en",since='2015-04-01',untill=time.strftime('%Y-%m-%d'),count=100)
        statement = []
        linesearch = api.search(query,lang="en",since='2015-04-01',untill=time.strftime('%Y-%m-%d')\
            ,count=100, result_type='popular')
        for search in searches:
            k = search._json['user']
            statement += [textCleaner(search.text)]
        senti_neut, senti_neg, senti_pos, tot = getSenti(statement, classifier)

        # Words_India.objects.filter(word_name=word).aggregate(Max())

        data = [['Sentiment','Percentage'],['Negative',senti_neg],['Positive',senti_pos],['Neutral',senti_neut],]
        piechart = gchart.PieChart(SimpleDataSource(data=data))

        data=[['Time','Favourties'],]
        for search in linesearch:
            data += [[str(search.created_at),search.favorite_count]]

        print data
        linechart = gchart.LineChart(SimpleDataSource(data=data))
        return render(request,'search.html',{'query':query,'form':SearchForm(), \
        'value':'India', 'piechart':piechart, 'linechart':linechart})

def show(request,value,word):
    searches = api.search(word,lang="en",since='2015-04-01',untill=time.strftime('%Y-%m-%d'),count=100)
    statement = []
    for search in searches:
        k = search._json['user']
        statement += [textCleaner(search.text)]
    senti_neut, senti_neg, senti_pos, tot = getSenti(statement, classifier)

    # Words_India.objects.filter(word_name=word).aggregate(Max())

    data = [['Sentiment','Percentage'],['Negative',senti_neg],['Positive',senti_pos],['Neutral',senti_neut],]
    piechart = gchart.PieChart(SimpleDataSource(data=data))
    linechart = None
    return render(request,'search.html',{'query':word,'form':SearchForm(), \
        'value':'India', 'piechart':piechart, 'linechart':linechart})
    