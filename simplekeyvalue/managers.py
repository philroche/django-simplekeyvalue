from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class KeyValueManager(models.Manager):


    def has_keyvalue(self, owner, key):
        """
        Test if a given owner has an instance of
        keyvalue for all the names provided
        """
        qs = self.get_query_set()
        owner_type = ContentType.objects.get_for_model(owner)
        return qs.filter(owner_content_type=owner_type,
                                       owner_object_id=owner.id,
                                       key=key).exists()

    def get_keyvalue(self, owner, key=None, select_for_update=True):
        """
        Get keyvalue instances for a given owner
        and filter with an optional names
        """

        filter_args = {'owner_content_type': ContentType.objects.get_for_model(owner),
                       'owner_object_id': owner.id,
                       'key': key}

        qs=self.get_query_set().get(**filter_args)
        if select_for_update:
            qs = qs.select_for_update()

        return qs


    def set_keyvalue(self, owner, key, value):


        kwargs = {
            'key': key,
            'owner_content_type': ContentType.objects.get_for_model(owner),
            'owner_object_id': owner.id,
            'value': value
        }

        return self.get_or_create(**kwargs)[0]

    def del_keyvalue(self, owner, key):
        """
        Delete a list of keyvalue instances for a given user.
        """
        owner_type = ContentType.objects.get_for_model(owner)
        qs = self.get_query_set()
        qs.filter(owner_content_type=owner_type,
                  owner_object_id=owner.id,
                  key=key).delete()
