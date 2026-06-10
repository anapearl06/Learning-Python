# Integers

black_tea_grams = 15
ginger_grams = 5

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea: {total_grams}") 

remaining_grams = black_tea_grams - ginger_grams
print(f"Remaining grams of black tea: {remaining_grams}")

milk_liters = 22
servings = 2
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving} liters")   

total_tea_bags = 10
pots = 4
tea_bags_per_pot = total_tea_bags // pots   
print(f"Tea bags per pot: {tea_bags_per_pot}") 

total_black_tea_grams = 15
pots_per_gram = 4
leftover_grams = total_black_tea_grams % pots_per_gram
print(f"Leftover grams of black tea: {leftover_grams} grams")

base_flavour_strength = 2
scale_factor = 3
scaled_flavour_strength = base_flavour_strength ** scale_factor  
print(f"Scaled flavour strength: {scaled_flavour_strength}")

total_tea_leaves_harvested = 100_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")