from readthedocs.settings.dev import *

import os
environ = os.environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ['DB_ENV_DB_NAME'],
        'USER': environ['DB_ENV_DB_USER'],
        'PASSWORD': environ['DB_ENV_DB_PASS'],
        'HOST': 'db',
        'PORT': 5432,
    }
}
SITE_ROOT = '/app'
ES_HOSTS = ['elasticsearch:9200']
REDIS = {
    'host': 'redis',
    'port': 6379,
    'db': 0,
}
BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
DEBUG = True
CELERY_ALWAYS_EAGER = False
ALLOW_PRIVATE_REPOS = True
USE_SUBDOMAIN = True
SLUMBER_API_HOST = 'http://docs.na-kd.com'
PRODUCTION_DOMAIN = 'docs.na-kd.com'

