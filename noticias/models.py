    # -*- coding: UTF-8 -*-
from addac.extras.models import Adjunto
from django.contrib.contenttypes import generic
from django.db import models
from django.template.defaultfilters import slugify
from south.modelsinspector import add_introspection_rules
from addac.tagging.models import Tag
from addac.tagging_autocomplete.models import TagAutocompleteField
from thumbs import ImageWithThumbsField
from addac.utils import get_image_path
add_introspection_rules ([], ["^addac\.tagging_autocomplete\.models\.TagAutocompleteField"])
from django.contrib.comments.moderation import CommentModerator, moderator,AlreadyModerated
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted
from addac.noticias.signals import comment_notifier
comment_was_posted.connect(comment_notifier, sender=Comment)
class CategoriaNoticia(models.Model):
    '''Modelo que representa la categorias de las noticias'''
    nombre = models.CharField('Título', max_length=40, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, help_text='unico Valor', editable=False)

    def __unicode__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(CategoriaNoticia, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Categoria de Noticia"
        verbose_name_plural = "Categorias de Noticias"

NOTICIA_CHOICES = (
    (1, 'General'),
    (2, 'Innovacion Tecnologica'),
)

class Noticia(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length=120, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=120, unique=True, help_text='unico Valor', editable=False)
    fecha = models.DateField()
    autor = models.CharField('Autor', max_length=100, blank=True, null=True)
    tipo = models.IntegerField('tipo',choices=NOTICIA_CHOICES)
    categoria = models.ForeignKey(CategoriaNoticia)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((62, 48), (206, 138), (265, 200)),help_text="Resolución 640x480")
    contenido = models.TextField('Contenido', blank=True, null=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')
    adjunto = generic.GenericRelation(Adjunto)
    #habilita_comentario = models.BooleanField(default=True)

    imgDir = 'attachments/imagenes'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

    def save(self, force_insert=False, force_update=False):
        try:
            Noticia.objects.get(pk=self.id)
        except:
            n = Noticia.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Noticia, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    #metodo para devolver la url exacta del objeto
    def get_full_url(self):
        return "/noticias/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo

#    def categorias(self):
#        return self.Noticia.all()[0].categoria.nombre


from django.db.models import signals
class NoticiaModerador(CommentModerator):
    email_notification = True
    auto_moderate_field = 'fecha'
    moderate_after = 15

signals.post_save.connect(comment_notifier, sender=Comment)


try:
    moderator.register(Noticia, NoticiaModerador)
except AlreadyModerated:
    pass


