# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Publicacion'
        db.create_table('publicaciones_publicacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('imagen', self.gf('addac.publicaciones.thumbs.ImageWithThumbsField')(max_length=100)),
            ('publicacion', self.gf('addac.publicaciones.customfilefield.ContentTypeRestrictedFileField')(max_length=100)),
            ('cidoc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('addac.tagging_autocomplete.models.TagAutocompleteField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('publicaciones', ['Publicacion'])


    def backwards(self, orm):
        
        # Deleting model 'Publicacion'
        db.delete_table('publicaciones_publicacion')


    models = {
        'publicaciones.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'cidoc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('addac.publicaciones.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'publicacion': ('addac.publicaciones.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'tags': ('addac.tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['publicaciones']
