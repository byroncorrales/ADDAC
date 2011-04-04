from django.contrib import admin
from addac.videos.models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
    save_on_top = False
    date_hierarchy = 'fecha'
    list_per_page = 12

admin.site.register(Video, VideoAdmin)

