from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-agdbrmp29s_^z&-26niv4lnc7l_yg@%7nwrg1ntou19r0j$c-h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}