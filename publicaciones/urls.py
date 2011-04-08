from django.conf.urls.defaults import *
from django.conf import settings
from models import Publicacion

urlpatterns = patterns('publicaciones.views',
    (r'^publicaciones/$', 'publicacion_lista'),
    #(r'^boletines/(?P<slug>[-\w]+)/$', 'boletin_detalle'),
)
