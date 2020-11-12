from cellar_backend.ingredient import Ingredient

class Recipe:
#represents recipe, thus an object combining ingredients and actions

    def __init__(self):
        self.ingredients = []


    def add_ingredient(self, name, **kwargs):
        amount = None

        if 'amount' in kwargs:
            amount = kwargs['amount']

        ingredient = Ingredient(name, amount)
        self.ingredients.append(ingredient)

    def get_ingredients_list(self):
        return self.ingredients

    def save_recipe(self):
        self._table=[['ingredient', 'amount', 'unit']]
        for i in self.ingredients:
            table_line = i.list_representation()
            self._table.append(table_line)