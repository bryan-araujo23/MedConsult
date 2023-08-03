import os
from .settings import *

DEBUG = True

SECRET_KEY = 's+9(^sf*0@+aww=v5tlr*!hqr^*qogibs*o-z7-+&617ob)z^n'

ALLOWED_HOSTS = ['127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
