from django.contrib.syndication.views import Feed
from models import Noticia
from addac.tagging.models import Tag, TaggedItem
#from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

class NoticiasFeed(Feed):
    title = "Noticias de ADDAC"
    link = "/rss"
    description = 'Noticias mas recientes de ADDAC'

    def items(self):
        return Noticia.objects.order_by('-fecha')[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.contenido

    def item_author_name(self, item):
        return item.autor

    def item_link(self, item):
        return item.get_full_url()
