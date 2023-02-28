from .base import *

DEBUG = True
SECRET_KEY = 'x3o0qcp0w^nh04ulck1$#d4&1#7+q%^9e&hq9g42pm+u7foe*p'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kartonpmv',
        'USER': 'kartonpmv',
        'PASSWORD': 'kartonpmv',
        'HOST': 'localhost',
        'PORT': '3306',
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ADMINS = []
