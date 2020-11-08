import unittest
from cellar_backend.recipe import Recipe
from cellar_backend.ingredient import Ingredient
from parameterized import parameterized

class RecipeIngredientsTests(unittest.TestCase):

    def test_should_retrieve_ingredient(self):
        recipe = Recipe()
        recipe.add_ingredient('pożywka')
        ingredients = recipe.get_ingredients_list()
        assert self.ingredient_name_present_on_list( 'pożywka', ingredients )


    def test_should_retrieve_multiple_ingredients(self):
        recipe = Recipe()
        recipe.add_ingredient('pożywka')
        recipe.add_ingredient('cynamon')
        ingredients = recipe.get_ingredients_list()
        assert self.ingredient_name_present_on_list('pożywka', ingredients)
        assert self.ingredient_name_present_on_list('cynamon', ingredients)


    def test_should_retrieve_amount_of_ingredient(self):
        name = 'pożywka'
        recipe = Recipe()
        recipe.add_ingredient(name, amount = 1337)
        ingredients = recipe.get_ingredients_list()
        assert self.ingredient_name_present_on_list(name, ingredients)
        assert self.inrgedient_amount_present_on_list(name, 1337, ingredients)

    @parameterized.expand([
        ('pożywka', '3 g', 3, 'g'),
        ('sok', '5 l', 5, 'l')
    ])
    def test_should_retrieve_unit_of_amount(self, name, amount, expected_amount, expected_unit):
        recipe = Recipe()
        recipe.add_ingredient(name, amount= amount)
        ingredients = recipe.get_ingredients_list()
        assert self.ingredient_name_present_on_list(name, ingredients)
        assert self.inrgedient_amount_present_on_list(name, expected_amount, ingredients)
        assert self.ingredient_unit_present_on_list(name, expected_unit, ingredients)


    def ingredient_name_present_on_list(self, value, list):
        for element in list:
            if element.name == value:
                return True
        return False

    def inrgedient_amount_present_on_list(self, name,  value, list):
        for element in list:
            if element.name == name:
                return element.amount == value

    def ingredient_unit_present_on_list(self, name, unit, list):
        for element in list:
            if element.name == name:
                return element.unit == unit
