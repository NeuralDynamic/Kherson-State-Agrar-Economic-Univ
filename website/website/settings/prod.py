from .django import *
from .project import *
from .third_party import *

SECRET_KEY = 'Au+Sr,t>U]<8\Zn8Z3X!uTq<Q#4<sQS^Ezda5DhkV}C)&Nu{Sjy@Hq#y`nM2'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': os.environ['DATABASE_HOST'],
        'NAME': os.environ['DATABASE_NAME'],
        'PORT': os.environ['DATABASE_PORT'],
        'USER': os.environ['DATABASE_USER'],
    }
}


print(">>> START PROJECT WITH PROD SETTINGS <<<")