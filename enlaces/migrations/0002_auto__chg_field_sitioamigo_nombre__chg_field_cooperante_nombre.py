# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'SitioAmigo.nombre'
        db.alter_column('enlaces_sitioamigo', 'nombre', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=200))

        # Changing field 'Cooperante.nombre'
        db.alter_column('enlaces_cooperante', 'nombre', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=200))


    def backwards(self, orm):
        
        # Changing field 'SitioAmigo.nombre'
        db.alter_column('enlaces_sitioamigo', 'nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, null=True))

        # Changing field 'Cooperante.nombre'
        db.alter_column('enlaces_cooperante', 'nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, null=True))


    models = {
        'enlaces.cooperante': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cooperante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('addac.enlaces.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'enlaces.sitioamigo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'SitioAmigo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['enlaces']
