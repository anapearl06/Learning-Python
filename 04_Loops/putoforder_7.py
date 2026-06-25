flavours = ["Cardemom","out of stock", "Lemon", "discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print("discontinued item found")

print(f"Out side of loop")