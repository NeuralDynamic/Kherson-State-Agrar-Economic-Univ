from dotenv import load_dotenv

from .django import *
from .project import *
from .third_party import *

load_dotenv()

SECRET_KEY = 'rt^p8v+8e*gyo4!)qx&4gkb^n5o1w6fc-$bvko9-=5slu225bv'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['DATABASE_HOST'],
        'NAME': os.environ['DATABASE_NAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'PORT': os.environ['DATABASE_PORT'],
        'USER': os.environ['DATABASE_USER'],
    }
}

print(">>> START PROJECT WITH LOCAL SETTINGS <<<")