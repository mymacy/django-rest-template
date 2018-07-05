import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
##################################################################
# Django 2.0.5.
# mymacy Template
##################################################################
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # APPNAME
    'XXXXXXXXXXX',
    # API
    'api',

    # Vendor
    'rest_framework',
    'rest_framework.authtoken',
    'templated_mail',
    'djoser',
    'social_django',
]

##################################################################
# change the following for DEPLOYMENT:
##################################################################
CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True
STATIC_ROOT="/var/www/XXXXXXXXXXX/static/"
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = ["*"]
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql',                  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': os.environ['DEFAULT_DB'],                               # Or path to database file if using sqlite3.
        # 'USER': os.environ['USER_DB'],
        # 'PASSWORD': os.environ['PASSWORD_DB'],
        # 'HOST': 'localhost',                                   # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        # 'PORT': '',                                            # Set to empty string for default.
    # }
}
##################################################################
# LOGGING / also log with manual server run
##################################################################
from logger import LOGGING
##################################################################
# REST-auth
##################################################################
AUTH_USER_MODEL = 'api.CustomUser' # sets the custom user

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# # REAL MAIL
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'XXXXXXXX'
# EMAIL_HOST_PASSWORD = 'XXXXXXX'

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'djoser.social.backends.facebook.FacebookOAuth2Override',
#     'social_core.backends.google.GoogleOAuth2',
#     'social_core.backends.steam.SteamOpenId',
# ]

DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': False,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'api/activate/{uid}/{token}',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://test.localhost/'],
    # 'EMAIL': {
    #     'activation': 'api.templates.email.ActivationEmail',
    #     'confirmation': 'api.email.ConfirmationEmail',
    #     'password_reset': 'api.email.PasswordResetEmail',
    # }
}

# JWT_AUTH = {
#     'JWT_ALLOW_REFRESH': True,
# }

##################################################################
# SOCIAL AUTH
##################################################################
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET', '')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
SOCIAL_AUTH_STEAM_API_KEY = os.environ.get('STEAM_API_KEY', '')
SOCIAL_AUTH_OPENID_TRUST_ROOT = 'http://test.localhost/'
##################################################################
# OTHER
##################################################################
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

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
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
