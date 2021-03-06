from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from gleeoke.models import *

from django.db.models import Count

from django.http import HttpResponse
from django.utils import simplejson

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def choose(request, template_name='choose.html'):
    print('choosing')
    left_song = Song.objects.order_by('?')[0]
    right_song = Song.objects.exclude(pk=left_song.pk).order_by('?')[0]
    return render_to_response(template_name, {'left_song':left_song, 'right_song':right_song}, context_instance=RequestContext(request))

def what_is_this(request, template_name='what-is-this.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))

def vote(request):
    if request.method == 'POST' and 'badsong' in request.POST and 'worsesong' in request.POST:
        badsong = Song.objects.get(short_id=request.POST['badsong'])
        worsesong = Song.objects.get(short_id=request.POST['worsesong'])
        
        vote = Vote.objects.create(badsong=badsong,worsesong=worsesong)
        
        left_song = Song.objects.order_by('?')[0]
        right_song = Song.objects.exclude(pk=left_song.pk).order_by('?')[0]
        
        response = {}
        response['left'] = {
                                'url' : left_song.url,
                                'short_id' : left_song.short_id,
                                'name' : left_song.name,
                                'user_handle' : left_song.user_handle
                            }
        response['right'] = {
                                'url' : right_song.url,
                                'short_id' : right_song.short_id,
                                'name' : right_song.name,
                                'user_handle' : right_song.user_handle
                            }       
        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='application/json')
        
def rankings(request, template_name='rankings.html'):
    songs = Song.objects.annotate(worsecount=Count('worsevotes'), badcount=Count('badvotes')).exclude(worsecount=0).order_by('-worsecount','badcount')[:10]
    return render_to_response(template_name, {'songs':songs}, context_instance=RequestContext(request))
    