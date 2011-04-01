# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pagina'
        db.create_table('paginas_pagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('paginas', ['Pagina'])

        # Adding model 'PaginaImagen'
        db.create_table('paginas_paginaimagen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('imagen', self.gf('addac.paginas.thumbs.ImageWithThumbsField')(max_length=100)),
            ('pagina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paginas.Pagina'])),
        ))
        db.send_create_signal('paginas', ['PaginaImagen'])


    def backwards(self, orm):
        
        # Deleting model 'Pagina'
        db.delete_table('paginas_pagina')

        # Deleting model 'PaginaImagen'
        db.delete_table('paginas_paginaimagen')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'extras.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('addac.extras.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'paginas.paginaimagen': {
            'Meta': {'object_name': 'PaginaImagen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('addac.paginas.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paginas.Pagina']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['paginas']
