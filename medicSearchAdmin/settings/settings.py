from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's+7(^sf*0@+aww=v5tlr*!hqr^*qogibs*o-z6-+&617ob)z^m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'medicSearch',
    'social_django'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medicSearchAdmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'medicSearchAdmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

from pathlib import Path
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# url que lida com a mídia veiuculada na pasta media_root
MEDIA_URL = '/media/'

# Caminho absoluto do sistema de arquivos, para pasta que conterá
#  todos arquivos enviados pelo usuário 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_URL = '/login'                  # define a rota padrão de login do sistema
LOGIN_REDIRECT_URL = '/'              # define para onde seremos redirecionado caso o login ocorra com sucesso
LOGOUT_URL = '/logout'                # define a rota padrão de logout do sitema
LOGOUT_REDIRECT_URL = '/login'        # define por onde seremos redirecionado caso o logout seja dfeito com sucesso


# define quais backends de autenticação serão utilizados para lidar com a autenticação social. 
AUTHENTICATION_BACKENDS = [
    # Google
    'social_core.backends.google.GoogleOAuth2', 
    # Facebook         
    'social_core.backends.facebook.FacebookOAuth2',
    # modelo padrão da nossa aplicação
    'django.contrib.auth.backends.ModelBackend',
]

# Quando criamos o login com alguma rede social, geralmente alguns dados são transitados
# entre a API dda rede social e nossa aplicação(username, email, fotos,  etc...)
# O social_django cria algumas tabelas em nossa aplicação para poder gerenciar esses dados 
# Sem interfirir na tabela de usuário(Profile) padrão

# id do aplicativo: 1043662877067985
# chave secreta do app: 84ab2aaeb7e3009bdfcf7ff46ada0220


SOCIAL_AUTH_FACEBOOK_KEY = "1043662877067985"
SOCIAL_AUTH_FACEBOOK_SECRET  = "84ab2aaeb7e3009bdfcf7ff46ada0220"

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']  # lista de permissões para acessar as propriedades de dados do nosso app

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {                # dict possuí  uma chave com os campos em que o valor é uma 
    'fields': 'id, name, email, picture.type(large), link'   # lista de attr que devem ser retornados pelo facebook.
}


# Precisamos especificar os campos para armazenar os dados
#  Adicionais que solicitamos ao banco de dados
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [  

    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),

]

# google
# ID do cliente: 71921871485-f9dsh60dqfsrni9kkjteps5fmatssji5.apps.googleusercontent.com
# Chave Secreta do cliente: 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


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '71921871485-f9dsh60dqfsrni9kkjteps5fmatssji5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# campo que diz que se será usada a criptgrafia TLS ou não
EMAIL_USE_TLS = True  
# Host do seu provedor de e-mail       
EMAIL_HOST = 'smtp.gmail.com'
# E-mail que será usado para fazer o envio dos e-mails.
EMAIL_HOSTE_USER = 'seuemail@gmail.com'
# Senha do seu e-mail
EMAIL_HOST_PASSWORD = 'sua senha'
# porta que provedor usará parafazer o envio dos e-mails
EMAIL_PORT = 587
# E-mail padrão para servir de remetente em nossos e-mails
DEFAULT_FROM_EMAIL = EMAIL_HOSTE_USER
# Campo que informa se será usada a criptografia ssl no envio.
EMAIL_USE_SSL = False

import django_heroku
django_heroku.settings(locals())


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'