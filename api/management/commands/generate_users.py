from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

# python3 manage.py generate_users
class Command(BaseCommand):
    help = 'Generating users ... '

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_users = 100

        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = 'secret'  
                        
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))

        self.stdout.write(self.style.SUCCESS(f'Created {num_users} users successfully!'))
