# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Comic'
        db.create_table('comic_comic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('comic', ['Comic'])


    def backwards(self, orm):
        
        # Deleting model 'Comic'
        db.delete_table('comic_comic')


    models = {
        'comic.comic': {
            'Meta': {'object_name': 'Comic'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['comic']
