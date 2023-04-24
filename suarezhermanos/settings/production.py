from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['gestoriasuarezhermanos.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deb5qccl523dfh',
        'USER': 'eebslnmhjbbqeh',
        'PASSWORD': '1460198651ad496791731b5911443e7d9fae4ef6bc07b5278d59d29a36cf7238',
        'HOST': 'ec2-34-197-84-74.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

"""
losmillogestoria

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd349tjo1ar85sa',
        'USER': 'nqwynjcpaqvhil',
        'PASSWORD': 'fa82221be58715cf2c686ee4e93b27598fa570b18fcb7edf21108dc0e8d829c6',
        'HOST': 'ec2-34-230-153-41.compute-1.amazonaws.com',
        'PORT': 5432,

gestoriasuarezhermanos

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deb5qccl523dfh',
        'USER': 'eebslnmhjbbqeh',
        'PASSWORD': '1460198651ad496791731b5911443e7d9fae4ef6bc07b5278d59d29a36cf7238',
        'HOST': 'ec2-34-197-84-74.compute-1.amazonaws.com',
        'PORT': 5432,

"""



