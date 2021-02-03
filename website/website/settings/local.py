from dotenv import load_dotenv

from .django import *
from .project import *
from .third_party import *

load_dotenv()

SECRET_KEY = 'rt^p8v+8e*gyo4!)qx&4gkb^n5o1w6fc-$bvko9-=5slu225bv'

DEBUG = True

ALLOWED_HOSTS = ['ksau.neuraldynamics.online','localhost',
                 '127.0.0.1','212.111.209.71']

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

print(">>> START PROJECT WITH LOCAL SETTINGS <<<")