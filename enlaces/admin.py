from django.contrib import admin
from addac.enlaces.models import Cooperante, SitioAmigo

class CooperanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'web']
    search_fields = ['nombre']
    list_per_page = 12

class SitioAmigoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'web']
    search_fields = ['nombre']
    list_per_page = 12


admin.site.register(Cooperante, CooperanteAdmin)
admin.site.register(SitioAmigo, SitioAmigoAdmin)
