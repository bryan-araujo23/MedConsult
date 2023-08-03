import os
from .settings import *

DEBUG = False

SECRET_KEY = 's+3(^Ca*0@+aww=v4tlr*!hqr@*q0gibs*o-z1-+&615ob)k^F'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
