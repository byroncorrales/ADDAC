from addac.publicaciones.models import Publicacion
from django.contrib import admin
from django.contrib.contenttypes import generic
#from amunse.boletines.actions import *
#admin.site.disable_action('delete_selected')


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','tipo']
    list_filter = ['fecha','tipo','cidoc']
    search_fields = ['titulo']
    save_on_top = False
    date_hierarchy = 'fecha'
    list_per_page = 12
    radio_fields = {"tipo": admin.HORIZONTAL}
    #actions = ['delete_selected']

    #def delete_selected(self, request, queryset):
    #    print queryset
    #    for obj in queryset:
    #        obj.delete()

    #delete_selected.short_description = "Eliminar los boletines seleccionados"

admin.site.register(Publicacion, PublicacionAdmin)
