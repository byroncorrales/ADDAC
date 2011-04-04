from django.contrib import admin
from addac.banners.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    list_per_page = 12

admin.site.register(Banner, BannerAdmin)

