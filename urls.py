from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
from os import path as os_path

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addac.views.home', name='home'),
    # url(r'^addac/', include('addac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', 'addac.extras.views.subir_imagen'),
    url(r'^admin/settings/$', include('livesettings.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )