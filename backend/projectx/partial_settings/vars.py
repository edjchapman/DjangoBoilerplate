import os
from pathlib import Path


APPENV = os.getenv("APP_SETTINGS_ENV", "LOCAL")

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = APPENV != "PRODUCTION"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "projectx.urls"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") if APPENV == "PRODUCTION" else "TEST"

WSGI_APPLICATION = "projectx.wsgi.application"
