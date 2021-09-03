import os

from django_default.settings import PROJECT_NAME, BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DEFAULT_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DEFAULT_DB_NAME', BASE_DIR.parent.parent / f'{PROJECT_NAME}.sqlite3'),
        'HOST': os.getenv('DJANGO_DEFAULT_DB_HOST'),
        'PORT': os.getenv('DJANGO_DEFAULT_DB_PORT'),
        'USER': os.getenv('DJANGO_DEFAULT_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DEFAULT_DB_PASSWORD'),
    },
}
