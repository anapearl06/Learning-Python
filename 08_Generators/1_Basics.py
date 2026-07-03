from webbrowser import get


def serve_coffee():
    yield "Cup 1: Capuccino"
    yield "Cup 2: Latte"
    yield "Cup 3: Espresso"
    yield "Cup 4: Americano"

stall = serve_coffee()

for cup in stall:
    print(cup)

def get_coffee_list():
    return ["Capuccino", "Latte", "Espresso", "Americano"]

def get_coffee_generator():
    yield "Capuccino"
    yield "Latte"
    yield "Espresso"
    yield "Americano"

coffee = get_coffee_generator()
print(next(coffee))
print(next(coffee))
print(next(coffee))
print(next(coffee))

