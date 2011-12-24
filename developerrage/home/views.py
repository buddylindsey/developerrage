from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from comic.models import *

def index(request):
    comics = Comic.objects.filter(approved=True).order_by('-id')
    return render_to_response("home/index.html",
            { 'comics': comics },
            context_instance=RequestContext(request))

def about(request):
    return render_to_response("home/about.html",
            { },
            context_instance=RequestContext(request))
