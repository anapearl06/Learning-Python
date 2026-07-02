# Smart Inventory Filter

def smart_inventory_filter(products):
    # List comprehension
    low_price_products = [product["name"] for product in products if product["price"] < 500]

    # Set comprehension
    categories = {product["category"] for product in products}

    # Dictionary comprehension
    name_price = {product["name"]: product["price"] for product in products}

    # Generator expression
    discounted_prices = list(product["price"] * 0.9 for product in products)

    return (low_price_products, categories, name_price, discounted_prices)


products = [
    {"name": "Shampoo", "price": 250, "category": "Personal Care"},
    {"name": "Headphones", "price": 1200, "category": "Electronics"},
    {"name": "Notebook", "price": 100, "category": "Stationery"},
    {"name": "Pen", "price": 50, "category": "Stationery"},
]

result = smart_inventory_filter(products)

print(result)