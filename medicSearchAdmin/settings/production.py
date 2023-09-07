from .settings import *

DEBUG = True

SECRET_KEY = 's+3(^Ca*0@+aww=v4tlr*!hqr@*q0gibs*o-z1-+&615ob)k^F'

ALLOWED_HOSTS = ['https://med-consult-63b45cb0f41f.herokuapp.com/'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
