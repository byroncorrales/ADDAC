# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from publicaciones.models import *

def publicacion_detalle(request,slug):
    '''Muestra el detalle de una publicacion'''
    publicacion = get_object_or_404(Boletin, slug=slug)
    dicc = {'publicacion': publicacion,
           }
    return direct_to_template(request, 'publicaciones/publicacion_detalle.html',dicc)

def publicacion_lista(request):
    '''Vista para mostrar la lista de publicaciones'''
    publicacion_lista = Publicacion.objects.all().order_by('-fecha','-id')
    paginator = Paginator(publicacion_lista, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        publicacion = paginator.page(page)
    except (EmptyPage, InvalidPage):
        publicacion = paginator.page(paginator.num_pages)

    dicc = {'publicaciones': publicacion,
           }
    return direct_to_template(request, 'publicacion/publicaciones_lista.html',dicc)


