from viddypull.models import *

from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django import forms
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from mezzanine.utils.views import paginate
from django.db.models import Count

def home(request):
    sort_criteria = request.GET.get("sortby", '-like_count')
    viddy = Viddy.objects.all().order_by(sort_criteria)
    viddy = paginate(viddy,
                        request.GET.get("page", 1),
                        25, 25)

    tag_count = Tag.objects.values('tag', 'tag_id').annotate(tcount=Count('tag_id')).order_by('-tcount')[:100]

    return render_to_response('index.html',{"viddy":viddy, 'tag_count':tag_count},
                context_instance=RequestContext(request))


def viddy_details(request, viddy_id):
    viddy = Viddy.objects.get(pk=viddy_id)
    return render_to_response('pages/details.html',{"viddy":viddy},
                context_instance=RequestContext(request))


def viddys_by_tag(request, tag_id):
    sort_criteria = request.GET.get("sortby", '-viddy__like_count')
    tag = Tag.objects.filter(tag_id=tag_id).order_by(sort_criteria)
    tag = paginate(tag,
                        request.GET.get("page", 1),
                        25, 25)

    tag_count = Tag.objects.values('tag', 'tag_id').annotate(tcount=Count('tag_id')).order_by('-tcount')[:100]

    return render_to_response('pages/list-by-tag.html',{'tag':tag, 'tag_count':tag_count},
                context_instance=RequestContext(request))