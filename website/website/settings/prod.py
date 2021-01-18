from .django import *
from .project import *
from .third_party import *

SECRET_KEY = 'Au+Sr,t>U]<8\Zn8Z3X!uTq<Q#4<sQS^Ezda5DhkV}C)&Nu{Sjy@Hq#y`nM2'

DEBUG = False

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

print(">>> START PROJECT WITH PROD SETTINGS <<<")