import os

from django.core.wsgi import get_wsgi_application

from django_boilerplate.settings import PROJECT_NAME

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')

application = get_wsgi_application()
