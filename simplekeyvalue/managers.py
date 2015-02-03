from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class KeyValueManager(models.Manager):


    def has_keyvalue(self, owner=None, key=None, co_owner=None):
        """
        Test if a given owner has an instance of
        keyvalue for all the names provided
        """
        if owner and key:
            qs = self.get_queryset()
            owner_content_type_id = ContentType.objects.get_for_model(owner).id
            owner_id = owner.id
            filter_args = {'owner_content_type_id': owner_content_type_id,
                           'owner_object_id': owner_id,
                           'co_owner_content_type_id': None,
                           'co_owner_object_id': None,
                           'key': key }

            if co_owner:
                co_owner_content_type_id =ContentType.objects.get_for_model(co_owner).id
                co_owner_id = co_owner.id
                filter_args['co_owner_content_type_id'] = co_owner_content_type_id
                filter_args['co_owner_object_id'] = co_owner_id

            return qs.filter(**filter_args).exists()
        else:
            return False

    def get_keyvalue(self, owner=None, key=None, co_owner=None, select_for_update=True):

        """
        Get keyvalue instances for a given owner
        and filter with an optional names
        """
        if owner and key:
            owner_content_type_id = ContentType.objects.get_for_model(owner).id
            owner_id = owner.id
            filter_args = {'owner_content_type_id': owner_content_type_id,
                           'owner_object_id': owner_id,
                           'co_owner_content_type_id': None,
                           'co_owner_object_id': None,
                           'key': key }
            if co_owner:
                co_owner_content_type_id =ContentType.objects.get_for_model(co_owner).id
                co_owner_id = co_owner.id
                filter_args['co_owner_content_type_id'] = co_owner_content_type_id
                filter_args['co_owner_object_id'] = co_owner_id

            qs=self.get_queryset()
            if select_for_update:
                qs = qs.select_for_update()

            return qs.get(**filter_args)
        else:
            return self.get_queryset().none()


    def set_keyvalue(self, owner=None, key=None, value=None, co_owner=None):

        if owner and key:
            owner_content_type_id = ContentType.objects.get_for_model(owner).id
            owner_id = owner.id
            kwargs = {
                'key': key,
                'owner_content_type_id': owner_content_type_id,
                'owner_object_id': owner_id,
                'co_owner_content_type_id': None,
                'co_owner_object_id': None
            }
            if co_owner:
                co_owner_content_type_id =ContentType.objects.get_for_model(co_owner).id
                co_owner_id = co_owner.id
                kwargs['co_owner_content_type_id'] = co_owner_content_type_id
                kwargs['co_owner_object_id'] = co_owner_id
            kv = self.get_or_create(**kwargs)[0]
            kv.value = value
            kv.save()
            return kv
        else:
            return self.get_queryset().none()

    def del_keyvalue(self, owner=None, key=None, co_owner=None):
        """
        Delete a list of keyvalue instances for a given user.
        """
        owner_content_type_id = ContentType.objects.get_for_model(owner).id
        owner_id = owner.id
        filter_args = {'owner_content_type_id': owner_content_type_id,
                           'owner_object_id': owner_id,
                           'co_owner_content_type_id': None,
                           'co_owner_object_id': None,
                           'key': key }
        if co_owner:
            co_owner_content_type_id =ContentType.objects.get_for_model(co_owner).id
            co_owner_id = co_owner.id
            filter_args['co_owner_content_type_id'] = co_owner_content_type_id
            filter_args['co_owner_object_id'] = co_owner_id

        return self.get_queryset().filter(**filter_args).delete()
