from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category': 'eat', 'descriptions': 'hamburher'},
            {'category': 'shose', 'descriptions': 'sneakers'},
            {'category': 'cloth', 'descriptions': 'shirt'},
            {'category': 'car', 'descriptions': 'kia'},
            {'category': 'phone', 'descriptions': 'iphone'},
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)
