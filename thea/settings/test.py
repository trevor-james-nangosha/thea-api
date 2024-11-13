import os
from .prod import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'test_db.sqlite3',
    #     'TEST': {
    #         'NAME': 'test_db.sqlite3',
    #     },
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG = True
