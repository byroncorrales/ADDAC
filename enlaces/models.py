    # -*- coding: UTF-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from addac.utils import get_image_path

class Cooperante(models.Model):
    '''Modelo que representa los enlaces a cooperantes'''
    nombre = models.CharField('Nombre Cooperante', max_length=200, unique=True)
    logo = ImageWithThumbsField(upload_to=get_image_path, sizes=((250, 250), (180, 180)),help_text="Resolución 400x400")
    web = models.URLField('Sitio Web' ,help_text=" Debe cumplir con el formato 'http://www.dominio.com'",blank=True, null=True)
    pais = models.CharField('Pais', max_length=200)
    imgDir = 'attachments/cooperantes'

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cooperante"
        verbose_name_plural = "Cooperantes"
        ordering = ['nombre']

class SitioAmigo(models.Model):
    '''Modelo que representa los enlaces a sitios amigos'''
    nombre = models.CharField('Nombre Sitio Amigo', max_length=200, unique=True)
    web = models.URLField('Sitio Web' ,help_text=" Debe cumplir con el formato 'http://www.dominio.com'")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sitio Amigo"
        verbose_name_plural = "Sitios Amigos"
        ordering = ['nombre']
