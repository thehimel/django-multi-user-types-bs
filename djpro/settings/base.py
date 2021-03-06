"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from decouple import config
from pathlib import Path
from manage import PROJECT_NAME

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Customized the BASE_DIR as changed settings.py to settings directory.
# By this we are selecting src as BASE_DIR.
# Present file name is base.py. Parent of base.py is settings.
# settings -> parent -> <directory> -> parent -> src.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIR = BASE_DIR / 'templates'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Fetching SECRET_KEY with decouple
SECRET_KEY = config('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # For allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'core',
    'users',

    'crispy_forms',

    # For django-cleanup. Must be on the bottom of INSTALLED_APPS
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    # Part of base
    'django.middleware.security.SecurityMiddleware',

    # From WhiteNoise to serve static files in Heroku from Django
    # Remove this if you are using S3
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Part of base
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = f'{PROJECT_NAME}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # noqa: E501
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1


# Custom allauth settings

ACCOUNT_ADAPTER = f'{PROJECT_NAME}.adapter.UsernameMaxAdapter'

# Use username or email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_EMAIL_REQUIRED = True

# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
LOGIN_REDIRECT_URL = 'core:dashboard'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# LOGIN_URL = '/'

EMAIL_USE_TLS = True  # This must be True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASS')

# Default sender is mandatory
DEFAULT_FROM_EMAIL = "MultiUser <info@domain.com>"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static_files']
STATIC_ROOT = BASE_DIR / 'static'

# Media files (Uploaded by the users)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# We have custom user model. Thus we need to add this.
AUTH_USER_MODEL = "users.User"

# Boostrap version in crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
