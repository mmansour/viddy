from viddypull.models import *

from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django import forms
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect

def home(request):
    viddy = Viddy.objects.all()
    return render_to_response('index.html',{"viddy":viddy},
                context_instance=RequestContext(request))