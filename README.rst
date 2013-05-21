simplekeyvalue
========================

django-simplekeyvalue is a simple key value store for django inspired by https://github.com/sligodave/django-keyvalue.

This is a little simpler than django-keyvalue as the value of the keyvalue pair is always an integer.

It also allows for locking (select_for_update) when updating the values.

Each entry will have an owner (and optional co owner) which is an instance of an existing model, a key which is a string and a value which is an integer.

Install
------------------------------------
add simplekeyvalue to INSTALLED_APPS and either run 'python manage.py syncdb' or 'python manage.py migrate simplekeyvalue' if you also have the south app installed.

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py
