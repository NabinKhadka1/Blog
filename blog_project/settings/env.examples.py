
from .base import *

SECRET_KEY = 'Your Secret Key here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    ALLOWED_HOSTS=['*']
else:
    ALLOWED_HOSTS=[]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}