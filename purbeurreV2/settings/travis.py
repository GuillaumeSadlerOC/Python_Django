"""
Django settings for purbeurreV2 project > Travis.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from purbeurreV2.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i2d#l63_88kv)(ic52shwa9!lzdf@fso3*1d#^#pa^eif_k%v5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}