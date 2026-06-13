chai_order = dict(type="Masala Chai", size="Large", sugar_level=3, extra_flavour="Ginger")
print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "cardamom"
chai_recipe["liquid"] = "milk"

print(f"Recipe_base: {chai_recipe['base']}")
print(f"Recipe_liquid: {chai_recipe['liquid']}")

del chai_recipe["base"]
print(f"Chai Recipe after deletion: {chai_recipe}")

print(f"Is 'sugar' in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar_level": 2, "extra_flavour": "Cinnamon"}

print(f"Updated Chai Order: {chai_order.keys()}")
print(f"Updated Chai Order values: {chai_order.values()}")
print(f"Updated Chai Order items: {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed item: {last_item}")
print(f"Chai Order after popitem: {chai_order}")

extra_spices = {"cardamom", "clove", "ginger"}
chai_recipe.update({"spices": extra_spices})

print(f"Updated Chai Recipe: {chai_recipe}")

chai_size = chai_order.get("size", "Unknown")

print(f"Chai size: {chai_size}")

