# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Banner'
        db.create_table('banners_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('imagen', self.gf('addac.banners.thumbs.ImageWithThumbsField')(max_length=100)),
            ('miniatura', self.gf('addac.banners.thumbs.ImageWithThumbsField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('banners', ['Banner'])


    def backwards(self, orm):
        
        # Deleting model 'Banner'
        db.delete_table('banners_banner')


    models = {
        'banners.banner': {
            'Meta': {'ordering': "['titulo']", 'object_name': 'Banner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('addac.banners.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'miniatura': ('addac.banners.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['banners']
