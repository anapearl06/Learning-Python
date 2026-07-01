# Managing Store Inventory

# Create sets
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

# Print both sets
print("Branch A Products:", branch_a_products)
print("Branch B Products:", branch_b_products)

# Union of both sets
print("Union:", branch_a_products.union(branch_b_products))

# Intersection of both sets
print("Intersection:", branch_a_products.intersection(branch_b_products))

# Products in Branch A but not in Branch B
print("Only in Branch A:", branch_a_products.difference(branch_b_products))

# Check if ketchup is in Branch A
print("Is ketchup available in Branch A?", "ketchup" in branch_a_products)

# Create a frozenset
essential_items = frozenset({"milk", "bread", "ketchup"})

# Print the frozenset
print("Essential Items:", essential_items)