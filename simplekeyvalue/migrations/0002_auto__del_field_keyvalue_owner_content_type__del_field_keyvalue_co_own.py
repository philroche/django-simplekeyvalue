# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'KeyValue', fields ['owner_content_type', 'owner_object_id', 'co_owner_content_type', 'key', 'co_owner_object_id']
        #db.delete_unique(u'simplekeyvalue_keyvalue', ['owner_content_type_id', 'owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id'])

        # Deleting field 'KeyValue.owner_content_type'
        #db.delete_column(u'simplekeyvalue_keyvalue', 'owner_content_type_id')

        # Deleting field 'KeyValue.co_owner_content_type'
        #db.delete_column(u'simplekeyvalue_keyvalue', 'co_owner_content_type_id')

        # Adding field 'KeyValue.owner_content_type_id'
        # db.add_column(u'simplekeyvalue_keyvalue', 'owner_content_type_id',
        #               self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
        #               keep_default=False)

        # Adding field 'KeyValue.co_owner_content_type_id'
        # db.add_column(u'simplekeyvalue_keyvalue', 'co_owner_content_type_id',
        #               self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True, null=True, blank=True),
        #               keep_default=False)

        # Adding unique constraint on 'KeyValue', fields ['owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id', 'owner_content_type_id']
        #db.create_unique(u'simplekeyvalue_keyvalue', ['owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id', 'owner_content_type_id'])
        pass

    def backwards(self, orm):
        # Removing unique constraint on 'KeyValue', fields ['owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id', 'owner_content_type_id']
        #db.delete_unique(u'simplekeyvalue_keyvalue', ['owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id', 'owner_content_type_id'])

        # Adding field 'KeyValue.owner_content_type'
        # db.add_column(u'simplekeyvalue_keyvalue', 'owner_content_type',
        #               self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='keyvalue_owners', to=orm['contenttypes.ContentType']),
        #               keep_default=False)

        # Adding field 'KeyValue.co_owner_content_type'
        #db.add_column(u'simplekeyvalue_keyvalue', 'co_owner_content_type',
        #               self.gf('django.db.models.fields.related.ForeignKey')(related_name='keyvalue_coowners', null=True, to=orm['contenttypes.ContentType'], blank=True),
        #               keep_default=False)

        # Deleting field 'KeyValue.owner_content_type_id'
        #db.delete_column(u'simplekeyvalue_keyvalue', 'owner_content_type_id')

        # Deleting field 'KeyValue.co_owner_content_type_id'
        #db.delete_column(u'simplekeyvalue_keyvalue', 'co_owner_content_type_id')

        # Adding unique constraint on 'KeyValue', fields ['owner_content_type', 'owner_object_id', 'co_owner_content_type', 'key', 'co_owner_object_id']
        #db.create_unique(u'simplekeyvalue_keyvalue', ['owner_content_type_id', 'owner_object_id', 'co_owner_content_type_id', 'key', 'co_owner_object_id'])
        pass

    models = {
        u'simplekeyvalue.keyvalue': {
            'Meta': {'unique_together': "(('owner_content_type_id', 'owner_object_id', 'co_owner_content_type_id', 'co_owner_object_id', 'key'),)", 'object_name': 'KeyValue'},
            'co_owner_content_type_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'co_owner_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'owner_content_type_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'owner_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['simplekeyvalue']