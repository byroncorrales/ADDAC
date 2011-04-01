from django.contrib import admin
from addac.noticias.models import Noticia, CategoriaNoticia
from django.contrib.contenttypes import generic
from addac.extras.models import Adjunto #importando el modelo de adjuntos genericos

class CategoriaNoticiaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 12

class AdjuntoInline(generic.GenericTabularInline):
    model = Adjunto
    extra = 1
    max_num = 3

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','tipo','categoria']
    list_filter = ['categoria','tipo']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12
    radio_fields = {"tipo": admin.HORIZONTAL}

    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]


admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)

