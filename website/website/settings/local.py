from .django import *
from .project import *
from .third_party import *

SECRET_KEY = 'rt^p8v+8e*gyo4!)qx&4gkb^n5o1w6fc-$bvko9-=5slu225bv'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

print(">>> START PROJECT WITH LOCAL SETTINGS <<<")