"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'spam-spam-lovely-spam'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django_bootstrap_input_group',
    'app',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

STATIC_URL = 'static/'
