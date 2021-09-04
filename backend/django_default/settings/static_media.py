import os

from .vars import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT')
