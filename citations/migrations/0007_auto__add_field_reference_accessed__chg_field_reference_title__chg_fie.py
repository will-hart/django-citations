# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reference.accessed'
        db.add_column(u'citations_reference', 'accessed',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 20, 0, 0)),
                      keep_default=False)


        # Changing field 'Reference.title'
        db.alter_column(u'citations_reference', 'title', self.gf('django.db.models.fields.CharField')(default='New reference', max_length=512))

        # Changing field 'Reference.year'
        db.alter_column(u'citations_reference', 'year', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):
        # Deleting field 'Reference.accessed'
        db.delete_column(u'citations_reference', 'accessed')


        # Changing field 'Reference.title'
        db.alter_column(u'citations_reference', 'title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'Reference.year'
        db.alter_column(u'citations_reference', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'citations.reference': {
            'Meta': {'object_name': 'Reference'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'accessed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 12, 20, 0, 0)'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'edition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'BK'", 'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2000'})
        }
    }

    complete_apps = ['citations']