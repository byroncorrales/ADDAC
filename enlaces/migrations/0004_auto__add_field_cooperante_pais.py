# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Cooperante.pais'
        db.add_column('enlaces_cooperante', 'pais', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Cooperante.pais'
        db.delete_column('enlaces_cooperante', 'pais')


    models = {
        'enlaces.cooperante': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cooperante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('addac.enlaces.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'enlaces.sitioamigo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'SitioAmigo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['enlaces']
