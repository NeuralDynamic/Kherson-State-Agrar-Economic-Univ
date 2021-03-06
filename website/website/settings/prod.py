from dotenv import load_dotenv

from .django import *
from .project import *
from .third_party import *

load_dotenv()

SECRET_KEY = 'Au+Sr,t>U]<8\Zn8Z3X!uTq<Q#4<sQS^Ezda5DhkV}C)&Nu{Sjy@Hq#y`nM2'

DEBUG = False

ALLOWED_HOSTS = ['ksau.neuraldynamics.online','www.ksau.neuraldynamics.online',
                '212.111.209.71','ksaeu.kherson.ua','www.ksaeu.kherson.ua']

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}


# MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware'] + \
#              MIDDLEWARE + \
#              ['django.middleware.cache.FetchFromCacheMiddleware']

print(">>> START PROJECT WITH PROD SETTINGS <<<")