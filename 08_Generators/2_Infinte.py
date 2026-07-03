def infinte_coffee():
    count = 1
    while True:
        yield f"Cup {count}: Coffee"
        count += 1

refill = infinte_coffee()

for _ in range(5):
    print(next(refill))

for _ in range(8):
    print(next(refill))