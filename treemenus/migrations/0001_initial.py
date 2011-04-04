# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MenuItem'
        db.create_table('treemenus_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['treemenus.MenuItem'], null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('named_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contained_items', null=True, to=orm['treemenus.Menu'])),
        ))
        db.send_create_signal('treemenus', ['MenuItem'])

        # Adding model 'Menu'
        db.create_table('treemenus_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('root_item', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='is_root_item_of', null=True, to=orm['treemenus.MenuItem'])),
            ('levels', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('treemenus', ['Menu'])


    def backwards(self, orm):
        
        # Deleting model 'MenuItem'
        db.delete_table('treemenus_menuitem')

        # Deleting model 'Menu'
        db.delete_table('treemenus_menu')


    models = {
        'treemenus.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levels': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'root_item': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'is_root_item_of'", 'null': 'True', 'to': "orm['treemenus.MenuItem']"})
        },
        'treemenus.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contained_items'", 'null': 'True', 'to': "orm['treemenus.Menu']"}),
            'named_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['treemenus.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['treemenus']
