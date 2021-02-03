from dotenv import load_dotenv

from .django import *
from .project import *
from .third_party import *

load_dotenv()

SECRET_KEY = 'Au+Sr,t>U]<8\Zn8Z3X!uTq<Q#4<sQS^Ezda5DhkV}C)&Nu{Sjy@Hq#y`nM2'

DEBUG = False

ALLOWED_HOSTS = ['ksau.neuraldynamics.online','212.111.209.71']

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

print(">>> START PROJECT WITH PROD SETTINGS <<<")