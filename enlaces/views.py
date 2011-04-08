# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist

from addac.enlaces.models import Cooperante, SitioAmigo


def cooperante_lista(request):
    '''Vista para mostrar la lista de cooperantes'''
    enlace = Cooperante.objects.all().order_by('-nombre')

    dicc = {'enlace': enlace,
           }
    return direct_to_template(request, 'enlaces/enlace_lista.html',dicc)

def amigo_lista(request):
    '''Vista para mostrar la lista de cooperantes'''
    enlace = SitioAmigo.objects.all().order_by('-nombre')
    centinela = True
    dicc = {'enlace': enlace,'centinela':centinela,
           }
    return direct_to_template(request, 'enlaces/enlace_lista.html',dicc)