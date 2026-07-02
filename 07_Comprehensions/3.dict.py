coffee_prices_inr = {
    "Latte": 150,
    "Cappuccino": 200,
    "Flat White": 180,
    "Americano": 120,
    "Espresso": 100,
    "Affogato": 250
}

coffee_prices_usd = {coffee: price / 80 for coffee, price in coffee_prices_inr.items()}

print(coffee_prices_usd)

