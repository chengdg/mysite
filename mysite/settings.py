# coding: utf8
# Django settings for zjyw project.
from django.conf import settings  
settings.configure()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 会话关闭后自动删除session

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+f_nx3^g0#4d3pl6ypr22hp2+*@!8bvghvcw$r+v%qn=4!c=^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TIME_ZONE = "Etc/GMT-8"

LANGUAGE_CODE = 'zh-cn'

DEFAULT_CHARSET = 'utf-8'

ALLOWED_HOSTS = ['*']

FILE_CHARSET = 'iso-8859-1'

import logging
LOGLEVEL = logging.DEBUG


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',  
        'PORT': '3306',   
        
    }
}

DB_TYPE = 'mysql'
DB_CONSTR = dict( host='localhost',user='root',passwd='123456',db='mysite',port=3306)



STATIC_URL = '/static/'