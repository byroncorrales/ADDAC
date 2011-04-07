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
from addac.treemenus.models import MenuItem

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

def pagina(request,slug):
    '''Muestra el detalle de la pagina'''
    mp = request.GET.get('m','')
    pagina_detalle = get_object_or_404(Pagina, slug=slug)
    try:
        menu1 = get_object_or_404(MenuItem, id=mp)
    except:
        menu1 =""
        pass
    dicc = {'pagina_detalle': pagina_detalle,
            'menu1':menu1,
                       }
    return direct_to_template(request, 'paginas/pagina_detalle.html',dicc)

def busqueda(request):
    q = request.GET.get('q', '')
    return direct_to_template(request, 'busqueda.html', {'q': q})