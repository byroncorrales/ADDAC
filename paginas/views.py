# -*- coding: UTF-8 -*-
from django.core.exceptions import ViewDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.template.defaultfilters import slugify
from django.views.generic.simple import direct_to_template
from addac.noticias.models import Noticia
from addac.paginas.models import Pagina
from addac.banners.models import Banner
from addac.publicaciones.models import Publicacion
from tagging.models import *

def inicio(request):
    noticia = Noticia.objects.filter(tipo = 1).order_by('-fecha', '-id')[:4]
    noticia_inov = Noticia.objects.filter(tipo = 2).order_by('-fecha', '-id')[:1]
    banner = Banner.objects.all()
    publicacion = Publicacion.objects.filter(cidoc = True).order_by('-fecha', '-id')[:9]
    dicc = {
        'noticia':noticia,
        'noticia_inov':noticia_inov,
        'banner':banner,
        'publicacion':publicacion,
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
