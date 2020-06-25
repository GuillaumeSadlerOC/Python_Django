"""
Django settings for purbeurreV2 project on local development.
This file need to import common file.

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

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurrev2',
        'USER': 'purbeurreuser',
        'PASSWORD': 'purbeurrePass',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# SECURITY WARNING: keep the social secret keys used in production secret !

# https://console.developers.google.com/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "961551602475-sm7egi2h40vucgugkhhktq4ogc26o6s6.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "b4ykavMAZJRmopVtGJwaoTvF"

SOCIAL_AUTH_GITHUB_KEY = "d3d68d27c4439577397a"
SOCIAL_AUTH_GITHUB_SECRET = "3e30dfc7983867b7a563fac3404e18cf70a8d720"

SOCIAL_AUTH_FACEBOOK_KEY = "2389244584454329"
SOCIAL_AUTH_FACEBOOK_SECRET = "e6b4fda2154735f1f0e89fc19d8884e2"
