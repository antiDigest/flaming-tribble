from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
 
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

