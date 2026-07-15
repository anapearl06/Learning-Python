class Coffee:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


#class LatteCoffee(Coffee):
#    def __init__(self, type_, strength, spice_level):
#        self.type = type_
#        self.strength = strength
#        self.spice_level = spice_level

#class LatteCoffee(Coffee):
#    def __init__(self, type_, strength, spice_level):
#        Coffee.__init__(self, type_, strength)
#        self.spice_level = spice_level


class LatteCoffee(Coffee):
    def __init__(self, type_, strength, spice_level):
        super().__init__(self, type_, strength)
        self.spice_level = spice_level
