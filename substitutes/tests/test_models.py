from django.test import TestCase
from substitutes.models import Product


class ProductTestCase(TestCase):

    def setUp(self):

        # For PEP8 (LINE TO LONG)
        off_url_1 = "https://static.openfoodfacts.org/images/products/"
        off_url_2 = "https://fr.openfoodfacts.org/produit/"

        Product.objects.create(
            name="Andouille non fumée",
            image="{}325/039/092/8300/front_fr.9.400.jpg".format(off_url_1),
            url="{}3250390928300/andouille-non-fumee-netto".format(off_url_2),
            creator="jacob80",
            brands="netto,les mousquetaires",
            stores="Netto",
            nutriscore=5,
            categories="\
                meats,\
                prepared-meats,\
                fresh-foods,\
                saucissons,\
                andouilles,\
                saucissons-cuits",
            ingredients='[\
                {"rank": 1, "text": "Chaudins", "id": "fr:Chaudins"}, \
                {"text": "rosettes", "id": "fr:rosettes", "rank": 2}, \
                {"rank": 3, "id": "fr:gras", "text": "gras"}, \
                {"rank": 4, "text": "sel", "id": "en:salt"}, \
                {"text": "\u00e9pices", "id": "en:spice", "rank": 5}, \
                {"rank": 6, "id": "en:spice", "text": "aromates"}, \
                {"rank": 7, "text": "conservateur", "id": "en:preservative"}, \
                {"text": "sodium", "id": "fr:nitrite-de-sodium", "rank": 8}, \
                {"rank": 9, "id": "en:flavouring", "text": "ar\u00f4mes"}]',
            nutriments='{\
                "carbohydrates": 0.0, \
                "carbohydrates_100g": 0, \
                "energy_kcal": 0, \
                "energy_kcal_100g": 0, \
                "energy_kj": 0, \
                "energy_kj_100g": 0, \
                "fat": 0, \
                "fat_100g": 0, \
                "fiber": 0, \
                "fiber_100g": 0, \
                "proteins": 0, \
                "proteins_100g": 0, \
                "salt": 0, \
                "salt_100g": 0, \
                "saturated-fat": 0, \
                "saturated-fat_100g": 0, \
                "sodium": 0, \
                "sodium_100g": 0, \
                "sugars": 0, \
                "sugars_100g": 0, \
                "sugars_block": 0 \
            }',
        )
