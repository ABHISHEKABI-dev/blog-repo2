import os
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE","fakerproject.settings")
import django
django.setup()
f = Faker()
from myapp.models import Student
def populate(n):
    for i in range(n):
        fname = f.name()
        froll = f.random_int(min=1,max=20)
        marks = f.random_int(min=1,max=100)
        fdob = f.date_of_birth()
        femail = f.email()
        s = Student.objects.get_or_create(name=fname,roll=froll,marks=marks,dob=fdob,email=femail)
populate(20)
