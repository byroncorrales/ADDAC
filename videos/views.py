# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from videos.models import *


def index(request):
    '''vista de indice lista de videos paginados'''
    videos = Video.objects.all().order_by('-fecha','-id')

    return render_to_response('videos/video_lista.html', {'videos': videos},
                              context_instance = RequestContext(request))

def video_detalle(request, slug):
    '''vista detalle del video'''
    video = get_object_or_404(Video, slug=slug)
    return render_to_response('videos/video_detalle.html', {'video': video},
                              context_instance = RequestContext(request))
