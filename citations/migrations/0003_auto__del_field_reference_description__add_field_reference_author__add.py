# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reference.description'
        db.delete_column(u'citations_reference', 'description')

        # Adding field 'Reference.author'
        db.add_column(u'citations_reference', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Not supplied', max_length=512),
                      keep_default=False)

        # Adding field 'Reference.series'
        db.add_column(u'citations_reference', 'series',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Reference.volume'
        db.add_column(u'citations_reference', 'volume',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Reference.edition'
        db.add_column(u'citations_reference', 'edition',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Reference.place'
        db.add_column(u'citations_reference', 'place',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Reference.abstract'
        db.add_column(u'citations_reference', 'abstract',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Reference.title'
        db.alter_column(u'citations_reference', 'title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

    def backwards(self, orm):
        # Adding field 'Reference.description'
        db.add_column(u'citations_reference', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Reference.author'
        db.delete_column(u'citations_reference', 'author')

        # Deleting field 'Reference.series'
        db.delete_column(u'citations_reference', 'series')

        # Deleting field 'Reference.volume'
        db.delete_column(u'citations_reference', 'volume')

        # Deleting field 'Reference.edition'
        db.delete_column(u'citations_reference', 'edition')

        # Deleting field 'Reference.place'
        db.delete_column(u'citations_reference', 'place')

        # Deleting field 'Reference.abstract'
        db.delete_column(u'citations_reference', 'abstract')


        # User chose to not deal with backwards NULL issues for 'Reference.title'
        raise RuntimeError("Cannot reverse this migration. 'Reference.title' and its values cannot be restored.")

    models = {
        u'citations.reference': {
            'Meta': {'object_name': 'Reference'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'edition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['citations']