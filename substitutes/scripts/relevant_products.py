"""
RELEVANT PRODUCTS

Algorithm who search in database the most relevant products
for the reference product give in parameter.

This module need to have use import_products module.
"""

from django.core.exceptions import ObjectDoesNotExist
from substitutes.models import Product
import json


class RelevantProducts():

    def __init__(self, ref_product_id=None, relevant_level="5"):
        """
        ref_product_id              (int ): ID of ref enter in parameter.
        ref_product                 (Obj ): Django ref product orm object.
        relevant_products           (list): List of relevant_products.
        relevant_levels             (str ): Relevant level.
        products                    (list): List of database products.
        name_results                (list): Products list who matched whis ref.
        nbr_categories_results      (list): Products list who matched whis ref.
        nbr_ingredients_results     (list): Products list who matched whis ref.
        first_ingredient_results    (list): Products list who matched whis ref.
        first_category_results      (list): Products list who matched whis ref.
        """

        self.ref_product_id = ref_product_id
        self.ref_product = None
        self.products = Product.objects.all()
        self.relevant_products = []
        self.relevant_levels = relevant_level.split(",")

        self.name_results = []
        self.nbr_categories_results = []
        self.nbr_ingredients_results = []
        self.first_ingredient_results = []
        self.first_category_results = []

    def get_relevant_products(self):
        """
        All methods necessary to have relevant products.
        """

        # If the product are found
        if self.get_product() is True:

            self.name_match()
            self.nbr_categories_match()
            self.nbr_ingredients_match()
            self.first_ingredient_match()
            self.first_category_match()
            self.get_relevant_product_lists()

            return self.relevant_products

    def get_product(self):
        """
        1. Verify if the product exist in database with his ID.
        2. Add the product found in self.product variable.
        """

        result = False

        try:
            self.ref_product = Product.objects.get(
                id=self.ref_product_id
            )
            result = True
        except ObjectDoesNotExist:
            result = False

        return result

    def name_match(self):
        """
        This method search in database all products who have the
        same word in their name.
        """

        temp_name_results = Product.objects.filter(
            name__icontains=self.ref_product.name
        )

        for product in temp_name_results:

            self.name_results.append(product)

        return self.name_results

    def nbr_categories_match(self):
        """
        This method compare all categories products with referant
        product categories to find matchs.

        Why calculate the average number of categories ?
        Each products contains a different number of categories,
        it's not possible or desirable to define a median number
        of categories arbitrarily for all database products.
        So we calculate on each sample.
        """

        # Average number of categories
        nbr_categories = 0

        for product in self.products:

            product_categories = product.categories.split(",")
            nbr_categories += len(product_categories)

        nbr_categories = int(nbr_categories / len(self.products) / 2)

        # Categorie
        ref_categories = self.ref_product.categories.split(",")

        for product in self.products:

            product_categories = product.categories.split(",")

            cat_match = 0

            for ref_category in ref_categories:

                if ref_category in product_categories:

                    cat_match += 1

            if cat_match >= nbr_categories:

                self.nbr_categories_results.append(product)

        return self.nbr_categories_results

    def nbr_ingredients_match(self):
        """
        This method compare all products ingredients with referant
        product to find matchs.
        """

        # Average number of ingredients
        nbr_ingredients = 0

        for product in self.products:

            products_ingredients = json.loads(product.ingredients)
            nbr_ingredients += len(products_ingredients)

        nbr_ingredients = int(nbr_ingredients / len(self.products) / 2)

        # Ingredients
        ref_ingredients = json.loads(self.ref_product.ingredients)

        for product in self.products:

            product_ingredients = json.loads(product.ingredients)

            ing_match = 0

            for ref_ingredient in ref_ingredients:

                for product_ingredient in product_ingredients:

                    if ref_ingredient["id"] == product_ingredient["id"]:

                        ing_match += 1

            if ing_match >= nbr_ingredients:

                self.nbr_ingredients_results.append(product)

        return self.nbr_ingredients_results

    def first_ingredient_match(self):
        """
        This method compare all products first ingredient with referant
        product to find matchs.
        """

        # First ingredient
        ref_ingredients = json.loads(self.ref_product.ingredients)
        ref_first_ingredient = ref_ingredients[0]["id"]

        for product in self.products:

            product_ingredients = json.loads(product.ingredients)
            product_first_ingredient = product_ingredients[0]["id"]

            if ref_first_ingredient == product_first_ingredient:

                self.first_ingredient_results.append(product)

        return self.first_ingredient_results

    def first_category_match(self):
        """
        This method compare all products first categories with referant
        product to find matchs.
        """

        # First categories
        ref_categories = self.ref_product.categories.split(",")
        ref_first_category = ref_categories[0]

        for product in self.products:

            product_categories = product.categories.split(",")
            product_first_category = product_categories[0]

            if ref_first_category == product_first_category:

                self.first_category_results.append(product)

        return self.first_category_results

    def get_relevant_product_lists(self):
        """
        This method get relevant products.
        """

        for product in self.products:

            match = 0

            if product in self.name_results:
                match += 1

            if product in self.nbr_categories_results:
                match += 1

            if product in self.nbr_ingredients_results:
                match += 1

            if product in self.first_ingredient_results:
                match += 1

            if product in self.first_category_results:
                match += 1

            for relevant_level in self.relevant_levels:

                if match == int(relevant_level):
                    self.relevant_products.append(product)

        return self.relevant_products
