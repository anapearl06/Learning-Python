def coffee_customer():
    print("Customer: I would like a cup of coffee, please.")
    cup = yield
    while True:
        print(f"Customer: Thank you for the {cup}.")
        cup = yield

stall = coffee_customer()
next(stall)  # Start the generator   

stall.send("Capuccino") 
