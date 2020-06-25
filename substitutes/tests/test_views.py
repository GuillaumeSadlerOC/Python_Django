"""
For more informations about django test :
https://docs.djangoproject.com/en/2.2/topics/testing/overview/

"""
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.test import TestCase, Client
from django.urls import reverse
from substitutes.models import Product


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="testing"
        )

        # For PEP8 (LINE TO LONG)
        off_url_1 = "https://static.openfoodfacts.org/images/products/"
        off_url_2 = "https://fr.openfoodfacts.org/produit/"

        cls.product = Product.objects.create(
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

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitutes/index.html')

    def test_results(self):
        response = self.client.post(
            reverse("results"), {
                'product-name': 'Bananne'
            }
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitutes/result.html')

    @login_required
    def test_favorites_connected(self):
        self.client.login(username="test", password="testing")
        response = self.client.get(reverse("favorites"))
        self.assertEquals(response.status_code, 200)

    @login_required
    def test_favorites_no_connected(self):
        response = self.client.get(reverse("favorites"))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/favorites')

    @login_required
    def test_add_favorite_connected(self):
        self.client.login(username="test", password="testing")
        response = self.client.get(
            reverse("add_favorite", args=[self.product.id])
        )
        self.assertEquals(response.status_code, 200)

    @login_required
    def test_add_favorite_no_connected(self):
        response = self.client.get(
            reverse("add_favorite", args=[self.product.id])
        )
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/add_favorite/{}'.format(
                self.product.id
            )
        )

    @login_required
    def test_del_favorite_connected(self):
        self.client.login(
            username="test", password="testing"
        )
        response = self.client.get(
            reverse(
                "del_favorite", args=[self.product.id]
            )
        )
        self.assertEquals(response.status_code, 200)

    @login_required
    def test_del_favorite_no_connected(self):
        response = self.client.get(
            reverse(
                "del_favorite", args=[self.product.id]
            )
        )
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/del_favorite/{}'.format(
                self.product.id
            )
        )

    def test_substitutes(self):
        response = self.client.get(
            reverse(
                "substitutes", args=[self.product.id]
            )
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'substitutes/sub_result.html'
        )

    def test_legales_notices(self):
        response = self.client.get(reverse("legales_notices"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'substitutes/legales_notices.html'
        )

    def test_product(self):
        response = self.client.get(reverse("product", args=[self.product.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'substitutes/product.html'
        )
