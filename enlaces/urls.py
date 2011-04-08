from django.conf.urls.defaults import *
from django.conf import settings
from models import Cooperante, SitioAmigo

urlpatterns = patterns('enlaces.views',
    (r'^enlacescooperante/$', 'cooperante_lista'),
    (r'^enlacesamigos/$', 'amigo_lista'),
)
