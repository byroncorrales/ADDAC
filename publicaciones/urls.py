from django.conf.urls.defaults import *
from django.conf import settings
from models import Publicacion

urlpatterns = patterns('publicaciones.views',
    (r'^publicaciones/$', 'publicacion_lista'),
    (r'^publicaciones/organizar/(?P<org>[-\w]+)/$', 'publicacion_lista_org'),
    (r'^publicaciones/tipo/(?P<tipo>[-\w]+)/$', 'publicacion_lista_tipo'),
    (r'^publicaciones/(?P<slug>[-\w]+)/$', 'publicacion_detalle'),
)
