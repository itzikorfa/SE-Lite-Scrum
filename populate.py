import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SE_Project_VerX.settings')

import django
django.setup()
from accounts.models import User
from faker import Faker



engine = Faker()

def create_user():
    try:
        name = "{}_{}".format(engine.first_name(),engine.last_name())
        email = engine.email()
        passwod = "lkjmnb123"
        user = User.objects.create_user(name,password= passwod)
        user.email = email
        user.save()
    except Exception as e:
        print("error creating user")


if __name__ == '__main__':
    for i in range(10):
        create_user()