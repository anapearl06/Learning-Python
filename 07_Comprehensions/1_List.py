menu = [
    "Cardamom Latte",
    "Cappuccino",
    "Espresso",
    "Flat White",
    "Latte",
    "Long Black"
]

#iced_coffee = [coffee for coffee in menu if "Iced" in coffee]
iced_coffee = [coffee for coffee in menu if len(coffee) > 12]
print(iced_coffee)