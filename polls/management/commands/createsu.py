from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='SHUBHAM').exists():
            User.objects.create_superuser(
                username='SHUBHAM',
                password='SSSD#0101',
                email='bakade001122@gmail.com'
            )
            self.stdout.write('Superuser created.')
        else:
            self.stdout.write('Superuser already exists.')