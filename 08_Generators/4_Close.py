def local_coffee():
    yield "Cup 1: Capuccino"
    yield "Cup 2: Latte"
    yield "Cup 3: Espresso"
    yield "Cup 4: Americano"
    yield "Cup 5: Mocha"

def imported_coffee():
    yield "Cup 1: Americano"
    yield "Cup 2: Mocha"

def full_menu():
    yield from local_coffee()
    yield from imported_coffee()

for cup in full_menu():
    print(cup)

def coffee_stall():
    try:
       while True:
            order = yield "Cup: Capuccino"
    except:
        print("Stall is closed. No more orders can be taken.")

stall = coffee_stall()
print(next(stall))  # Start the generator
stall.close()  # Close the generator

