ingredients = ["water","milk", "tea leaves","sugar"]
ingredients.append("cardamom")
print(f"Ingredients: {ingredients}")
ingredients.remove("sugar")
print(f"Ingredients: {ingredients}")

spice_options = ["ginger","cinnamon"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients: {chai_ingredients}")

chai_ingredients.insert(3, "tea leaves")
print(f"Chai Ingredients: {chai_ingredients}")  

last_ingredient = chai_ingredients.pop()
print(f"Removed ingredient: {last_ingredient}")
print(f"Chai Ingredients: {chai_ingredients}")

last_added_ingredient = chai_ingredients.pop()
print(f"{last_added_ingredient}")
print(f"Chai Ingredients: {chai_ingredients}")
print(f"chai: {chai_ingredients.reverse}")
chai_ingredients.reverse()
print(f"Chai Ingredients: {chai_ingredients}")  
chai_ingredients.sort()
print(f"Chai Ingredients: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"maximum sugar level: {max(sugar_levels)}")
print(f"minimum sugar level: {min(sugar_levels)}")

base_liquids = ["water", "milk"]
extra_flavour_to_chai = ["ginger", "cinnamon", "cardamom"]

full_liquid_mix = base_liquids + extra_flavour_to_chai
print(f"Full liquid mix: {full_liquid_mix}")

strong_tea = ["tea leaves"] * 3
print(f"Strong tea ingredients: {strong_tea}")

strong_brew = ["black tea", "water"] * 4
print(f"Strong brew ingredients: {strong_brew}")

raw_spice_mix = bytearray(b"Cardamom")
raw_spice_mix = raw_spice_mix.replace(b"Cardamom", b"Ginger")
print(f"Raw spice mix: {raw_spice_mix.decode('utf-8')}")

