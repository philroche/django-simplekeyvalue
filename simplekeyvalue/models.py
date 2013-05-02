from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .managers import KeyValueManager
# Create your models here.

class KeyValue(models.Model):
    """

    """
    class Meta:
        unique_together = (("owner_content_type","owner_object_id", "key"),)
        index_together = [
            ["owner_content_type","owner_object_id", "key"],
        ]

    objects = KeyValueManager()

    # Model instance that is the owner of this key value
    owner_content_type = models.ForeignKey(ContentType,
                                           related_name="keyvalue_owners")

    owner_object_id = models.PositiveIntegerField()

    owner_content_object = generic.GenericForeignKey('owner_content_type',
                                                     'owner_object_id')

    key = models.CharField(max_length=50,help_text="Key the KeyValue")

    value = models.IntegerField()

    @property
    def owner(self):
        return self.owner_content_object

    def __unicode__(self):
        if not self.description:
            return self.name
        return u'%s - %s' % (self.name, self.description)

