essential_spices = {"cardamom", "cinnamon", "ginger"}
optional_spices = {"clove", "daalchini", "cardamom"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_essential = essential_spices - optional_spices
print(f"Only essential spices: {only_essential}")

only_optional = optional_spices - essential_spices
print(f"Only optional spices: {only_optional}")

print(f"Is 'cardamom' an essential spice? {'cardamom' in essential_spices}")
 