from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('videos.views',
                      #(r'^popup/(?P<id>\d+)/$', 'video_popup'),
                      (r'^videos/(?P<slug>[-\w]+)/$', 'video_detalle'),
                      (r'^videos/$', 'index'),
)
