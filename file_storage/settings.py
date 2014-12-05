import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ck-y6d!0lobj97i$m2d)-t0iv2&7khrnz)@ks0v$5p3g3&5kf8'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = ()

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'file_storage.urls'

WSGI_APPLICATION = 'file_storage.wsgi.application'

SENDFILE_BACKEND = 'sendfile.backends.development'
