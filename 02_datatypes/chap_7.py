masala_spices = {"Ginger", "Cardamom", "Lemon grass"}

(spice1, spice2, spice3) = masala_spices

print(f"Spice 1: {spice1}")
print(f"Spice 2: {spice2}")
print(f"Spice 3: {spice3}")

ginger_ratio, cardamom_ratio, lemon_grass_ratio = 3, 5, 2
print(f"Ginger ratio: {ginger_ratio}")
print(f"Cardamom ratio: {cardamom_ratio}")  
print(f"Lemon grass ratio: {lemon_grass_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping - Ginger ratio: {ginger_ratio}") 
print(f"After swapping - Cardamom ratio: {cardamom_ratio}")

#membership

print(f"Is Ginger in the masala mix? {'Ginger' in masala_spices}")
print(f"Is Cinnamon in the masala mix? {'Cinnamon' in masala_spices}")      
print(f"Is Cardamom in the masala mix? {'cardamom' in masala_spices}")