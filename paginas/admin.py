from django.contrib import admin
from addac.paginas.models import Pagina, PaginaImagen
from django.contrib.contenttypes import generic
from addac.extras.models import Adjunto #importando el modelo de adjuntos genericos

class AdjuntoInline(generic.GenericTabularInline):
    model = Adjunto
    extra = 1
    max_num = 3

class ImagenInline(admin.TabularInline):
    model = PaginaImagen
    extra = 1
    max_num = 5
    template = "tabular.html"

class PaginaAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
    inlines = [ImagenInline,AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12
    fieldsets = (
        (None, {
            'fields': (('titulo', 'fecha'), 'contenido')
        }),
        #('Advanced options', {
        #    'classes': ('collapse',),
        #    'fields': (AdjuntoInline,)
        #}),
    )

    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js'
              ]

#class PaginaImagenAdmin(admin.ModelAdmin):
#    list_display = ['titulo','imagen','image_img']
#    fields = ('titulo','imagen','image_img')
#    search_fields = ['titulo']


admin.site.register(Pagina, PaginaAdmin)
#admin.site.register(PaginaImagen, PaginaImagenAdmin)
