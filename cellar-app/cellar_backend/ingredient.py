class Ingredient:
    name = None
    #this "amount" is dirty-should be obj Amount
    amount = None
    unit = None

    def __init__(self, name, amount = 1):
        self.name = name
        self.set_ingredient_amount(amount)

    def set_ingredient_amount(self, amount):
        try:
            split_amount_string = amount.split()
            self.amount =  int(split_amount_string[0])
            self.unit = split_amount_string[1]

        except AttributeError:
            self.amount = amount
