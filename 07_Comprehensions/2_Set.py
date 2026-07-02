favourite_coffee = [
    "Latte", "Cappuccino", "Flat White",
    "Americano", "Espresso", "Affogato"
]

unique_coffee = {coffee for coffee in favourite_coffee if len(coffee) > 7}

print(unique_coffee)


recipes = {
    "Latte": ["Espresso", "Steamed Milk"],
    "Cappuccino": ["Espresso", "Steamed Milk", "Foamed Milk"],
    "Flat White": ["Espresso", "Steamed Milk"],
    "Americano": ["Espresso", "Hot Water"],
    "Espresso": ["Espresso"],
    "Affogato": ["Espresso", "Ice Cream"]
}

unique_spices = {ingredient for ingredients in recipes.values() for ingredient in ingredients if len(ingredient) > 5}
