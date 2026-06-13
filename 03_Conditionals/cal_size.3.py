cup = input("Choose the cup size (small/medium/large): ").lower()

if cup == "small":
    print(f"Price is ₹10")

elif cup == "medium":
    print(f"Price is ₹15")

elif cup == "large":
    print(f"Price is ₹20")

else: 
    print("Unknown cup size")