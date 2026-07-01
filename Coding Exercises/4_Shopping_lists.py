# Shopping List

# Create a grocery list
my_cart = ["apples", "bananas", "milk"]

# Print the grocery list
print("Original List:", my_cart)

# Add "bread" to the end
my_cart.append("bread")
print("After Adding Bread:", my_cart)

# Insert "ketchup" at the beginning
my_cart.insert(0, "ketchup")
print("After Inserting Ketchup:", my_cart)

# Remove "bananas"
my_cart.remove("bananas")
print("After Removing Bananas:", my_cart)

# Remove the last item and store it
removed_item = my_cart.pop()
print("Removed Item:", removed_item)

# Extend the list
my_cart.extend(["rice", "butter"])
print("After Extending:", my_cart)

# Sort the list
my_cart.sort()
print("After Sorting:", my_cart)

# Reverse the list
my_cart.reverse()
print("After Reversing:", my_cart)

# Concatenate with another list
new_list = my_cart + ["juice", "jam"]
print("Concatenated List:", new_list)

# Duplicate the grocery list twice
duplicated_list = my_cart * 2
print("Duplicated List:", duplicated_list)

# Convert a string into a list
vegetables = "tomato cucumber spinach"
vegetable_list = vegetables.split()
print("Converted List:", vegetable_list)