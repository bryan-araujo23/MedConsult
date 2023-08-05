from .settings import *
DEBUG = False

SECRET_KEY = 's+3(^Ca*0@+aww=v4tlr*!hqr@*q0gibs*o-z1-+&615ob)k^F'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medicSearchAdmin',
        'USER': 'postgres',
        'PASSWORD': 123, 
        'HOST': 'localhost',
        'PORT': 5432
    }
}
