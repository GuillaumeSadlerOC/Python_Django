"""
For more informations about django test :
https://docs.djangoproject.com/en/2.2/topics/testing/overview/

For more informations about reverse and resolve methods :
https://docs.djangoproject.com/en/2.2/ref/urlresolvers/
"""
from django.test import TestCase, Client
from django.urls import resolve, reverse
from substitutes.views import results, product, substitutes
from substitutes.views import favorites, add_favorite, del_favorite
from substitutes.views import index, legales_notices


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_index_url_is_resolved(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, index)

    def test_results_url_is_resolved(self):
        url = reverse("results")
        self.assertEquals(resolve(url).func, results)

    def test_product_url_is_resolved(self):
        url = reverse("product", args=[1])
        self.assertEquals(resolve(url).func, product)

    def test_substitutes_url_is_resolved(self):
        url = reverse("substitutes", args=[1])
        self.assertEquals(resolve(url).func, substitutes)

    def test_favorites_url_is_resolved(self):
        url = reverse("favorites")
        self.assertEquals(resolve(url).func, favorites)

    def test_add_favorite_url_is_resolved(self):
        url = reverse("add_favorite", args=[1])
        self.assertEquals(resolve(url).func, add_favorite)

    def test_del_favorite_url_is_resolved(self):
        url = reverse("del_favorite", args=[1])
        self.assertEquals(resolve(url).func, del_favorite)

    def test_legale_notice_url_is_resolved(self):
        url = reverse("legales_notices")
        self.assertEquals(resolve(url).func, legales_notices)
