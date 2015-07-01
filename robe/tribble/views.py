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
	return render(request,'search.html')

def getchart():
	print '__init__'
	chart = flot.LineChart(SimpleDataSource(data=data))
	return chart

def stats(request):
	return render(request,'stats.html',{'chart':getchart()})
	

def trend(request):
	return render(request,'trending.html')