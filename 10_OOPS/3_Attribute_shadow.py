class Coffee:
    temperature = "hot"
    strength = "strong"

Latte = Coffee()
print(Latte.temperature)  # hot
print(Latte.strength)  # strong

Latte.temperature = "cold"
print(Latte.temperature)  # cold

print("After changing", Latte.temperature)
print("Before changing", Coffee.temperature)

del Latte.temperature
print("After deleting", Latte.temperature)
  
