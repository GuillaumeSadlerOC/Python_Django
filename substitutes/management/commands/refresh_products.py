import requests
from django.core.management.base import BaseCommand, CommandError
from substitutes.models import Product
from substitutes.scripts.import_products import ImportProducts


class Command(BaseCommand):

    help = 'Import Openfoodfacts products to database'

    def add_arguments(self, parser):
        parser.add_argument("category_name", nargs="+", type=str)
        parser.add_argument("language", nargs="+", type=str)

    def handle(self, *args, **options):

        # Delete all database products
        Product.objects.all().delete()

        # Import products to database
        new_product_import = ImportProducts()

        products = new_product_import.auto_products_import(
            language=options["language"][0],
            category_name=options["category_name"][0]
        )

        self.stdout.write(
            'Nombres de produits importés : {}'.format(products[1])
        )
