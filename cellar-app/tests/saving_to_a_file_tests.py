import unittest
from cellar_backend.recipe import Recipe
from parameterized import parameterized

class SavingToAFileTests(unittest.TestCase):


    def test_recipe_should_be_presentable_as_a_table(self):
        recipe = self.basic_recipe()
        recipe.save_recipe()
        assert recipe._table == [['ingredient', 'amount', 'unit'],['kapusta', 1, 'kg'],['sól', 20, 'g']]


    def basic_recipe(self):
        recipe = Recipe()
        recipe.add_ingredient('kapusta', amount= '1 kg')
        recipe.add_ingredient('sól', amount= '20 g')
        return recipe
