# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from addac.extras.models import Adjunto #importando el modelo de adjuntos genericos
from django.template.defaultfilters import slugify
from thumbs import ImageWithThumbsField
from addac.utils import get_image_path

class Pagina(models.Model):
    '''Modelo Gpara representar a paginas estaticas'''
    titulo = models.CharField('Título', max_length = 200, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField()
    contenido = models.TextField('Contenido',blank = True, null = True)
    adjunto = generic.GenericRelation(Adjunto)

    def __unicode__(self):
        return self.titulo

    def get_full_url(self):
        return "/paginas/%s/" % self.slug

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.titulo)
        super(Pagina, self).save(force_insert, force_update)

    def galeria(self):
        return PaginaImagen.objects.filter(pagina__id=self.id)

class PaginaImagen(models.Model):
    '''fotos para las paginas'''
    titulo = models.CharField('Título', max_length = 100,blank = False, null = False)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((100, 100), (180, 250), (640, 480)), help_text="Resolución 640x480")
    pagina = models.ForeignKey(Pagina)
    imgDir = 'attachments/imagenes/pagina'

    class Meta:
        verbose_name = "Pagina imagen"
        verbose_name_plural = "Pagina imagenes"

    def __unicode__(self):
        return str(self.image_img())

    def photo_name(self):
        return "Imagen %s" % self.pk

    def image_img(self):
        if self.imagen:
            return u'<img alt="%s" title="%s" width="80" height="52" src="%s" />' % (self.photo_name(), self.photo_name(), self.imagen.url_100x100)
        else:
            return '(Without image)'
    image_img.short_description = 'vista previa'
    image_img.allow_tags = True