#value = 13
#remainder = value % 5

#if remainder:
 #   print(f"Not devivisble, remainder is {remainder}")

value = 15

if remainder := value % 5:
    print(f"Not devivisble, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your cup size")) in available_sizes:
    print(f"Servings{requested_size} chai")

else:
    print(f"Size is unavaible - {requested_size}")

flavours = ["Red", "Black", "Mint", "Lemon"]

print = (f"Available floavours:", flavours)

while(flavours := input("choose your flavour:")) not in flavours:
    print(f"Sorry, {flavour} is not available")
    print(f" You choose {flavour} chai")