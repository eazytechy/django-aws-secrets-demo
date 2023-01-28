"""
Django settings for demo project.

"""
from pathlib import Path
from django_secrets import SECRETS
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


AWS_SECRETS_MANAGER_ACCESS_KEY_ID       = env('AWS_SECRETS_MANAGER_ACCESS_KEY_ID')
AWS_SECRETS_MANAGER_SECRET_ACCESS_KEY   = env('AWS_SECRETS_MANAGER_SECRET_ACCESS_KEY')
AWS_SECRETS_MANAGER_SECRETS_NAME        = env('AWS_SECRETS_MANAGER_SECRETS_NAME')
AWS_SECRETS_MANAGER_REGION_NAME         = env('AWS_SECRETS_MANAGER_REGION_NAME')

SECRET_KEY  = SECRETS.get('SECRET_KEY')
DEBUG       = SECRETS.get('DEBUG')

# You can uncomment next line and see if your project is able to fetch and read from AWS Secrets Manager
# print("Secret Key: %s" % SECRET_KEY)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'demo.urls'

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

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE'        : 'django.db.backends.mysql',
        'NAME'          : SECRETS.get('DB_NAME'),
        'USER'          : SECRETS.get('DB_USER'),
        'PASSWORD'      : SECRETS.get('DB_PASSWORD'),
        "HOST"          : SECRETS.get('DB_HOST'),
        'TIME_ZONE'     : 'Asia/Kolkata'
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
