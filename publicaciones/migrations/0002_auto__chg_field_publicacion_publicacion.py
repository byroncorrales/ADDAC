# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Publicacion.publicacion'
        db.alter_column('publicaciones_publicacion', 'publicacion', self.gf('addac.publicaciones.customfilefield.ContentTypeRestrictedFileField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Publicacion.publicacion'
        db.alter_column('publicaciones_publicacion', 'publicacion', self.gf('addac.publicaciones.customfilefield.ContentTypeRestrictedFileField')(default='', max_length=100))


    models = {
        'publicaciones.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'cidoc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('addac.publicaciones.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'publicacion': ('addac.publicaciones.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'tags': ('addac.tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['publicaciones']
