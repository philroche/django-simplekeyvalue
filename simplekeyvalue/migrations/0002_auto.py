# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'KeyValue', fields ['owner_object_id']
        db.create_index(u'simplekeyvalue_keyvalue', ['owner_object_id'])

        # Adding index on 'KeyValue', fields ['key']
        db.create_index(u'simplekeyvalue_keyvalue', ['key'])


    def backwards(self, orm):
        # Removing index on 'KeyValue', fields ['key']
        db.delete_index(u'simplekeyvalue_keyvalue', ['key'])

        # Removing index on 'KeyValue', fields ['owner_object_id']
        db.delete_index(u'simplekeyvalue_keyvalue', ['owner_object_id'])


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simplekeyvalue.keyvalue': {
            'Meta': {'unique_together': "(('owner_content_type', 'owner_object_id', 'key'),)", 'object_name': 'KeyValue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keyvalue_owners'", 'to': u"orm['contenttypes.ContentType']"}),
            'owner_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['simplekeyvalue']