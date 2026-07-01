#chai = "Ginger Chai"

#def prepare_chai(order):
 #   print(f"Preparing {order}.")


#prepare_chai(chai)
#print(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(f"Making chai with {tea}, {milk}, and {sugar}.")

make_chai("Darjeeling", "whole milk", "brown sugar") #positional arguments
make_chai("Earl Grey", "skim milk", "honey") #positional arguments

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)
   
    special_chai(Cardamom="2 pods", Cinnamon="1 stick", Cloves="3 pods", Ginger="1 inch")
