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
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# SECURITY WARNING: keep the social secret keys used in production secret !

# https://console.developers.google.com/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"
)

SOCIAL_AUTH_GITHUB_KEY = os.environ.get(
    "SOCIAL_AUTH_GITHUB_KEY"
)
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get(
    "SOCIAL_AUTH_GITHUB_SECRET"
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get(
    "SOCIAL_AUTH_FACEBOOK_KEY"
)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get(
    "SOCIAL_AUTH_FACEBOOK_SECRET"
)
