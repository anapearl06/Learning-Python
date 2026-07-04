class BaseCoffee:

    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_} coffee")


# Inheritance
class Latte(BaseCoffee):

    def add_ingredients(self):
        print("Adding coffee beans, milk, sugar, and water")


# Composition
class CoffeeShop:

    coffee_cls = BaseCoffee

    def __init__(self):
        self.coffee = self.coffee_cls("Regular")

    def serve(self):
        print(f"Serving {self.coffee.type_} coffee in the shop")


# Object of CoffeeShop
shop = CoffeeShop()
shop.coffee.prepare()
shop.serve()

print()

# Object of Latte
latte = Latte("Latte")
latte.prepare()
latte.add_ingredients()