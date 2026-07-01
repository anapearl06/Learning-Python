# Food Menu Selector

def get_item_price(item):
    match item.lower():
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"

# Take input from the user
item = input("Enter food item: ")

# Print the result
print(get_item_price(item))