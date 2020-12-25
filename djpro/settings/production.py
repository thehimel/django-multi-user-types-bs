# flake8: noqa
from .base import *
import dj_database_url

# In production, make sure environment variable DEBUG=False
DEBUG = config('DEBUG', cast=bool)

# Include your hosts here
ALLOWED_HOSTS = ['multiusers.herokuapp.com']

# Redirect non-ssl requests to ssl version.
SECURE_SSL_REDIRECT = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }

# Fetch the env var with decouple
DATABASE_URL = config('DATABASE_URL')
# create db dictionary with dj_database_url from DATABASE_URL
postgres_db = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
# DATABASES = {} is declared in the base.py
DATABASES['default'] = postgres_db

# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
