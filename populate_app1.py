import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Django1.settings')

import django
django.setup()

import random
from app1.models import *
from faker import Faker

fakegen=Faker()
topics=['Search','Social','News','marketplace','games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for i in range(0,n):
        top=add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec=AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print('populating script!')
    populate(20)
    print('populated!!')