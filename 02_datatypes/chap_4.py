is_boiling = True
stir_counter = 5

#upcasting
total_actions = stir_counter + is_boiling
print(f"Total actions: {total_actions}")

milk_liters = 22
#downcasting
print(f"is_there_milk: {bool(milk_liters)}")

water_hot = True
tea_added = False
#logical operators
is_tea_ready = water_hot and tea_added
print(f"Is the tea ready? {is_tea_ready}")

tea_hot = True
cookies_ready = False
is_snack_time = tea_hot or cookies_ready
print(f"Is it snack time? {is_snack_time}")

  