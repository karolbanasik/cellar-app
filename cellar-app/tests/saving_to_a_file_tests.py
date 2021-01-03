import unittest
from cellar_backend.recipe import Recipe
from parameterized import parameterized
from cellar_backend.permanency.csv_handler import CsvHandler
import os
import csv

class SavingToAFileTests(unittest.TestCase):

    basic_recipe_table = [['ingredient', 'amount', 'unit'],
                          ['kapusta', 1, 'kg'],
                          ['sól', 20, 'g']]

    def test_recipe_should_be_presentable_as_a_table(self):
        recipe = self.basic_recipe()
        recipe.save_recipe()
        assert recipe._table == self.basic_recipe_table

    def test_can_be_given_name(self):
        name = 'test'
        recipe = Recipe(name)
        assert recipe.name == name


    def test_should_write_to_csv(self):
        recipe = self.basic_recipe()
        recipe.save_recipe(CsvHandler)
        path_to_file = os.path.join(os.path.expanduser('~'), 'Documents', recipe.name + '.csv')
        with open(path_to_file, newline='') as csv_file:
            read_content = csv.reader(csv_file)
            counter = 0
            for row in read_content:
                stringified_row = self.list_items_to_string(self.basic_recipe_table[counter])
                assert stringified_row == row
                counter += 1
        os.remove(path_to_file)


    def basic_recipe(self):
        recipe = Recipe('kapusta kiszona')
        recipe.add_ingredient('kapusta', amount= '1 kg')
        recipe.add_ingredient('sól', amount= '20 g')
        return recipe

    def list_items_to_string(self, list):
        stringified_list = []
        for item in list:
            if isinstance(item, str):
                stringified_list.append(item)

            else:
                stringified_item = str(item)
                stringified_list.append(stringified_item)
        return stringified_list
