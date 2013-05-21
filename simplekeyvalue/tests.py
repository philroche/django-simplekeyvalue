"""

"""

from django.test import TestCase
from .models import KeyValue
from django.contrib.auth.models import User
import string
import random

class KeyValueTest(TestCase):

    def createUserObject(self):

        username_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
        u, created = User.objects.get_or_create(username=username_password, password=username_password)
        return u

    def test_set(self):
        """

        """

        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        self.assertEqual(kv.value, 17)

    def test_get(self):
        """

        """
        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        kv  = KeyValue.objects.get_keyvalue(u, 'testkey')
        self.assertEqual(kv.value, 17)

    def test_has(self):
        """

        """
        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        has_kv  = KeyValue.objects.has_keyvalue(u, 'testkey')

        self.assertEqual(has_kv, True)

    def test_del(self):
        """

        """
        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        KeyValue.objects.del_keyvalue(u, 'testkey')
        has_kv  = KeyValue.objects.has_keyvalue(u, 'testkey')
        self.assertEqual(has_kv, False)

    def test_incremenet(self):
        """

        """
        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        kv  = KeyValue.objects.get_keyvalue(u, 'testkey')
        self.assertEqual(kv.value, 17)
        kv.increment_value(count=3)
        kv.save()
        kv  = KeyValue.objects.get_keyvalue(u, 'testkey')
        self.assertEqual(kv.value, 20)


    def test_decremenet(self):
        """

        """
        u = self.createUserObject()
        kv  = KeyValue.objects.set_keyvalue(u, 'testkey', 17)
        kv  = KeyValue.objects.get_keyvalue(u, 'testkey')
        self.assertEqual(kv.value, 17)
        kv.decrement_value(count=13)
        kv.save()
        kv  = KeyValue.objects.get_keyvalue(u, 'testkey')
        self.assertEqual(kv.value, 4)



