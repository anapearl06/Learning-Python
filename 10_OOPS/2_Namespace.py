class Coffee:
    origin = "Colombia"

print(Coffee.origin)  # Colombia

Coffee.is_hot = True
print(Coffee.is_hot)  # True

powder = Coffee()
print(powder.origin)  # Colombia
print(powder.is_hot)  # True
