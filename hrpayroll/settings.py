"""
Django settings for hrpayroll project.
"""

import os
from pathlib import Path

# ─── BASE DIRECTORY ─────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent

# ─── SECURITY ───────────────────────────────────────────────────────────────────

# Use an env var in production; fallback to your local secret if absent
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-t+_zns-6f_*a!u0=t(#!^m&7rnmko71*eo_a@&pt#i(&nnw54('
)

# Turn DEBUG off in prod by setting DEBUG=False in env
DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1')

# Hosts/domain names that are valid for this site
if DEBUG:
    ALLOWED_HOSTS = []
else:
    _hosts = os.getenv('ALLOWED_HOSTS', '')
    ALLOWED_HOSTS = _hosts.split(',') if _hosts else []

# ─── APPLICATION DEFINITION ────────────────────────────────────────────────────

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hr',  # your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for serving static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrpayroll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # point to your project-level templates folder
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'hrpayroll.wsgi.application'

# ─── DATABASES ─────────────────────────────────────────────────────────────────

if DEBUG:
    # Local development with SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Production with Postgres (set these env vars on Render)
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     os.getenv('DB_NAME'),
            'USER':     os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST':     os.getenv('DB_HOST'),
            'PORT':     os.getenv('DB_PORT', '5432'),
        }
    }

# ─── PASSWORD VALIDATION ───────────────────────────────────────────────────────

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

# ─── INTERNATIONALIZATION ──────────────────────────────────────────────────────

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dubai'
USE_I18N = True
USE_TZ = True

# ─── STATIC FILES ──────────────────────────────────────────────────────────────

# URL prefix for static files
STATIC_URL = '/static/'

# Where collectstatic will gather static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional locations to find static files (e.g. your local /static/ folder)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Use WhiteNoise’s compressed manifest storage backend in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ─── DEFAULT AUTO FIELD ────────────────────────────────────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─── AUTH REDIRECTS ────────────────────────────────────────────────────────────

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'       # or '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# ─── OPTIONAL EMAIL (for password reset) ───────────────────────────────────────

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST        = os.getenv('EMAIL_HOST')
# EMAIL_PORT        = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER   = os.getenv('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
# EMAIL_USE_TLS     = True
