from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populate database using data factories in apps"

    def handle(self, *args, **options):
        self.setup_test_user()

    @staticmethod
    def setup_test_user():
        try:
            _ = User.objects.get(username="testuser")
        except User.DoesNotExist:
            u = User.objects.create_user("testuser", password="testpassword")
            u.is_superuser = True
            u.is_staff = True
            u.save()
