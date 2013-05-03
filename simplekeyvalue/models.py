from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .managers import KeyValueManager
# Create your models here.

class KeyValue(models.Model):
    """

    """
    class Meta:
        unique_together = (("owner_content_type","owner_object_id","co_owner_content_type","co_owner_object_id", "key"),)
        #only works in django 1.5+
        #index_together = [
        #    ["owner_content_type","owner_object_id", "key"],
        #]

    objects = KeyValueManager()

    # Model instance that is the owner of this key value
    owner_content_type = models.ForeignKey(ContentType,
                                           related_name="keyvalue_owners", db_index=True)

    owner_object_id = models.PositiveIntegerField(db_index=True)

    owner_content_object = generic.GenericForeignKey('owner_content_type',
                                                     'owner_object_id')

    co_owner_content_type = models.ForeignKey(ContentType,
                                           related_name="keyvalue_coowners", db_index=True, null=True, blank=True)

    co_owner_object_id = models.PositiveIntegerField(db_index=True, null=True, blank=True)

    co_owner_content_object = generic.GenericForeignKey('co_owner_content_type',
                                                     'co_owner_object_id')

    key = models.CharField(max_length=50,help_text="Key the KeyValue", db_index=True)

    value = models.IntegerField(null=True, blank=True)

    @property
    def owner(self):
        return self.owner_content_object

    @property
    def cp_owner(self):
        return self.co_owner_content_object

    def __unicode__(self):
        return u'%d - %s' % (self.id, self.key)

