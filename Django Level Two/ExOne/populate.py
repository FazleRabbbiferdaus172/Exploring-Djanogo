import django
from faker import Faker
import random
import os


fakegen = Faker()


def populate(N=5):

    for _ in range(N):
        fake_name = fakegen.name().split(" ")
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        person = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating database")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExOne.settings')
    django.setup()
    from users.models import User
    populate()
    print("complete populating")
