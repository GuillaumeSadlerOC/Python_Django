"""
PRODUCTS models
"""

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    image = models.URLField(max_length=300)
    url = models.URLField(max_length=300)
    creator = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    stores = models.TextField()
    nutriscore = models.IntegerField()
    categories = models.TextField()
    ingredients = models.TextField()
    nutriments = models.TextField()

    class Meta:
        verbose_name = "product"
        ordering = ['name']

    def __str__(self):
        return self.name


class ImportReport(models.Model):

    category_name = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    lenght = models.IntegerField()
    received_products = models.IntegerField()
    accepted_products = models.IntegerField()
    rejected_names = models.IntegerField()
    rejected_images = models.IntegerField()
    rejected_url = models.IntegerField()
    rejected_creator = models.IntegerField()
    rejected_stores = models.IntegerField()
    rejected_brands = models.IntegerField()
    rejected_nutriscore = models.IntegerField()
    rejected_nutriments_unit_g = models.IntegerField()
    rejected_nutriments_energy_unit = models.IntegerField()
    rejected_nutriments_energy_kcal = models.IntegerField()
    rejected_nutriments_energy_kj = models.IntegerField()
    rejected_categories = models.IntegerField()
    rejected_ingredients = models.IntegerField()

    class Meta:
        verbose_name = "import report"

    def __str__(self):
        return self.category_name
