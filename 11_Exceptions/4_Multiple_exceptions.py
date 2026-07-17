def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is{cost}")
    except KeyError:
        print("Sorry that chai is not available!!")
    except TypeError:
        print("Quantity must be in numm.. ")

process_order("ginger", 2)
process_order("masala", "two")
