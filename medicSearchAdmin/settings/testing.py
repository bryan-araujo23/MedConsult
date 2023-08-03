import os
from .settings import *

DEBUG = True

SECRET_KEY = 's+1(^Cf*0@+aww=v4tlr*!hqr^*qogibs*o-z7-+&615ob)z^a'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
