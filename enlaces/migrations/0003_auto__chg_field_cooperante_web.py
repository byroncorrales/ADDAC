# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Cooperante.web'
        db.alter_column('enlaces_cooperante', 'web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))


    def backwards(self, orm):
        
        # Changing field 'Cooperante.web'
        db.alter_column('enlaces_cooperante', 'web', self.gf('django.db.models.fields.URLField')(default='', max_length=200))


    models = {
        'enlaces.cooperante': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cooperante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('addac.enlaces.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
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
