import csv
import datetime
import re
from django.core.management.base import BaseCommand
from phones.models import Phone


def str_to_date(str_date):
    pattern = re.compile(r'\d+')
    result = pattern.findall(str_date)
    correct_date = datetime.date(int(result[0]), int(result[1]), int(result[2]))
    return correct_date


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv') as f:
            phones = csv.DictReader(f, delimiter=';')
            for phone in phones:
                phone.pop(None)
                phone['release_date'] = str_to_date(phone['release_date'])
                slugged_name = phone['name'].replace(' ', '-')
                p = Phone(slug=slugged_name, **phone)
                p.save()
