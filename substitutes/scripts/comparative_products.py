"""
COMPARATIVE PRODUCTS

Algorithm who take an list of products and compare their
nutritional values with each other.
"""

import json
from collections import OrderedDict
from substitutes.models import Product


class ComparativeProducts():

    def __init__(self):
        """
        ladder        (list): Result of the comparison. (List of products)
        """

        self.ladder = []

    def get_substitutes(self, reference=None, sample=None):

        averages = self.get_averages(sample=sample)
        ladder = self.get_ladder(
            reference=reference,
            sample=sample,
            averages=averages
        )

        return ladder

    def get_averages(self, sample=None):

        nutriment_names = [
            "salt",
            "saturated-fat",
            "sodium",
            "energy_kcal",
            "energy_kj",
            "fiber",
            "sugars",
            "proteins",
            "carbohydrates",
            "fat"
        ]

        medians = {
            "nutriscore": 0,
            "ingredients": 0,
            "salt": 0,
            "saturated-fat": 0,
            "sodium": 0,
            "energy_kcal": 0,
            "energy_kj": 0,
            "fiber": 0,
            "sugars": 0,
            "proteins": 0,
            "carbohydrates": 0,
            "fat": 0,
        }

        average = {
            "lower": 0,
            "median": 0,
            "upper": 0
        }

        averages = []

        for product in sample:

            medians[
                "nutriscore"
            ] = medians["nutriscore"] + int(product.nutriscore)

            product_ingredients = json.loads(product.ingredients)
            medians[
                "ingredients"
            ] = medians["ingredients"] + len(product_ingredients)

            nutriments = json.loads(product.nutriments)

            for nutriment_name in nutriment_names:
                medians[
                    nutriment_name
                ] = medians[nutriment_name] + nutriments[nutriment_name]

        for key, value in medians.items():

            if key == "nutriscore":
                medians[key] = int(value / len(sample))
            elif key == "ingredients":
                medians[key] = int(value / len(sample))
            else:
                medians[key] = round(value / len(sample), 2)

        return medians

    def get_ladder(self, reference=None, sample=None, averages=None):
        """
        reference (): Reference product to compare.
        sample    (): Products to compare to reference product.
        averages  (): Sample averages.
        """

        reference_score = self.get_score(product=reference, averages=averages)

        temp_ladder = []

        for product in sample:

            score = self.get_score(product=product, averages=averages)

            if score >= reference_score:

                product_ladder = {
                    "product": product,
                    "score": score
                }

                if product != reference:
                    temp_ladder.append(product_ladder)
                    temp_ladder.sort(key=lambda x: x['score'], reverse=False)

        for ladder_line in temp_ladder:
            self.ladder.append(ladder_line["product"])

        return self.ladder

    def get_score(self, product=None, averages=None):

        cat_names = ["nutriscore", "ingredients", "nutriments"]
        nut_names = [
            "salt",
            "saturated-fat",
            "sodium",
            "energy_kcal",
            "energy_kj",
            "fiber",
            "sugars",
            "proteins",
            "carbohydrates",
            "fat"
        ]

        score = 0

        for cat_name in cat_names:

            if cat_name == "nutriscore":

                if product.nutriscore <= averages["nutriscore"]:
                    score += 1

            elif cat_name == "ingredients":

                ingredients = json.loads(product.ingredients)

                if len(ingredients) <= averages["ingredients"]:
                    score += 1

            elif cat_name == "nutriments":

                nutriments = json.loads(product.nutriments)

                for nut_name in nut_names:

                    if nutriments[nut_name] <= averages[nut_name]:
                        score += 1

        return score
