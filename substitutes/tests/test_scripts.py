"""
For more informations about django test :
https://docs.djangoproject.com/en/2.2/topics/testing/overview/
"""

from django.test import TestCase
from substitutes.scripts.import_products import ImportProducts
from substitutes.scripts.relevant_products import RelevantProducts
from substitutes.scripts.comparative_products import ComparativeProducts
from substitutes.models import Product, ImportReport


class ImportProductTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        This method is called once when the test suite
        is started.
        """
        cls.import_products = ImportProducts()

    def setUp(self):
        """
        This method is called before each tests.
        """
        pass

    def test_get_off_categories_return(self):
        """
        This method test if what we receive from Openfoodfacts is
        a string.
        """
        categories = self.import_products.get_off_categories(
            language="fr",
            min_products=100
        )

        self.assertIs(type(categories), str)

    def test_get_off_products_return(self):
        """
        This method test if what we receive from Openfoodfacts is
        a string.
        """
        products = self.import_products.get_off_products(
            language="fr",
            category_name="saucissons"
        )

        self.assertIs(type(products), str)

    def test_get_clear_products(self):
        """
        This method test if the result of get_clear_products method
        is a list.
        """
        products = self.import_products.get_off_products(
            language="fr",
            category_name="saucissons"
        )
        product = self.import_products.get_clear_products()

        self.assertIs(type(product), list)

    def test_auto_products_import(self):
        """
        This method test if the result is correct.
        """

        result = self.import_products.auto_products_import(
            language="fr",
            category_name="produits-a-tartiner-sucres"
        )

        report = ImportReport.objects.all()

        self.assertIs(type(self.import_products.off_categories), str)
        self.assertIs(type(self.import_products.off_products), str)
        self.assertIs(type(self.import_products.clear_products), list)
        self.assertIs(type(result), tuple)
        self.assertEqual(len(report), 1)


class RelevantProductsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        This method is called once when the test suite
        is started.
        """
        cls.import_products = ImportProducts()
        cls.import_products.auto_products_import(
            language="fr",
            min_products=100,
            category_name="saucissons"
        )

        cls.ref_product = Product.objects.all().first()

        cls.relevant_product = RelevantProducts(
            ref_product_id=cls.ref_product.id
        )

    def setUp(self):
        """
        This method is called before each tests.
        """

        self.relevant_product.ref_product_id = self.ref_product.id

    def test_get_product_exist(self):
        """
        This method test if the referant product was found.
        """

        result = self.relevant_product.get_product()

        self.assertIs(type(result), bool)
        self.assertEqual(result, True)

    def test_get_product_no_exist(self):
        """
        This method test if the referant product was found.
        """

        self.relevant_product.ref_product_id = 1000000

        result = self.relevant_product.get_product()

        self.assertIs(type(result), bool)
        self.assertEqual(result, False)

    def test_relevant_products_return(self):

        self.relevant_product.get_product()
        name_match = self.relevant_product.name_match()
        cat_match = self.relevant_product.nbr_categories_match()
        ing_match = self.relevant_product.nbr_ingredients_match()
        first_ing_match = self.relevant_product.first_ingredient_match()
        first_cat_match = self.relevant_product.first_category_match()
        relevant_products = self.relevant_product.get_relevant_product_lists()

        self.assertIs(type(name_match), list)
        self.assertIs(type(cat_match), list)
        self.assertIs(type(ing_match), list)
        self.assertIs(type(first_ing_match), list)
        self.assertIs(type(first_cat_match), list)
        self.assertIs(type(relevant_products), list)

    def test_get_relevant_products(self):

        result = self.relevant_product.get_relevant_products()

        self.assertIs(type(result), list)


class ComparativeProductsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        This method is called once when the test suite
        is started.
        """

        # 1. IMPORT PRODUCTS TO DATABASE
        cls.import_products = ImportProducts()
        cls.import_products.auto_products_import(
            language="fr",
            min_products=100,
            category_name="saucissons"
        )

        # 2. GET REFERENCE PRODUCT
        cls.ref_product = Product.objects.all().first()

        # 3. GET RELEVANT PRODUCTS
        cls.relevant_product = RelevantProducts(
            ref_product_id=cls.ref_product.id,
            relevant_level="5,4,3,2"
        )
        cls.relevant_products = cls.relevant_product.get_relevant_products()

        # 4. GET COMPARATIVE PRODUCTS
        cls.comparative_product = ComparativeProducts()

    def setUp(self):
        """
        This method is called before each tests.
        """

        pass

    def test_get_averages(self):
        averages = self.comparative_product.get_averages(
            sample=self.relevant_products
        )
        self.assertIs(type(averages), dict)

    def test_get_ladder(self):

        averages = self.comparative_product.get_averages(
            sample=self.relevant_products
        )
        ladder = self.comparative_product.get_ladder(
            reference=self.ref_product,
            sample=self.relevant_products,
            averages=averages
        )

        self.assertIs(type(ladder), list)

    def test_get_substitutes(self):

        substitutes = self.comparative_product.get_substitutes(
            reference=self.ref_product,
            sample=self.relevant_products
        )

        self.assertIs(type(substitutes), list)
