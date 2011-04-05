# -*- coding: UTF-8 -*-
from django.core.exceptions import ViewDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.views.generic.simple import direct_to_template
from noticias.models import *
from paginas.models import *
from tagging.models import *

def inicio(request):
    noticia = Noticia.objects.filter(tipo = 1).order_by('-fecha', '-id')[:4]
    dicc = {
        'noticia':noticia,
    }
    return render_to_response('index.html',dicc,
                              context_instance=RequestContext(request))

def tags(request, id):
    tag = get_object_or_404(Tag, pk=int(id))
    objects = TaggedItem.objects.filter(tag=tag)
    return render_to_response('tags.html', RequestContext(request, locals()))

def pagina(request,slug):
    '''Muestra el detalle de la pagina'''
    pagina = get_object_or_404(Pagina, slug=slug)
    #Jala las ultimas noticias relacionadas con la misma categoria y excluye a la noticia misma
    dicc = {'pagina': pagina,
           }
    return direct_to_template(request, 'paginas/pagina_detalle.html',dicc)
