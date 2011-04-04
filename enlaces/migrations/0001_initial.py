# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Cooperante'
        db.create_table('enlaces_cooperante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('logo', self.gf('addac.enlaces.thumbs.ImageWithThumbsField')(max_length=100)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('enlaces', ['Cooperante'])

        # Adding model 'SitioAmigo'
        db.create_table('enlaces_sitioamigo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('enlaces', ['SitioAmigo'])


    def backwards(self, orm):
        
        # Deleting model 'Cooperante'
        db.delete_table('enlaces_cooperante')

        # Deleting model 'SitioAmigo'
        db.delete_table('enlaces_sitioamigo')


    models = {
        'enlaces.cooperante': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cooperante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('addac.enlaces.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'enlaces.sitioamigo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'SitioAmigo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['enlaces']
