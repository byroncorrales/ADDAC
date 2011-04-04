    # -*- coding: UTF-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from addac.utils import get_image_path

class Banner(models.Model):
    '''Modelo que representa el banner de portada'''
    titulo = models.CharField('Titulo', max_length=200, unique=True)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((540,275),))
    miniatura = ImageWithThumbsField(upload_to=get_image_path, sizes=((69,51),))
    url = models.URLField('Url Destino' ,help_text=" Debe cumplir con el formato 'http://www.dominio.com'")
    imgDir = 'attachments/banner'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Banner Portada"
        verbose_name_plural = "Banners Portada"
        ordering = ['titulo']
