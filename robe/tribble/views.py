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


class HomeView(generic.TemplateView):
	template_name='index.html'

class SearchView(generic.TemplateView):
	template_name='search.html'

class StatsView(generic.TemplateView):
	template_name='stats.html'

class TrendView(generic.TemplateView):
	template_name='trending.html'