 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from addac.tagging.fields import TagField
from addac.tagging.models import Tag
from thumbs import ImageWithThumbsField
from addac.tagging_autocomplete.models import TagAutocompleteField
from customfilefield import ContentTypeRestrictedFileField
from addac.utils import *

# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules ([], ["^addac\.tagging_autocomplete\.models\.TagAutocompleteField"])

PUBLICACION_CHOICES = (
    (1, 'Boletines'),
    (2, 'Revistas'),
    (3, 'Nuestras Experiencias'),
    (4, 'Libros'),
    (5, 'Historias de Exito')
)

ORGANIZAR_CHOICES = (
    (1, 'Adquisiciones CEDOC'),
    (2, 'Publicaciones ADDAC'),
)

class Publicacion(models.Model):
    '''Modelo que representa el tipo de contenido para las publicaciones del sitio'''
    titulo = models.CharField('Título', max_length = 200, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 200, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField('Fecha',blank = False, null = False)
    tipo = models.IntegerField('tipo',choices=PUBLICACION_CHOICES)
    imagen = ImageWithThumbsField('Imagen portada',upload_to=get_image_path, sizes=((156,192),(90,110)), help_text="Imágen de portada, Resolución 250 x 305")
    publicacion = ContentTypeRestrictedFileField(upload_to = get_file_path, content_types=['application/pdf', 'application/zip','application/vnd.ms-powerpoint','application/vnd.ms-excel','application/msword','application/vnd.oasis.opendocument.text','application/vnd.oasis.opendocument.spreadsheet','application/vnd.oasis.opendocument.presentation'],max_upload_size=12582912, help_text='Solo se permiten archivos .doc .xls .ppt .docx .xlsx .pptx .pdf .zip .odp .odt .ods , tamaño máximo 12MB',blank = True, null = True)
    cidoc = models.IntegerField('Organizar en', choices=ORGANIZAR_CHOICES, help_text="Seleccionar si pertenece a CEDOC o a ADDAC")
    descripcion = models.TextField('Descripción',blank = True, null = True)
    tags =  TagAutocompleteField(help_text='Separar elementos con "," ')

    imgDir = 'attachments/imagenes'
    fileDir = 'attachments/documentos'

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, self.id)

    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.publicacion)

    def get_full_url(self):
        return '/publicaciones/%s/' % self.slug

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def save(self, force_insert=False, force_update=False):
        try:
            Publicacion.objects.get(pk=self.id)
        except:
            n = Publicacion.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Publicacion, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    #metodo url del objeto
    #def get_full_url(self):
    #    return "/boletines/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo

    def ext(self):
        '''Devuelve la extension del archivo'''
        cadena = len(str(self.publicacion))
        ext = str(self.publicacion)[cadena-3:cadena]
        return ext
