class Coffeecup:
    size = "90 ml"

    def describe(self):
        return f" A {self.size} coffee cup"

cup = Coffeecup()
print(cup.describe())  # A 90 ml coffee cup
print(Coffeecup.describe(cup))

cup_two = Coffeecup()
cup_two.size = "120 ml"
print(Coffeecup.describe(cup_two))
