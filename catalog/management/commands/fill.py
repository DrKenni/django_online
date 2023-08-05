from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'name': 'Мясо', 'description': ''},
            {'name': 'Рыба', 'description': ''},
            {'name': 'Напитки', 'description': ''},
            {'name': 'Алкоголь', 'description': ''},
            {'name': 'Фрукты', 'description': ''},
            {'name': 'Овощи', 'description': ''},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Яблоко', 'price': '35', 'category': '5'},
            {'name': 'Помидор', 'price': '30', 'category': '6'},
            {'name': 'Пиво', 'price': '100', 'category': '4'},
            {'name': 'Тунец', 'price': '250', 'category': '2'},
            {'name': 'Кола', 'price': '100', 'category': '3'},
            {'name': 'Говядина', 'price': '350', 'category': '1'},
        ]

        products_for_create = []

        for products_item in product_list:
            products_for_create.append(
                Product(**products_item)
            )
        Product.objects.bulk_create(products_for_create)
