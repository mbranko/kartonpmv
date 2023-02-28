from .base import *
from .utils import read_or_get

DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = read_or_get('/private/secrets', 'SECRET_KEY', '123456789012345678901234567890123456789')
DB_HOST = read_or_get('/private/secrets', 'DB_HOST', 'kartonpmv-mariadb')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kartonpmv',
        'USER': 'kartonpmv',
        'PASSWORD': 'kartonpmv',
        'HOST': DB_HOST,
        'PORT': '',
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = read_or_get('/private/secrets', 'EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = eval(read_or_get('/private/secrets', 'EMAIL_PORT', '587')) or 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = read_or_get('/private/secrets', 'EMAIL_HOST_USER', 'pmvkarton@gmail.com')
EMAIL_HOST_PASSWORD = read_or_get('/private/secrets', 'EMAIL_HOST_PASSWORD', '**********')
CSRF_TRUSTED_ORIGINS = ['https://*.pmv.org.rs']
ADMINS = [('Branko Milosavljevic', 'mbranko@uns.ac.rs')]
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
